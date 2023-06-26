import ctypes
from IMI.Neptune_API import *

class IMI_Attribute(object):
    def __init__(self,hCamHandle):
        self.hCamHandle = hCamHandle
       
    def IMI_exposuretime(self,value):
        puiMicroSec = ctypes.c_uint32(value)
        puiMin = ctypes.c_uint32(0)
        puiMax = ctypes.c_uint32(0)
        err = ntcSetExposureTime(self.hCamHandle, puiMicroSec)

    def IMI_ntcGetExposureTime(self):
        puiMicroSec = ctypes.c_uint32(0)
        puiMin = ctypes.c_uint32(0)
        puiMax = ctypes.c_uint32(0)
        err = ntcGetExposureTime(self.hCamHandle, ctypes.pointer(puiMicroSec), ctypes.pointer(puiMin), ctypes.pointer(puiMax))
        return puiMicroSec.value
    
    def IMI_getTriggerInfo(self):
        neptune_trigger_info = NEPTUNE_TRIGGER_INFO()
        err = ntcGetTriggerInfo(self.hCamHandle,ctypes.pointer(neptune_trigger_info))
        return neptune_trigger_info.nModeFlag
    
    def IMI_getTrigger(self):
        netune_trigger = NEPTUNE_TRIGGER()
        err = ntcGetTrigger(self.hCamHandle,ctypes.pointer(netune_trigger))
    
     
    def IMI_acquisition_mode(self,mode):
        if mode == "MultiFrame":
            mode = ENeptuneAcquisitionMode.NEPTUNE_ACQ_MULTIFRAME.value
        elif mode == "Continuous":
            mode = ENeptuneAcquisitionMode.NEPTUNE_ACQ_CONTINUOUS.value
        elif mode == "SingleFrame":
            mode = ENeptuneAcquisitionMode.NEPTUNE_ACQ_SINGLEFRAME.value

        #1. Acquisition Mode
        mode = ctypes.c_int32(mode)
        uiFrames = ctypes.c_uint32(2)
        err = ntcSetAcquisitionMode(self.hCamHandle,mode,uiFrames)
        # print("[{}] ntcSetAcquisitionMode err code ".format(err))
        
    def IMI_set_trigger(self,set_trigger_dict):
        netune_trigger = NEPTUNE_TRIGGER()
        
        if set_trigger_dict["trigger_source"] == 'Line1':
            trigger_source = ENeptuneTriggerSource.NEPTUNE_TRIGGER_SOURCE_LINE1.value
        elif set_trigger_dict["trigger_source"] == 'Software':
            trigger_source = ENeptuneTriggerSource.NEPTUNE_TRIGGER_SOURCE_SW.value
        if set_trigger_dict["trigger_mode"] == 'Mode0':
            trigger_mode = ENeptuneTriggerMode.NEPTUNE_TRIGGER_MODE_0.value
        elif set_trigger_dict["trigger_mode"] == 'Mode15':
            trigger_mode = ENeptuneTriggerMode.NEPTUNE_TRIGGER_MODE_15.value
        if set_trigger_dict["trigger_activation"] == 'RisingEdge':
            trigger_activation = ENeptunePolarity.NEPTUNE_POLARITY_RISINGEDGE.value
        elif set_trigger_dict["trigger_activation"] == 'FallingEdge':
            trigger_activation = ENeptunePolarity.NEPTUNE_POLARITY_FALLINGEDGE.value
        if set_trigger_dict["trigger_onoff"] == 'On':
            trigger_onoff = ENeptuneBoolean.NEPTUNE_BOOL_TRUE.value
        elif set_trigger_dict["trigger_onoff"] == 'Off':
            trigger_onoff = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value   
        
        trigger_source  = ctypes.c_int32(trigger_source)
        trigger_mode = ctypes.c_int32(trigger_mode)
        trigger_activation = ctypes.c_int32(trigger_activation)
        trigger_onoff = ctypes.c_int32(trigger_onoff)
        netune_trigger.Source = trigger_source
        netune_trigger.Mode = trigger_mode
        netune_trigger.Polarity = trigger_activation
        netune_trigger.OnOff = trigger_onoff
        err = ntcSetTrigger(self.hCamHandle,netune_trigger)
        
    def IMI_run_sw_trigger(self):
        ntcSetTriggerDelay(self.hCamHandle, 500);
        ntcRunSWTrigger(self.hCamHandle);
        
    def IMI_ntcGetFeature(self):
        FeatureInfo = NEPTUNE_FEATURE()
        pixelformat = ctypes.c_int32(0)
        err = ntcGetPixelFormat(self.hCamHandle, ctypes.pointer(pixelformat))
        err = ntcGetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_GAMMA.value, ctypes.pointer(FeatureInfo))
        gamma = FeatureInfo.Value
        err = ntcGetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_SHARPNESS.value, ctypes.pointer(FeatureInfo))
        sharpness = FeatureInfo.Value
        err = ntcGetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_CONTRAST.value, ctypes.pointer(FeatureInfo))
        contrast = FeatureInfo.Value
        exposure = self.IMI_ntcGetExposureTime()
        RotInfo = ctypes.c_int32(0)
        err = ntcGetRotation(self.hCamHandle,ctypes.pointer(RotInfo))
        feature_info = {
            "pixel_format":pixelformat.value,
            "sharpness" : sharpness,
            "contrast"  : contrast,
            "exposure"  : exposure,
            "white_balance_execution":False,
        }
        return feature_info
    
    def IMI_ntcSetFeature(self,feature_info):
        now_feature_info = self.IMI_ntcGetFeature()
        pixel_format = feature_info["pixel_format"]
        pixel_format = 101 if pixel_format=="gray" else 109
        if now_feature_info["pixel_format"]!=pixel_format:
            ntcSetPixelFormat(self.hCamHandle, pixel_format)
        
        sharpness = feature_info["sharpness"]
        FeatureInfo = NEPTUNE_FEATURE()
        try:
            FeatureInfo.Value = sharpness
        except TypeError as e:
            pass
        if now_feature_info["sharpness"]!=sharpness:
            ntcSetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_SHARPNESS.value, FeatureInfo)
        contrast = feature_info["contrast"]
        FeatureInfo = NEPTUNE_FEATURE()
        try:
            FeatureInfo.Value = contrast
        except TypeError as e:
            pass
        if now_feature_info["contrast"]!=contrast:
            ntcSetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_SHARPNESS.value, FeatureInfo)
        exposure = feature_info["exposure"]
        puiMicroSec = ctypes.c_uint32(exposure)
        if now_feature_info["exposure"]!=exposure:
            ntcSetExposureTime(self.hCamHandle, puiMicroSec)
        white_balance_execution = feature_info["white_balance_execution"]
            
    
    def IMI_ntcSetFeature(self,value,mode):
        FeatureInfo = NEPTUNE_FEATURE()
        try:
            FeatureInfo.Value = value
        except TypeError as e:
            pass
        if mode =="sharpness":
            err = ntcSetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_SHARPNESS.value, FeatureInfo);

        elif mode =="contrast":
            err = ntcSetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_CONTRAST.value, FeatureInfo);

        elif mode =="whitebalance":
            err = ntcSetAcquisition(self.hCamHandle, ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value);
            value = ctypes.c_uint8(2)
            FeatureInfo.SupportAutoModes = value
            #12. whiteBalance
            err = ntcSetFeature(self.hCamHandle, ENeptuneFeature.NEPTUNE_FEATURE_WHITEBALANCE.value, FeatureInfo);
            err = ntcSetAcquisition(self.hCamHandle, ENeptuneBoolean.NEPTUNE_BOOL_TRUE.value);
