import ctypes
import numpy as np
import time
import cv2
import random
from multiprocessing.shared_memory import SharedMemory
from typing import List
from multiprocessing import Queue
from IMI.imi_attribute import IMI_Attribute
from threading import Thread
# from Neptune_API import NEPTUNE_IMAGE,ntcInit,ntcGetCameraCount,ntcOpen,NEPTUNE_IMAGE_SIZE,ntcGetImageSize,ntcGetPixelFormatList,ntcSetPixelFormat,ENeptuneBoolean, \
#     ntcSetFrameCallback,ntcSetAcquisition,NEPTUNE_CAM_INFO,ntcGetCameraInfo,ENeptuneError
from .Neptune_API import NEPTUNE_IMAGE,ntcInit,ntcGetCameraCount,ntcOpen,NEPTUNE_IMAGE_SIZE,ntcGetImageSize,ntcGetPixelFormatList,ntcSetPixelFormat,ENeptuneBoolean, \
    ntcSetFrameCallback,ntcSetAcquisition,NEPTUNE_CAM_INFO,ntcGetCameraInfo,ENeptuneError
from copy import deepcopy
from typing import Dict,List
def imi_run(camera2inference_queue:Queue,feedback2camera_queue:Queue,config:Dict):
    camera = IMI_Camera(camera2inference_queue,feedback2camera_queue,config)

class IMI_Camera(object):
    def __init__(self,camera2inference_queue:Queue,feedback2camera_queue:Queue,config:Dict):
        self.camera2inference_queue = camera2inference_queue
        self.feedback2camera_queue = feedback2camera_queue
        self.config=config
        self.set_config(self.config)
        self.total_frame_count=0
        ntcInit()
        nNums = ctypes.c_uint32(0)
        ntcGetCameraCount(ctypes.pointer(nNums))
        self.hCamHandle = ctypes.c_void_p(0)
        CamID = b'00:09:7e:24:08:31'
        ntcOpen(CamID, ctypes.byref(self.hCamHandle))
        ImageSize = NEPTUNE_IMAGE_SIZE()
        ntcGetImageSize(self.hCamHandle, ctypes.pointer(ImageSize))
        ntcGetPixelFormatList(self.hCamHandle, None, ctypes.pointer(nNums))
        pPixelFmtList = (ctypes.c_int32 * nNums.value)()
        ctypes.cast(pPixelFmtList,ctypes.POINTER(ctypes.c_int32))
        ntcSetPixelFormat(self.hCamHandle, self.image_format)
        callback_type = ctypes.CFUNCTYPE(None, NEPTUNE_IMAGE, ctypes.c_void_p)
        self.callback_func = callback_type(self.RecvFrameCallBack)
        self.imi_attributes = IMI_Attribute(self.hCamHandle)
        dic = self.trigger_dict()
        dic["trigger_onoff"] = "Off"
        self.images_list=[]
        self.imi_attributes.IMI_set_trigger(dic)
        background_thread = Thread(target = self.stream)
        background_thread.start()
        # buffer_check_thread = Thread(target = self.camera_buffer_check)
        # buffer_check_thread.start()
        self.start()
        self.stop()
        self.start()

    def camera_buffer_check(self,):
        while True:
            time.sleep(5)
            print("Camera Buffer Stack : ", len(self.images_list))

    def __del__(self):
        ntcSetAcquisition(self.hCamHandle, ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value)
        
    def stream(self):
        while True:
            data = self.feedback2camera_queue.get()
            while True:
                try:
                    encoded_image,size,width,height = self.images_list.pop()
                    self.images_list.clear()
                    break
                except:
                    continue
            image = encoded_image.reshape(height,width) if size==height*width else encoded_image.reshape(height,width,-1)
            self.camera2inference_queue.put(image)
            self.total_frame_count+=1

    def make_data(self,shape,data):
        new_data = deepcopy(data)
        new_data["time"]=time.time()
        new_data["image_shape"] = shape
        return new_data

    def RecvFrameCallBack(self,pImage, pContext=None):
        encoded_img = np.frombuffer(pImage.pData[0:pImage.uiSize], dtype = np.uint8).copy()
        self.images_list.append([encoded_img,pImage.uiSize,pImage.uiWidth,pImage.uiHeight,])

    def do_command(self,data):
        for command_camera in data["command_camera"]:
            if command_camera == "TriggerOn":
                self.stop()
                dic = self.trigger_dict()
                dic["trigger_onoff"] = "On"
                self.imi_attributes.IMI_set_trigger(dic)
                self.images_list.clear()
                self.start()

            elif command_camera == "TriggerOff":
                dic = self.trigger_dict()
                dic["trigger_onoff"] = "Off"
                self.imi_attributes.IMI_set_trigger(dic)
    def trigger_dict(self):
        result = {
            "trigger_source":"Line1",
            "trigger_mode":"Mode15",
            "trigger_activation":"FallingEdge",
            "trigger_onoff":"On"
        }
        return result
        
    def start(self):
        err = ntcSetPixelFormat(self.hCamHandle, self.image_format)
        err  = ntcSetAcquisition(self.hCamHandle, ENeptuneBoolean.NEPTUNE_BOOL_TRUE.value)
        err = ntcSetFrameCallback(self.hCamHandle, self.callback_func, self.hCamHandle)
    def stop(self):
        err = ntcSetAcquisition(self.hCamHandle, ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value)

    def set_config(self,config):
        image_format = config["pixel_format"]
        self.image_format = 101 if image_format.lower()=="gray" else 105
        engine_nums = config["engine_nums"]
        self.engine_nums = engine_nums
        shared_memory_name = config["shared_memory_name"]
        self.shared_memory_name = shared_memory_name
        camera_running = config['camera_running']
        self.camera_running = camera_running
        inference_running = config['inference_running']
        self.inference_running=inference_running
