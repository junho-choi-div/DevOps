config = {
    "camera_width":1440, # 카메라에서 오는 사진의 넓이
    "camera_height":1080, # 카메라에서 오는 사진의 높이
    "sharpness":10,
    "contrast":512,
    "exposure":10000,
    "inference_width":640, # 실제 추론할 때 이미지 넓이
    "inference_height":640, # 실제 추론할 때 이미지 높이
    "dtype":"np.float32", # np.float16 // np.float32
    "trt_path":None,
    "shared_memory_nums":3000,
    "confidence":0.8,
    "engine_nums":3,
    "shared_memory_not_inference":"GLOBAL_RAM_not_inference",
    "shared_memory_name":"GLOBAL_RAM",
    "pixel_format":"gray", # gray or color
    # "display_max_FPS":30,
    "inference_running":-1,
    "camera_running":1, # 1 : rugging 0 : stop -1 exit
    "mode" : "Trigger", # Trigger OR Continuous
    # "save_image_path" : os.path.join(DESKTOP_PATH,"results"),
    "session_name":"검사자이름",
    "collecter_nums" : 6,
    "size_per_one_inference_unit":350,
    "total_frame_per_one_cycle":round(73*13.2),
}