# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:29:49 2022

@author: Park Hyeon Gyu

"""

import ctypes
from enum import Enum
from pathlib import Path


"""
NUMBER_DEFINE

"""

MAX_NODE_LIST_COUNT				= 128	# for XML tree node
MAX_ENUM_LIST_COUNT				= 64	# for enumeration
MAX_XML_NODE_STRING_LENGTH		= 256
MAX_STRING_LENGTH				= 512
MAC_LENGTH						= 32
MAX_INTERFACE_NUM				= 140
MAX_TRIGGER_PARAM				= 255
KNEE_POINT_TABLE_SIZE			= 4
USER_LUT_TABLE_SIZE				= 4096


"""
ENUMERATE_DEFINE

"""
class ENeptuneError(Enum):
 	NEPTUNE_ERR_Fail					= -1
 	NEPTUNE_ERR_Success					= 0
 	NEPTUNE_ERR_AlreadyInitialized		= -100
 	NEPTUNE_ERR_APINotInitialized		= -101
 	NEPTUNE_ERR_NotInitialized			= -102
 	NEPTUNE_ERR_GC						= -103
 	NEPTUNE_ERR_TimeOut					= -104
 	NEPTUNE_ERR_NotSupportedFunc		= -105
 	NEPTUNE_ERR_OpenXML					= -106
 	NEPTUNE_ERR_InvalidValue			= -107
 	NEPTUNE_ERR_EventChannel			= -108
 	NEPTUNE_ERR_NotReady				= -109
 	NEPTUNE_ERR_PacketResend			= -110
 	NEPTUNE_ERR_InvalidFeatureRange		= -111
 	NEPTUNE_ERR_TLInterface				= -112
 	NEPTUNE_ERR_TLDevOpen				= -113
 	NEPTUNE_ERR_TLDevPort				= -114
 	NEPTUNE_ERR_TLDevURL				= -115
 	NEPTUNE_ERR_GrabTimeout				= -116
 	NEPTUNE_ERR_DeviceNotExist			= -117
 	NEPTUNE_ERR_TLInitFail				= -200
 	NEPTUNE_ERR_NoInterface				= -201
 	NEPTUNE_ERR_DeviceCheck				= -202
 	NEPTUNE_ERR_InvalidParameter		= -203
 	NEPTUNE_ERR_NotSupport				= -204
 	NEPTUNE_ERR_AccessDenied			= -205
 	NEPTUNE_ERR_InvalidAddress			= -206
 	NEPTUNE_ERR_InvalidArraySize		= -207
 	NEPTUNE_ERR_Interface				= -208
 	NEPTUNE_ERR_DeviceInfo				= -209
 	NEPTUNE_ERR_MemoryAlloc				= -210
 	NEPTUNE_ERR_DeviceOpen				= -211
 	NEPTUNE_ERR_DevicePort				= -212
 	NEPTUNE_ERR_DeviceURL				= -213
 	NEPTUNE_ERR_DeviceWrite				= -214
 	NEPTUNE_ERR_DeviceXML				= -215
 	NEPTUNE_ERR_DeviceHeartbeat			= -216
 	NEPTUNE_ERR_DeviceClose				= -217
 	NEPTUNE_ERR_DeviceNotStreaming		= -218
 	NEPTUNE_ERR_InvalidXMLNode			= -300
 	NEPTUNE_ERR_StreamCount				= -303
 	NEPTUNE_ERR_AccessTimeOut			= -304
 	NEPTUNE_ERR_OutOfRange				= -305
 	NEPTUNE_ERR_InvalidChannel			= -306
 	NEPTUNE_ERR_InvalidBuffer			= -307
 	NEPTUNE_ERR_FileAccessError			= -400
 	NEPTUNE_ERR_GrabFrameDropped		= -450
##########################################################################
class ENeptuneBoolean(Enum):
 	NEPTUNE_BOOL_FALSE		= 0
 	NEPTUNE_BOOL_TRUE		= 1
##########################################################################
class ENeptuneEffect(Enum):
 	NEPTUNE_EFFECT_NONE		= 0
 	NEPTUNE_EFFECT_FLIP		= 0x01		# flip image
 	NEPTUNE_EFFECT_MIRROR	= 0x02		# mirror
 	NEPTUNE_EFFECT_NEGATIVE	= 0x04		# negative
##########################################################################    
class ENeptuneAutoMode(Enum):
 	NEPTUNE_AUTO_OFF				= 0		# manual mode
 	NEPTUNE_AUTO_ONCE				= 1		# once(one-shot) mode
 	NEPTUNE_AUTO_CONTINUOUS			= 2		# auto mode
##########################################################################	
class ENeptunePixelFormat(Enum):
 	Unknown_PixelFormat			= -1
 	# 1394 Camera pixel format list.
 	Format0_320x240_YUV422		= 0
 	Format0_640x480_YUV411		= 1
 	Format0_640x480_YUV422		= 2
 	Format0_640x480_Mono8		= 3
 	Format0_640x480_Mono16		= 4
 	Format1_800x600_YUV422		= 5
 	Format1_800x600_Mono8		= 6
 	Format1_1024x768_YUV422		= 7
 	Format1_1024x768_Mono8		= 8
 	Format1_800x600_Mono16		= 9
 	Format1_1024x768_Mono16		= 10

 	Format2_1280x960_YUV422		= 11
 	Format2_1280x960_Mono8		= 12
 	Format2_1600x1200_YUV422	= 13
 	Format2_1600x1200_Mono8		= 14
 	Format2_1280x960_Mono16		= 15
 	Format2_1600x1200_Mono16	= 16

 	Format7_Mode0_Mono8			= 17
 	Format7_Mode0_YUV411		= 18
 	Format7_Mode0_YUV422		= 19
 	Format7_Mode0_Mono16		= 20
 	Format7_Mode0_Raw8			= 21
 	Format7_Mode0_Raw16			= 22
 	Format7_Mode0_Mono12		= 23
 	Format7_Mode0_Raw12			= 24

 	Format7_Mode1_Mono8			= 25
 	Format7_Mode1_YUV411		= 26
 	Format7_Mode1_YUV422		= 27
 	Format7_Mode1_Mono16		= 28
 	Format7_Mode1_Raw8			= 29
 	Format7_Mode1_Raw16			= 30
 	Format7_Mode1_Mono12		= 31
 	Format7_Mode1_Raw12			= 32

 	Format7_Mode2_Mono8			= 33
 	Format7_Mode2_YUV411		= 34
 	Format7_Mode2_YUV422		= 35
 	Format7_Mode2_Mono16		= 36
 	Format7_Mode2_Raw8			= 37
 	Format7_Mode2_Raw16			= 38
 	Format7_Mode2_Mono12		= 39
 	Format7_Mode2_Raw12			= 40

 	# GigE/USB3 Camera pixel format list.
 	Mono8						= 101
 	Mono10						= 102
 	Mono12						= 103
 	Mono16						= 104
 	BayerGR8					= 105
 	BayerGR10					= 106		
 	BayerGR12					= 107		
 	YUV411Packed				= 108
 	YUV422Packed				= 109
 	YUV422_8					= 110
 	BayerRG8					= 111
 	BayerRG12					= 112
 	BayerGB8					= 113
 	BayerGB12					= 114
 	BayerBG8					= 115
 	BayerBG12					= 116
 	Profile32					= 117
##########################################################################
class ENeptunePixelType(Enum):
 	NEPTUNE_PIXEL_MONO			= 1
 	NEPTUNE_PIXEL_BAYER			= 2
 	NEPTUNE_PIXEL_RGB			= 3
 	NEPTUNE_PIXEL_YUV			= 4
 	NEPTUNE_PIXEL_RGBPLANAR		= 5
 	NEPTUNE_PIXEL_YUV_8			= 6
 	NEPTUNE_PIXEL_MONO_OR_BAYER	= 7
##########################################################################     
class ENeptuneFrameRate(Enum):
 	FPS_UNKNOWN			= -1
 	FPS_1_875			= 0			# 1.875 frame (1394 camera)
 	FPS_3_75			= 1			# 3.75 frame (1394 camera)
 	FPS_7_5				= 2			# 7.5 frame (1394 camera)
 	FPS_15				= 3			# 15 frame (1394 camera)
 	FPS_30				= 4			# 30 frame (1394 camera)
 	FPS_60				= 5			# 60 frame (1394 camera)
 	FPS_120				= 6			# 120 frame (1394 camera)
 	FPS_240				= 7			# 240 frame (1394 camera)
 	FPS_VALUE			= 20		# frame rate value(GigE and USB3 camera)
##########################################################################
class ENeptuneBayerLayout(Enum):
 	NEPTUNE_BAYER_GB_RG = 0	       	# GB/RG layout
 	NEPTUNE_BAYER_BG_GR = 1	        # BG/GR layout
 	NEPTUNE_BAYER_RG_GB = 2		    # RG/GB layout
 	NEPTUNE_BAYER_GR_BG = 3			# GR/BG layout
##########################################################################
class ENeptuneBayerMethod(Enum):
 	NEPTUNE_BAYER_METHOD_NONE      = 0		# no bayer conversion
 	NEPTUNE_BAYER_METHOD_BILINEAR  = 1		# bilinear conversion
 	NEPTUNE_BAYER_METHOD_HQ        = 2		# HQ conversion
 	NEPTUNE_BAYER_METHOD_NEAREST   = 3		# nearest conversion
##########################################################################
class ENeptuneAcquisitionMode(Enum):
 	NEPTUNE_ACQ_CONTINUOUS		= 0			    # continuous
 	NEPTUNE_ACQ_MULTIFRAME		= 1		  	    # multi frame
 	NEPTUNE_ACQ_SINGLEFRAME		= 2				# single frame
##########################################################################
class ENeptuneStreamMode(Enum):
 	NEPTUNE_STRM_UNICAST	= 0
 	NEPTUNE_STRM_MULTICAST	= 1
##########################################################################
class ENeptuneImageFormat(Enum):
 	NEPTUNE_IMAGE_FORMAT_UNKNOWN	= -1
 	NEPTUNE_IMAGE_FORMAT_BMP		= 0
 	NEPTUNE_IMAGE_FORMAT_JPG		= 1
 	NEPTUNE_IMAGE_FORMAT_TIF		= 2
##########################################################################
class ENeptuneGrabFormat(Enum):
 	NEPTUNE_GRAB_RAW	= 0
 	NEPTUNE_GRAB_RGB	= 1
 	NEPTUNE_GRAB_RGB32	= 2
##########################################################################
class ENeptuneDeviceChangeState(Enum):
 	NEPTUNE_DEVICE_ADDED		= 0  	# camera count is increased
 	NEPTUNE_DEVICE_REMOVED		= 1		# camera count is decreased
##########################################################################
class ENeptuneRotationAngle(Enum):
 	NEPTUNE_ROTATE_0		= 0 		# 0 degree
 	NEPTUNE_ROTATE_90		= 1 	 	# 90 degree
 	NEPTUNE_ROTATE_180		= 2 		# 180 degree
 	NEPTUNE_ROTATE_270		= 3			# 270 degree
##########################################################################
class ENeptuneCameraListOpt(Enum):
 	NEPTUNE_CAMERALISTOPT_ONLYIMI  = 0
 	NEPTUNE_CAMERALISTOPT_ALL      = 1
##########################################################################
class ENeptuneDisplayOption(Enum):
 	NEPTUNE_DISPLAY_OPTION_FIT             = 0
 	NEPTUNE_DISPLAY_OPTION_ORIGINAL_CENTER = 1

##########################################################################
class ENeptune1394Foramt(Enum):
 	FORMAT_0 = 0
 	FORMAT_1 = 1
 	FORMAT_2 = 2
 	FORMAT_7 = 7
##########################################################################
class ENeptuneDevType(Enum):
 	NEPTUNE_DEV_TYPE_UNKNOWN	= -1	# unknown camera
 	NEPTUNE_DEV_TYPE_1394		= 0 	# 1394 camera
 	NEPTUNE_DEV_TYPE_USB3		= 1 	# USB3 Vision camera
 	NEPTUNE_DEV_TYPE_GIGE		= 2		# GigE camera
##########################################################################
class ENeptuneDevAccess(Enum):
 	NEPTUNE_DEV_ACCESS_UNKNOWN		= -1
 	NEPTUNE_DEV_ACCESS_EXCLUSIVE	= 0
 	NEPTUNE_DEV_ACCESS_CONTROL		= 1
 	NEPTUNE_DEV_ACCESS_MONITOR		= 2
##########################################################################
class ENeptuneFeature(Enum):
 	NEPTUNE_FEATURE_GAMMA				= 0 	# AnalogControls, Gamma
 	NEPTUNE_FEATURE_GAIN				= 1 	# AnalogControls, Gain or GainRaw
 	NEPTUNE_FEATURE_RGAIN				= 2 	# AnalogControls, Gain or GainRaw
 	NEPTUNE_FEATURE_GGAIN				= 3 	# AnalogControls, Gain or GainRaw
 	NEPTUNE_FEATURE_BGAIN				= 4 	# AnalogControls, Gain or GainRaw
 	NEPTUNE_FEATURE_BLACKLEVEL			= 5 	# AnalogControls, BlackLevel or BlackLevelRaw
 	NEPTUNE_FEATURE_SHARPNESS			= 6 	# AnalogControls, Sharpness or SharpnessRaw
 	NEPTUNE_FEATURE_SATURATION			= 7 	# AnalogControls, Saturation or SaturationRaw
 	NEPTUNE_FEATURE_AUTOEXPOSURE		= 8 	# AcquisitionControl, AutoExposure
 	NEPTUNE_FEATURE_SHUTTER				= 9 	# AcquisitionControl, ExposureTime
 	NEPTUNE_FEATURE_HUE					= 10	# AnalogControls, Hue or HueRaw
 	NEPTUNE_FEATURE_PAN					= 11	# AcquisitionControl, PanCtrl
 	NEPTUNE_FEATURE_TILT				= 12	# AcquisitionControl, TiltCtrl
 	NEPTUNE_FEATURE_OPTFILTER			= 13	# AnalogControls, OpticalFilter
 	NEPTUNE_FEATURE_AUTOSHUTTER_MIN		= 14	# CustomControl, AutoShutterSpeedMin
 	NEPTUNE_FEATURE_AUTOSHUTTER_MAX		= 15	# CustomControl, AutoShutterSpeedMin
 	NEPTUNE_FEATURE_AUTOGAIN_MIN		= 16	# CustomControl, AutoGainMin
 	NEPTUNE_FEATURE_AUTOGAIN_MAX		= 17	# CustomControl, AutoGainMax
 	NEPTUNE_FEATURE_TRIGNOISEFILTER		= 18	# CustomControl, TriggerNoiseFilter
 	NEPTUNE_FEATURE_BRIGHTLEVELIRIS		= 19	# CustomControl, BrightLevelForIRIS (Read Only)
 	NEPTUNE_FEATURE_SNOWNOISEREMOVE		= 20	# CustomControl, SnowNosieRemoveControl
 	NEPTUNE_FEATURE_WATCHDOG			= 21	# CustomControl, WDGControl
 	NEPTUNE_FEATURE_WHITEBALANCE		= 22	# AnalogControls, BalanceWhiteAudo
 	NEPTUNE_FEATURE_CONTRAST			= 23	# CustomControl, Contrast
 	NEPTUNE_FEATURE_LCD_BLUE_GAIN		= 24	# CustomControl, LED_BLUE_GAIN
 	NEPTUNE_FEATURE_LCD_RED_GAIN		= 25	# CustomControl, LED_RED_GAIN
##########################################################################
class ENeptuneUserSet(Enum):
 	NEPTUNE_USERSET_DEFAULT		= 0
 	NEPTUNE_USERSET_1			= 1
 	NEPTUNE_USERSET_2			= 2
 	NEPTUNE_USERSET_3			= 3
 	NEPTUNE_USERSET_4			= 4
 	NEPTUNE_USERSET_5			= 5
 	NEPTUNE_USERSET_6			= 6
 	NEPTUNE_USERSET_7			= 7
 	NEPTUNE_USERSET_8			= 8
 	NEPTUNE_USERSET_9			= 9
 	NEPTUNE_USERSET_10			= 10
 	NEPTUNE_USERSET_11			= 11
 	NEPTUNE_USERSET_12			= 12
 	NEPTUNE_USERSET_13			= 13
 	NEPTUNE_USERSET_14			= 14
 	NEPTUNE_USERSET_15			= 15
##########################################################################
class ENeptuneUserSetCommand(Enum):
 	NEPTUNE_USERSET_CMD_LOAD	= 0
 	NEPTUNE_USERSET_CMD_SAVE	= 1
##########################################################################
class ENeptuneAutoIrisMode(Enum):
 	NEPTUNE_AUTOIRIS_MODE_MANUAL = 0
 	NEPTUNE_AUTOIRIS_MODE_AUTO	 = 1
##########################################################################
class ENeptuneSIOParity(Enum):
 	NEPTUNE_SIO_PARITY_NONE		= 0
 	NEPTUNE_SIO_PARITY_ODD		= 1
 	NEPTUNE_SIO_PARITY_EVEN		= 2
##########################################################################
class ENeptuneAutoAreaSelect(Enum):
 	NEPTUNE_AUTOAREA_SELECT_AE		= 0 	# for AutoExposure
 	NEPTUNE_AUTOAREA_SELECT_AWB		= 1 	# for AutoWhiteBalance
 	NEPTUNE_AUTOAREA_SELECT_AF		= 2		# for AutoFocus
##########################################################################
class ENeptuneAutoAreaSize(Enum):
 	NEPTUNE_AUTOAREA_SIZE_SELECTED	= 0 	# selected size
 	NEPTUNE_AUTOAREA_SIZE_FULL		= 1		# full image size
##########################################################################
class ENeptuneAFMode(Enum):
 	NEPTUNE_AF_ORIGIN			= 0 		# set focus to origin point
 	NEPTUNE_AF_ONEPUSH			= 1 		# one-push auto focus
 	NEPTUNE_AF_STEP_FORWARD		= 2 		# move one step forward
 	NEPTUNE_AF_STEP_BACKWARD	= 3			# move one step backward
##########################################################################
class ENeptuneTriggerSource(Enum):
 	NEPTUNE_TRIGGER_SOURCE_LINE1	= 0 	# external(H/W trigger)
 	NEPTUNE_TRIGGER_SOURCE_SW		= 7		# software trigger
##########################################################################
class ENeptuneTriggerMode(Enum):
 	NEPTUNE_TRIGGER_MODE_0     = 0    		# trigger mode 0
 	NEPTUNE_TRIGGER_MODE_1     = 1			# trigger mode 1
 	NEPTUNE_TRIGGER_MODE_2     = 2			# trigger mode 2
 	NEPTUNE_TRIGGER_MODE_3     = 3			# trigger mode 3
 	NEPTUNE_TRIGGER_MODE_4     = 4			# trigger mode 4
 	NEPTUNE_TRIGGER_MODE_5     = 5			# trigger mode 5
 	NEPTUNE_TRIGGER_MODE_6     = 6			# trigger mode 6
 	NEPTUNE_TRIGGER_MODE_7     = 7			# trigger mode 7
 	NEPTUNE_TRIGGER_MODE_8     = 8			# trigger mode 8
 	NEPTUNE_TRIGGER_MODE_9     = 9			# trigger mode 9
 	NEPTUNE_TRIGGER_MODE_10    = 10 		# trigger mode 10
 	NEPTUNE_TRIGGER_MODE_11    = 11 		# trigger mode 11
 	NEPTUNE_TRIGGER_MODE_12    = 12 		# trigger mode 12
 	NEPTUNE_TRIGGER_MODE_13    = 13 		# trigger mode 13
 	NEPTUNE_TRIGGER_MODE_14    = 14 		# trigger mode 14
 	NEPTUNE_TRIGGER_MODE_15    = 15 		# trigger mode 15
##########################################################################
class ENeptuneStrobe(Enum):
 	NEPTUNE_STROBE0			= 0
 	NEPTUNE_STROBE1			= 1
 	NEPTUNE_STROBE2			= 2
 	NEPTUNE_STROBE3			= 3
 	NEPTUNE_STROBE4			= 4
##########################################################################
class ENeptunePolarity(Enum):
 	NEPTUNE_POLARITY_RISINGEDGE		= 0 	# rising edge
 	NEPTUNE_POLARITY_FALLINGEDGE	= 1 	# falling edge
 	NEPTUNE_POLARITY_ANYEDGE		= 2 	# any edge
 	NEPTUNE_POLARITY_LEVELHIGH		= 3 	# high level
 	NEPTUNE_POLARITY_LEVELLOW		= 4		# low level
##########################################################################
class ENeptuneNodeType(Enum):
 	NEPTUNE_NODE_TYPE_UKNOWN		= -1
 	NEPTUNE_NODE_TYPE_CATEGORY		= 0
 	NEPTUNE_NODE_TYPE_COMMAND       = 1 	# command type node
 	NEPTUNE_NODE_TYPE_RAW           = 2 	# raw node
 	NEPTUNE_NODE_TYPE_STRING        = 3 	# string node
 	NEPTUNE_NODE_TYPE_ENUM          = 4 	# enumeration node
 	NEPTUNE_NODE_TYPE_INT           = 5 	# int type node
 	NEPTUNE_NODE_TYPE_FLOAT         = 6 	# float type node
 	NEPTUNE_NODE_TYPE_BOOLEAN       = 7		# boolean type node
##########################################################################
class ENeptuneNodeAccessMode(Enum):
 	NEPTUNE_NODE_ACCESSMODE_NI			= 0 		# Not Implemented
 	NEPTUNE_NODE_ACCESSMODE_NA			= 1 		# Not Available
 	NEPTUNE_NODE_ACCESSMODE_WO			= 2 		# Write Only
 	NEPTUNE_NODE_ACCESSMODE_RO			= 3 		# Read Only
 	NEPTUNE_NODE_ACCESSMODE_RW			= 4 		# Read, Write
 	NEPTUNE_NODE_ACCESSMODE_UNDEFINED	= 5			# undefined
##########################################################################
class ENeptuneNodeVisibility(Enum):
 	NEPTUNE_NODE_VISIBLE_UNKNOWN		= -1
 	NEPTUNE_NODE_VISIBLE_BEGINNER		= 0 		# beginner
 	NEPTUNE_NODE_VISIBLE_EXPERT			= 1 		# expert
 	NEPTUNE_NODE_VISIBLE_GURU			= 2			# guru
##########################################################################
class ENeptuneGPIO(Enum):
 	NEPTUNE_GPIO_LINE0 = 0		# GPIO 0
 	NEPTUNE_GPIO_LINE1 = 1		# GPIO 1
##########################################################################
class ENeptuneGPIOSource(Enum):
 	NEPTUNE_GPIO_SOURCE_STROBE = 0	# strobe
 	NEPTUNE_GPIO_SOURCE_USER   = 1	# user defined
##########################################################################
class ENeptuneGPIOValue(Enum):
 	NEPTUNE_GPIO_VALUE_LOW   = 0		    # low level
 	NEPTUNE_GPIO_VALUE_HIGH  = 1			# high level
##########################################################################
class ENeptuneStopRecordNotify(Enum):
 	NEPTUNE_STOP_RECORD_UNKNOWN		= -1	# Unknown
 	NEPTUNE_STOP_RECORD_COMPLETE	= 0 	# Complete
 	NEPTUNE_STOP_RECORD_MANUAL		= 1 	# Manual stop
 	NEPTUNE_STOP_RECORD_CODEC_ERR	= 2 	# Codec error
 	NEPTUNE_STOP_RECORD_TIMEOUT		= 3 	# Time out (No images to process)
 	NEPTUNE_STOP_RECORD_BUFFER_FULL	= 4		# Buffer full


"""
STRUCT_DEFINE

"""
class NEPTUNE_CAM_INFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("strVendor",      ctypes.c_char*128),
                ("emDevType",      ctypes.c_int32),    # ENeptuneDevType
                ("szReserved",     ctypes.c_char*380),
                ("strModel",       ctypes.c_char*MAX_STRING_LENGTH),
                ("strSerial",      ctypes.c_char*MAX_STRING_LENGTH),
                ("strUserID",      ctypes.c_char*MAX_STRING_LENGTH),
                ("strIP",          ctypes.c_char*MAX_STRING_LENGTH),
                ("strMAC",         ctypes.c_char*MAC_LENGTH),
                ("strSubnet",      ctypes.c_char*MAX_STRING_LENGTH),
                ("strGateway",     ctypes.c_char*MAX_STRING_LENGTH),
                ("strCamID",       ctypes.c_char*MAX_STRING_LENGTH)]
##########################################################################
class NEPTUNE_IMAGE_SIZE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("nStartX",        ctypes.c_int32),	# start point of X coordinate(width direction)
 	            ("nStartY",        ctypes.c_int32),	# start point of Y coordinate(height direction)
 	            ("nSizeX",         ctypes.c_int32), # width 
 	            ("nSizeY",         ctypes.c_int32)]	# height
    
    def __init__(self) :
        self.nStartX        = 0
        self.nStartY        = 0
        self.nSizeX         = 0
        self.nSizeY         = 0
##########################################################################
class NEPTUNE_IMAGE(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("uiWidth",       ctypes.c_uint32),	                  # image data width
 	            ("uiHeight",      ctypes.c_uint32),                   # image data height
 	            ("uiBitDepth",    ctypes.c_uint32),                   # data bits per pixel
                ("pData",         ctypes.POINTER(ctypes.c_char)),    # image buffer #15040512
 	            ("uiSize",        ctypes.c_uint32),                   # buffer length
                ("uiIndex",       ctypes.c_uint32),	                  # buffer index
 	            ("uiTimestamp",   ctypes.c_int64),                    # data timestamp
 	            ("bFrameValid",   ctypes.c_uint8)]	                  # flag for frame state : 1(Valid), 0(Invalid)
    
    def __init__(self) :
        self.uiWidth            = 0
        self.uiHeight           = 0
        self.uiBitDepth         = 0
        self.uiSize             = 0
        self.uiIndex            = 0
        self.uiTimestamp        = 0
        self.bFrameValid        = 1
        #self.nSize 				= 2048 * 2448 *3
        #self.buffer = (ctypes.c_byte*self.nSize)()
        #self.buffer_p = ctypes.pointer(self.buffer)
        #self.pData = ctypes.cast(self.buffer_p,ctypes.POINTER(ctypes.c_ubyte*15040512))
        self.pData = None
##########################################################################
class NEPTUNE_IMAGE_EX(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("stImage",                NEPTUNE_IMAGE),
 	            ("ulBlockID",              ctypes.c_uint32),
 	            ("uExternalTriggerCount",  ctypes.c_uint8),
 	            ("uTmode15TriggerCount",   ctypes.c_uint8)]
##########################################################################
class NEPTUNE_FEATURE(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("bSupport",          ctypes.c_int32), #ENeptuneBoolean 
 	            ("bOnOff",            ctypes.c_int32), #ENeptuneBoolean	        # on/off state, on/off control(SnowNoiseRemove only)
 	            ("SupportAutoModes",  ctypes.c_uint8),	                        # bit flag for support(bit0:Off, bit1:Once, bit2:Continuous)
 	            ("AutoMode",          ctypes.c_int32), #ENeptuneAutoMode        # current Auto mode, valid only when "SuporeAutoMode != 0"
 	            ("Min",               ctypes.c_int32),                         # minimum value
 	            ("Max",               ctypes.c_int32),                         # maximum value
 	            ("Inc",               ctypes.c_int32),                         # increment step
 	            ("Value",             ctypes.c_int32),                         # current value
 	            ("ValueAccessMode",   ctypes.c_int32)] # ENeptuneNodeAccessMode # access state of the value		

    def __init__(self) :
        self.bOnOff              = ENeptuneBoolean.NEPTUNE_BOOL_TRUE.value
        self.bSupport            = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
        self.SupportAutoModes    = 0
        self.AutoMode            = ENeptuneAutoMode.NEPTUNE_AUTO_OFF.value
        self.Min                 = 0 	                        
        self.Max                 = 0	                    	
        self.Inc                 = 0		                    
        self.Value               = 0		                    
        self.ValueAccessMode     = ENeptuneNodeAccessMode.NEPTUNE_NODE_ACCESSMODE_NA.value
##########################################################################
class NEPTUNE_PACKAGE_FEATURE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("Gain",          ctypes.c_uint32),
 	            ("Sharpness",     ctypes.c_uint32),
 	            ("Shutter",       ctypes.c_uint32),
 	            ("BlackLevel",    ctypes.c_uint32),
 	            ("Contrast",      ctypes.c_uint32),
 	            ("Gamma",         ctypes.c_uint32)]
##########################################################################
class NEPTUNE_USERSET(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("SupportUserSet",   ctypes.c_uint16),                          # bit flag for supported user set, 0 is "Default"
 	            ("UserSetIndex",     ctypes.c_int32), # ENeptuneUserSet 	    # user set index to save or load
 	            ("Command",          ctypes.c_int32)] # ENeptuneUserSetCommand  # save or load

    def __init__(self):
        self.SupportUserSet     = 0;
        self.UserSetIndex       = ENeptuneUserSet.NEPTUNE_USERSET_DEFAULT.value
        self.Command            = ENeptuneUserSetCommand.NEPTUNE_USERSET_CMD_LOAD.value
##########################################################################
class NEPTUNE_POINT(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("x",   ctypes.c_uint32),  # x-coordinate
 	            ("y",   ctypes.c_uint32)]  # y-coordinate
                
    def __init__(self):
        self.x = 0
        self.y = 0
##########################################################################
class NEPTUNE_KNEE_LUT(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("Points",   NEPTUNE_POINT*KNEE_POINT_TABLE_SIZE),    # 4 points
 	            ("bEnable",  ctypes.c_int32)] # ENeptuneBoolean # enable/disable state/control
    
    def __init__(self):
        self.bEnable = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
        ctypes.memset(self.Points, 0, ctypes.sizeof(NEPTUNE_POINT)*KNEE_POINT_TABLE_SIZE)
##########################################################################
class NEPTUNE_USER_LUT(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("SupportLUT",                  ctypes.c_uint16),					  # bit Flag
 	            ("LUTIndex",                    ctypes.c_uint16), 					  # current LUT index
 	            ("bEnable",                     ctypes.c_int32),   # ENeptuneBoolean  # enable/disable state/control
 	            ("Data",                        ctypes.POINTER(ctypes.c_uint16)*USER_LUT_TABLE_SIZE)]	                  # LUT data, valid only in Set function
    
    def __init__(self):
     	self.SupportLUT    = 0
     	self.LUTIndex      = 0
     	self.bEnable       = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	ctypes.memset(self.Data, 0, ctypes.sizeof(ctypes.c_uint16)*USER_LUT_TABLE_SIZE)
##########################################################################
class NEPTUNE_SIO_PROPERTY(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("bEnable",       ctypes.c_int32),  # ENeptuneBoolean   # RS232 enable
 	            ("Baudrate",      ctypes.c_uint32),	                     # serial baudrate
 	            ("Parity",        ctypes.c_int32),   # ENeptuneSIOParity # parity bit
 	            ("DataBit",       ctypes.c_uint32),	                     # data bit
 	            ("StopBit",       ctypes.c_uint32)]	                     # stop bit
    
    def __init__(self):
     	self.bEnable       = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	self.Baudrate      = 9600
     	self.Parity        = ENeptuneSIOParity.NEPTUNE_SIO_PARITY_NONE.value
     	self.DataBit       = 8
     	self.StopBit       = 1
##########################################################################
class NEPTUNE_SIO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("TextCount",     ctypes.c_uint32),					  # bit Flag
 	            ("strText",       ctypes.POINTER(ctypes.c_char)*256),
 	            ("TimeOut",       ctypes.c_uint32)]
    
    def __init__(self):
        self.TexttCount = 0
        ctypes.memset(self.strText, 0, ctypes.sizeof(ctypes.c_char*256)) 
        self.TimeOut    = 100
##########################################################################
class NEPTUNE_AUTOAREA(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("OnOff",          ctypes.c_int32),	     # ENeptuneBoolean
 	            ("SizeControl",    ctypes.c_int32),      # ENeptuneAutoAreaSize
 	            ("AreaSize",       NEPTUNE_IMAGE_SIZE)]
    
    def __init__(self):
     	self.OnOff         = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	self.SizeControl   = ENeptuneAutoAreaSize.NEPTUNE_AUTOAREA_SIZE_FULL.value
     	ctypes.memset(self.AreaSize, 0, ctypes.sizeof(NEPTUNE_IMAGE_SIZE))
##########################################################################
class NEPTUNE_TRIGGER_INFO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("bSupport",         ctypes.c_int32),   # ENeptuneBoolean # trigger support flag
 	            ("nModeFlag",        ctypes.c_uint16),# bit mask for trigger mode
 	            ("nSourceFlag",      ctypes.c_uint16),# bit mask for trigger source (bit0 = H/W, bit7 = S/W)
 	            ("nPolarityFlag",    ctypes.c_uint16),# bit mask for polarity
 	            ("nParamMin",        ctypes.c_uint16),# trigger parameter minimum value
 	            ("nParamMax",        ctypes.c_uint16)]# trigger parameter maximum value
    
    def __init__(self):
     	self.bSupport          = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	self.nModeFlag         = 0
     	self.nSourceFlag       = 0
     	self.nPolarityFlag     = 0
     	self.nParamMin         = 0
     	self.nParamMax         = 0
##########################################################################
class NEPTUNE_TRIGGER(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("Source",      ctypes.c_int32),  # ENeptuneTriggerSource  # trigger source value
 	            ("Mode",        ctypes.c_int32),  # ptuneTriggerMode       # trigger mode value
 	            ("Polarity",    ctypes.c_int32),  # ENeptunePolarity       # trigger polarity value
 	            ("OnOff",       ctypes.c_int32),  # ENeptuneBoolean        # trigger on/off
 	            ("nParam",      ctypes.c_uint16)]                           # trigger parameter
    
    def __init__(self):
     	self.OnOff         = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	self.Mode          = ENeptuneTriggerMode.NEPTUNE_TRIGGER_MODE_0.value
     	self.Source        = ENeptuneTriggerSource.NEPTUNE_TRIGGER_SOURCE_LINE1.value
     	self.Polarity      = ENeptunePolarity.NEPTUNE_POLARITY_FALLINGEDGE.value
     	self.nParam        = 0;

##########################################################################
class NEPTUNE_TRIGGER_PARAM(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("nFrameOrder",         ctypes.c_uint32), # frame sequence number
 	            ("nIncrement",          ctypes.c_uint32), # end of table(0) or continuous(1)
 	            ("nGainValue",          ctypes.c_uint32), # gain feature value
 	            ("nShutterValue",       ctypes.c_uint32)] # shutter feature value
    
    def __init__(self):
     	self.nShutterValue     = 0
     	self.nGainValue        = 0
     	self.nIncrement        = 0
     	self.nFrameOrder       = 0
##########################################################################
class NEPTUNE_TRIGGER_TABLE(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("Param",     NEPTUNE_TRIGGER_PARAM*MAX_TRIGGER_PARAM),  # trigger parameter : max 255
 	            ("Index",     ctypes.c_uint32)]        # 0 ~ 15               
    
    def __init__(self):
     	self.Index = 0;
     	ctypes.memset(self.Param, 0, ctypes.sizeof(NEPTUNE_TRIGGER_PARAM)*MAX_TRIGGER_PARAM);

##########################################################################
class NEPTUNE_STROBE_INFO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("bSupport",        ctypes.c_int32), # ENeptuneBoolean # support of strobe
 	            ("nStrobeFlag",     ctypes.c_uint16),                  # support strobes bit flag
 	            ("nPolarityFlag",   ctypes.c_uint16),                  # strobe polarity support bit flag
 	            ("nDurationMin",    ctypes.c_uint16),                  # strobe duration minimum value
 	            ("nDurationMax",    ctypes.c_uint16),                  # strobe duration maximum value
 	            ("nDelayMin",       ctypes.c_uint16),                  # strobe delay minimum value
 	            ("nDelayMax",       ctypes.c_uint16)]                  # strobe delay maximum value   
     	
    def __init__(self):
     	self.bSupport          = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	self.nStrobeFlag       = 0
     	self.nDurationMin      = 0
     	self.nDurationMax      = 0
     	self.nDelayMin         = 0
     	self.nDelayMax         = 0
     	self.nPolarityFlag     = 0
    
##########################################################################
class NEPTUNE_STROBE(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("OnOff",      ctypes.c_int32), # ENeptuneBoolean  # strobe on/off control
 	            ("Strobe",     ctypes.c_int32), # ENeptuneStrobe   # strobe index
 	            ("nDuration",  ctypes.c_uint16),                   # strobe duration value
 	            ("nDelay",     ctypes.c_uint16),# strobe delay value
 	            ("Polarity",   ctypes.c_int32)] # ENeptunePolarity  # strobe polarity      
    
    def __init__(self):
     	self.OnOff     = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	self.Strobe    = ENeptuneStrobe.NEPTUNE_STROBE1.value
     	self.nDuration = 0
     	self.nDelay    = 0
     	self.Polarity  = ENeptunePolarity.NEPTUNE_POLARITY_LEVELHIGH.value
##########################################################################
class NEPTUNE_XML_NODE_LIST(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("nCount",       ctypes.c_uint32),
 	            ("pstrList",     ctypes.POINTER(ctypes.c_char)*MAX_NODE_LIST_COUNT*MAX_XML_NODE_STRING_LENGTH)]
    
    def __init__(self):
     	self.nCount = MAX_NODE_LIST_COUNT
     	ctypes.memset(self.pstrList, 0, ctypes.sizeof(ctypes.c_char)*MAX_NODE_LIST_COUNT*MAX_XML_NODE_STRING_LENGTH)
##########################################################################
class NEPTUNE_XML_ENUM_LIST(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("nCount",       ctypes.c_uint32),  # number of enumeration node string
 	            ("pstrList",     ctypes.POINTER(ctypes.c_char)*MAX_ENUM_LIST_COUNT*MAX_XML_NODE_STRING_LENGTH),    # enumeration node string list
 	            ("nIndex",       ctypes.c_uint32)]  # current index of the string list		
 	
    def __init__(self):
     	self.nCount    = MAX_ENUM_LIST_COUNT;
     	self.nIndex    = 0;
     	ctypes.memset(self.pstrList, 0, ctypes.sizeof(ctypes.c_char)*MAX_ENUM_LIST_COUNT*MAX_XML_NODE_STRING_LENGTH);
##########################################################################
class NEPTUNE_XML_NODE_INFO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("Type",               ctypes.c_int32),       # ENeptuneNodeType       # node type(int, float, boolean, string, enumeration, command)
 	            ("AccessMode",         ctypes.c_int32),   # ENeptuneNodeAccessMode # access mode
 	            ("Visibility",         ctypes.c_int32),   # ENeptuneNodeVisibility # node visibility
 	            ("bHasChild",          ctypes.c_int8),     # ENeptuneBoolean        # has child ?
 	            ("strDisplayName",     ctypes.POINTER(ctypes.c_char)*MAX_STRING_LENGTH),                         # node name
 	            ("strTooltip",         ctypes.POINTER(ctypes.c_char)*MAX_STRING_LENGTH),                             # node tooltip
 	            ("strDescription",     ctypes.POINTER(ctypes.c_char)*MAX_STRING_LENGTH)]                         # node description         

    def __init__(self):
     	self.Type          = ENeptuneNodeType.NEPTUNE_NODE_TYPE_UKNOWN.value
     	self.AccessMode    = ENeptuneNodeAccessMode.NEPTUNE_NODE_ACCESSMODE_UNDEFINED.value
     	self.Visibility    = ENeptuneNodeVisibility.NEPTUNE_NODE_VISIBLE_UNKNOWN.value
     	self.bHasChild     = ENeptuneBoolean.NEPTUNE_BOOL_FALSE.value
     	ctypes.memset(self.strDisplayName, 0, ctypes.sizeof(ctypes.c_char)*MAX_STRING_LENGTH)
     	ctypes.memset(self.strTooltip, 0, ctypes.sizeof(ctypes.c_char)*MAX_STRING_LENGTH)
     	ctypes.memset(self.strDescription, 0, ctypes.sizeof(ctypes.c_char)*MAX_STRING_LENGTH)
##########################################################################
class NEPTUNE_XML_INT_VALUE_INFO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("nValue",         ctypes.c_int64),                          # current value
 	            ("nMin",           ctypes.c_int64),                          # minimum value supported
 	            ("nMax",           ctypes.c_int64),                          # maximum value supported
 	            ("nInc",           ctypes.c_int64),                          # increment step
 	            ("AccessMode",     ctypes.c_int32)] # ENeptuneNodeAccessMode # access mode         	

    def __init__(self):
     	self.nValue        = 0
     	self.nMin          = 0
     	self.nMax          = 0
     	self.nInc          = 0
     	self.AccessMode    = ENeptuneNodeAccessMode.NEPTUNE_NODE_ACCESSMODE_UNDEFINED.value
##########################################################################
class NEPTUNE_XML_FLOAT_VALUE_INFO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("dValue",         ctypes.c_double),                          # current value
 	            ("dMin",           ctypes.c_double),                          # minimum
 	            ("dMax",           ctypes.c_double),                          # maximum
 	            ("dInc",           ctypes.c_double),                          # increment
 	            ("AccessMode",     ctypes.c_int32)] # ENeptuneNodeAccessMode  # access mode


    def __init__(self):
     	self.dValue        = 0
     	self.dMin          = 0
     	self.dMax          = 0
     	self.dInc          = 0.001
     	self.AccessMode    = ENeptuneNodeAccessMode.NEPTUNE_NODE_ACCESSMODE_UNDEFINED.value
##########################################################################
class NEPTUNE_GPIO(ctypes.Structure) :
    _pack_ = 1
    _fields_ = [("Gpio",     ctypes.c_int32),   # ENeptuneGPIO          # GPIO index
 	            ("Source",   ctypes.c_int32),   # ENeptuneGPIOSource    # GPIO source
 	            ("Value",    ctypes.c_int32)]   # ENeptuneGPIOValue     # GPIO value

    def __init__(self):
     	self.Gpio          = ENeptuneGPIO.NEPTUNE_GPIO_LINE1.value
     	self.Source        = ENeptuneGPIOSource.NEPTUNE_GPIO_SOURCE_STROBE.value
     	self.Value         = ENeptuneGPIOValue.NEPTUNE_GPIO_VALUE_LOW.value
##########################################################################
try:
	Neptune_dll = ctypes.windll.LoadLibrary(str(Path(__file__).parent/"NeptuneC_MD_VC141.dll"))
except:
	Neptune_dll = ctypes.windll.LoadLibrary("C:/Program Files/IMI Tech/Neptune/Runtime/x64/NeptuneC_MD_VC141.dll")
##########################################################################




"""
FUNCTION_DEFINE

"""


"""  
 	Description :
		initialize NeptuneC library
 	Parameters :
		None
"""
def ntcInit():
    Neptune_Error = Neptune_dll.ntcInit()
    return Neptune_Error
##########################################################################
"""
 	Description :
		clear NeptuneC library
 	Parameters :
		None
        
"""
def ntcUninit():
    Neptune_Error = Neptune_dll.ntcUninit()
    return Neptune_Error
##########################################################################
"""
 	Description :
		get number of cameras connected to the system
 	Parameters :
		[OUT] puiCount : number of cameras
        
"""
def ntcGetCameraCount(puiCount):

    Neptune_dll.ntcGetCameraCount.argtypes = [ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetCameraCount(puiCount)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of connected cameras
 	Parameters :
		[OUT] ctypes.POINTER(NEPTUNE_CAM_INFO) : camera information
		[IN] uiCount : number of NEPTUNE_CAM_INFO structure
"""  
def ntcGetCameraInfo(pInfo, nLength):

    Neptune_dll.ntcGetCameraInfo.argtypes = [ctypes.POINTER(NEPTUNE_CAM_INFO), ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGetCameraInfo(pInfo,nLength)
    return Neptune_Error
##########################################################################
"""
 	Description :
		create camera handle to control. All other function needs camera handle
 	Parameters :
		[IN] pszCameraID : strCamID of camera info
		[OUT] pCameraHandle : created camera handle 
		[IN] emAccessFlag : camera control level

"""
def ntcOpen(pstrDevID,phCamHandle,eAccessFlag = ENeptuneDevAccess.NEPTUNE_DEV_ACCESS_EXCLUSIVE.value ):
    p_CamID = ctypes.c_char_p(pstrDevID)
    Neptune_dll.ntcOpen.argtypes = [ctypes.c_char_p,ctypes.c_void_p,ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcOpen(pstrDevID,phCamHandle,eAccessFlag)
    
    return Neptune_Error
##########################################################################
"""
 	Description :
		delete camera handle
 	Parameters :
		[IN] hCameraHandle : camera handle to delete

"""
def ntcClose(hCameraHandle):
    Neptune_dll.ntcClose.argtypes = [ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcClose(hCameraHandle)
    return Neptune_Error
##########################################################################    
"""
 	Description :
		get the type(1394 or GigE) of camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemDevType : camera type
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetCameraType(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneDevType* pemDevType);
def ntcGetCameraType(hCameraHandle, pemDevType):
    Neptune_dll.ntcGetCameraType.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetCameraType(hCameraHandle, pemDevType)
    return Neptune_Error
##########################################################################

"""
	Description :
		get the list of pixel format supported by a camera. 
		The size of supported pixel format is returned when called ntcGetPixelFormatList(hCameraHandle, NULL, &nSize).
	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemPixelFmtList : list of pixel format
		[IN/OUT] puiCount : size of the list
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetPixelFormatList(IN NeptuneCamHandle hCameraHandle, OUT ENeptunePixelFormat* pemPixelFmtList, IN OUT _uint32_t* puiCount);
def ntcGetPixelFormatList(hCameraHandle, pemPixelFmtList, puiCount):
    Neptune_dll.ntcGetPixelFormatList.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetPixelFormatList(hCameraHandle, pemPixelFmtList, puiCount)
    return Neptune_Error

##########################################################################
"""
 	Description :
		get the current pixel format of a camera as a string
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emPixelFmt : current pixel format enumeration value
		[OUT] pszBuffer : pixel format string value
		[IN] uiBufSize : size of the string
        
"""    
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetPixelFormatString(IN NeptuneCamHandle hCameraHandle, IN ENeptunePixelFormat emPixelFmt, OUT _char_t* pszBuffer, IN _uint32_t uiBufSize);
def ntcGetPixelFormatString(hCameraHandle, emPixelFmt, pszBuffer,uiBufSize):
    Neptune_dll.ntcGetPixelFormatString.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGetPixelFormatString(hCameraHandle, emPixelFmt, pszBuffer, uiBufSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the current pixel format of a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemPixelFmt : current pixel format value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetPixelFormat(IN NeptuneCamHandle hCameraHandle, OUT ENeptunePixelFormat* pemPixelFmt);
def ntcGetPixelFormat (hCameraHandle, pemPixelFmt):
    Neptune_dll.ntcGetPixelFormat.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetPixelFormat(hCameraHandle, pemPixelFmt)
    return Neptune_Error


##########################################################################
"""
 	Description :
		set pixel format to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emPixelFmt : pixel format to set to a camera
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetPixelFormat(IN NeptuneCamHandle hCameraHandle, IN ENeptunePixelFormat emPixelFmt);	
def ntcSetPixelFormat(hCameraHandle, emPixelFmt):
    Neptune_dll.ntcSetPixelFormat.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetPixelFormat(hCameraHandle, ctypes.c_int32(emPixelFmt))
    return Neptune_Error
##########################################################################
"""
 	Description :
		get frame rate list supported by a camera.
		The size of supported pixel format is returned when called ntcGetFrameRateList(hCameraHandle, NULL, &nSize).
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemFPSList : list of frame rate supported by a camera
		[IN/OUT] puiCount : size of the list
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetFrameRateList(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneFrameRate* pemFPSList, IN OUT _uint32_t* puiCount);
def ntcGetFrameRateList(hCameraHandle, pemFPSList, puiCount):
    Neptune_dll.ntcGetFrameRateList.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetFrameRateList(hCameraHandle, pemFPSList, puiCount)
    return Neptune_Error

##########################################################################
"""
 	Description :
		get frame rate value as a string
 	Parameters :
		[IN] hCamHanle : camera handle to control
		[IN] emFPS : frame rate enumeration value
		[OUT] pszBuffer : frame rate string value converted
		[IN] uiBufSize ; size of the string
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetFrameRateString(IN NeptuneCamHandle hCameraHandle, IN ENeptuneFrameRate emFPS, OUT _char_t* pszBuffer, IN _uint32_t uiBufSize);
def ntcGetFrameRateString(hCameraHandle, emFPS, pszBuffer, uiBufSize):
    Neptune_dll.ntcGetFrameRateString.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.c_char_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGetFrameRateString(hCameraHandle, emFPS, pszBuffer, uiBufSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get current frame rate enumeration value of a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemFPS : current frame rate value
		[OUT] pdbFPS : valid float value if the peRate is "FPS_VALUE" for GigE camera
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetFrameRate(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneFrameRate* pemFPS, OUT _double_t* pdbFPS);
def ntcGetFrameRate(hCameraHandle, pemFPS, pdbFPS):
    Neptune_dll.ntcGetFrameRate.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double)]
    Neptune_Error = Neptune_dll.ntcGetFrameRate(hCameraHandle, pemFPS, pdbFPS)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set frame rate to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emFPS : frame rate to set to a camera
		[IN] dbFPS : frame rate float value valid only if eRate is "FPS_VALUE" for GigE camera
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetFrameRate(IN NeptuneCamHandle hCameraHandle, IN ENeptuneFrameRate emFPS, IN _double_t dbFPS);
def ntcSetFrameRate(hCameraHandle, emFPS, dbFPS):
    Neptune_dll.ntcSetFrameRate.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.c_double]
    Neptune_Error = Neptune_dll.ntcSetFrameRate(hCameraHandle, emFPS, dbFPS)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the real image data transfer rate
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pfRecvFPS : receive frame rate
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetReceiveFrameRate(IN NeptuneCamHandle hCameraHandle, OUT _float32_t* pfRecvFPS);
def ntcGetReceiveFrameRate(hCameraHandle, pfRecvFPS):
    Neptune_dll.ntcGetReceiveFrameRate.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float)]
    Neptune_Error = Neptune_dll.ntcGetReceiveFrameRate(hCameraHandle, pfRecvFPS)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the maximum image size of the assigned pixel format
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pImageSize : max image size information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetMaxImageSize(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_IMAGE_SIZE pImageSize);
def ntcGetMaxImageSize(hCameraHandle, pImageSize):
    Neptune_dll.ntcGetMaxImageSize.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_IMAGE_SIZE)]
    Neptune_Error = Neptune_dll.ntcGetMaxImageSize(hCameraHandle, pImageSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the current size information of an image
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pImageSize : image size information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetImageSize(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_IMAGE_SIZE pImageSize);
def ntcGetImageSize(phCamHandle,pImageSize):
    Neptune_dll.ntcGetImageSize.argtypes = [ctypes.c_void_p,ctypes.POINTER(NEPTUNE_IMAGE_SIZE)]
    Neptune_Error = Neptune_dll.ntcGetImageSize(phCamHandle,pImageSize) 
    return Neptune_Error
##########################################################################
"""
 	Description :
		set the image size. 
		Valid only if pixel format is Format7 for 1394 camera or GigE camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stImageSize : image size information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetImageSize(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_IMAGE_SIZE stImageSize);
def ntcSetImageSize(hCameraHandle, stImageSize):
    Neptune_dll.ntcSetImageSize.argtypes = [ctypes.c_void_p, NEPTUNE_IMAGE_SIZE]
    Neptune_Error = Neptune_dll.ntcSetImageSize(hCameraHandle, stImageSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get current play status
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemState : play/stop state
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAcquisition(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBoolean* pemState);
def ntcGetAcquisition(hCameraHandle, pemState):
    Neptune_dll.ntcGetAcquisition.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetAcquisition(hCameraHandle, pemState)
    return Neptune_Error ,pemState
##########################################################################
"""
 	Description :
		set camera play or stop
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emState : play/stop controlf
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAcquisition(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emState);
def ntcSetAcquisition(hCameraHandle, emState):
    Neptune_dll.ntcSetAcquisition.argtypes = [ctypes.c_void_p,ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetAcquisition(hCameraHandle, emState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the current acquisition mode of a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pemAcqMode : current acquisition mode
		[OUT] puiFrames : frame number(valid only if the peMode = NEPTUNE_ACQ_MULTIFRAME)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAcquisitionMode(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneAcquisitionMode* pemAcqMode, OUT _uint32_t* puiFrames);
def ntcGetAcquisitionMode(hCameraHandle, pemAcqMode, puiFrames):
    Neptune_dll.ntcGetAcquisitionMode.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetAcquisitionMode(hCameraHandle, pemAcqMode, puiFrames)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set the acquisition mode to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emAcqMode : acquisition mode
		[IN] uiFrames : multi frame image count(valid only if the eMode = NEPTUNE_ACQ_MULTIFRAME)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAcquisitionMode(IN NeptuneCamHandle hCameraHandle, IN ENeptuneAcquisitionMode emAcqMode, IN _uint32_t uiFrames = 2);

def ntcSetAcquisitionMode(hCameraHandle, emAcqMode, uiFrames = 2):
    Neptune_dll.ntcSetAcquisitionMode.argtypes = [ctypes.c_void_p,ctypes.c_int32, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetAcquisitionMode(hCameraHandle, emAcqMode, uiFrames)
    return Neptune_Error
##########################################################################
"""
 	Description :
		control camera to transfer a single image frame.
		Acquisition mode should be set as NEPTUNE_ACQ_SINGLEFRAME
 	Parameters :
		[IN] hCameraHandle : camera handle to control
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcOneShot(IN NeptuneCamHandle hCameraHandle);
def ntcOneShot(hCameraHandle):
    Neptune_dll.ntcOneShot.argtypes = [ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcOneShot(hCameraHandle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		control camera to transfer multiple image frames.
		Acquisition mode should be set as NEPTUNE_ACQ_MULTIFRAME
 	Parameters :
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcMultiShot(IN NeptuneCamHandle hCameraHandle);
def ntcMultiShot(hCameraHandle):
    Neptune_dll.ntcMultiShot.argtypes = [ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcMultiShot(hCameraHandle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get current bayer conversion information
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemMethod : bayer convert information(None or conversion method)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetBayerConvert(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBayerMethod* pemMethod);
def ntcGetBayerConvert(hCameraHandle, pemMethod):
    Neptune_dll.ntcGetBayerConvert.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetBayerConvert(hCameraHandle, pemMethod)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set bayer convert control
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emMethod : bayer convert information(None or conversion method)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetBayerConvert(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBayerMethod emMethod);
def ntcSetBayerConvert(hCameraHandle, emMethod):
    Neptune_dll.ntcSetBayerConvert.argtypes = [ctypes.c_void_p,ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetBayerConvert(hCameraHandle, emMethod)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get bayer pattern layout information
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemLayout : bayer pattern layout
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetBayerLayout(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBayerLayout* pemLayout);
def ntcGetBayerLayout(hCameraHandle, pemLayout):
    Neptune_dll.ntcGetBayerLayout.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetBayerLayout(hCameraHandle, pemLayout)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set bayer patter layout control
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emLayout : bayer pattern layout
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetBayerLayout(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBayerLayout emLayout);
def ntcSetBayerLayout(hCameraHandle, emLayout):
    Neptune_dll.ntcSetBayerLayout.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetBayerLayout(hCameraHandle, emLayout)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Get image rotation angle 
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemAngle : rotation angle
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetRotation(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneRotationAngle* pemAngle);
def ntcGetRotation(hCameraHandle, pemAngle):
    Neptune_dll.ntcGetRotation.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetRotation(hCameraHandle, pemAngle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Set image rotation angle 
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emAngle : rotation angle
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetRotation(IN NeptuneCamHandle hCameraHandle, IN ENeptuneRotationAngle emAngle);
def ntcSetRotation(hCameraHandle, emAngle):
    Neptune_dll.ntcSetRotation.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetRotation(hCameraHandle, emAngle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Get image effect(flip, mirror, negative).
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pnEffectFlag : use ENeptuneEffect (combination is possible)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetEffect(IN NeptuneCamHandle hCameraHandle, OUT _int32_t* pnEffectFlag);
def ntcGetEffect(hCameraHandle, pnEffectFlag):
    Neptune_dll.ntcGetEffect.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetEffect(hCameraHandle, pnEffectFlag)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set image effect(flip, mirror, negative).
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] nEffectFlag : use ENeptuneEffect (combination is possible)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetEffect(IN NeptuneCamHandle hCameraHandle, IN _int32_t nEffectFlag);
def ntcSetEffect(hCameraHandle, nEffectFlag):
    Neptune_dll.ntcSetEffect.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetEffect(hCameraHandle, nEffectFlag)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Get camera list option value.
 	Parameters :
		[OUT] peCameraListOpt : Camera List Option
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetCameraListOpt(OUT ENeptuneCameraListOpt* pemCameraListOpt);
def ntcGetCameraListOpt(peCameraListOpt):
    Neptune_dll.ntcGetCameraListOpt.argtypes = [ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetCameraListOpt(peCameraListOpt)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Set camera list option value.
 	Parameters :
		[IN] eCameraListOption : Camera List Option
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetCameraListOpt(IN ENeptuneCameraListOpt emCameraListOpt);
def ntcSetCameraListOpt(eCameraListOption):
    Neptune_dll.ntcSetCameraListOpt.argtypes = [ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetCameraListOpt(eCameraListOption)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Get image display option.
 	Parameters :
		[OUT] pemDisplayOpt : Camera Display Option
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetDisplayOption(OUT ENeptuneDisplayOption* pemDisplayOpt);
def ntcGetDisplayOption(pemDisplayOpt):
    Neptune_dll.ntcGetDisplayOption.argtypes = [ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetDisplayOption(pemDisplayOpt)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Set image display option.
 	Parameters :
		[IN] emDisplayOpt : Camera Display Option
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetDisplayOption(IN ENeptuneDisplayOption emDisplayOpt);
def ntcSetDisplayOption(emDisplayOpt):
    Neptune_dll.ntcSetDisplayOption.argtypes = [ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetDisplayOption(emDisplayOpt)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Get image display option.
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] emDisplayMode : Camera Display Option
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetDisplayMode(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneDisplayOption& emDisplayMode);
def ntcGetDisplayMode(hCameraHandle, emDisplayMode):
    Neptune_dll.ntcGetDisplayMode.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcGetDisplayMode(hCameraHandle, emDisplayMode)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Set image display option.
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emDisplayMode : Camera Display Option
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetDisplayMode(IN NeptuneCamHandle hCameraHandle, IN ENeptuneDisplayOption emDisplayMode);
def ntcSetDisplayMode(hCameraHandle, emDisplayMode):
    Neptune_dll.ntcSetDisplayMode.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetDisplayMode(hCameraHandle, emDisplayMode)
    return Neptune_Error
##########################################################################
""""WINDOWS"""
##########################################################################
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetZoomFactor(IN NeptuneCamHandle hCameraHandle, OUT FLOAT& fZoomFactor);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetZoomFactor(IN NeptuneCamHandle hCameraHandle, IN FLOAT fZoomFactor);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetCursorPosRGBValue(IN NeptuneCamHandle hCameraHandle, OUT POINT& ptPixel, OUT COLORREF& clrValue);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetDisplay(IN NeptuneCamHandle hCameraHandle, IN HWND hWnd);
##########################################################################
"""
 	Description :
		show the camera control dialog
 	Parameters :
		[IN] hCameraHandle : camera handle to control
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcShowControlDialog(IN NeptuneCamHandle hCameraHandle);
def ntcShowControlDialog(hCameraHandle):
    Neptune_dll.ntcShowControlDialog.argtypes = [ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcShowControlDialog(hCameraHandle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		grab single image from a camera.
		return when a frame data is received and wait if no frame until nTimeOut value(in mili-second)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pImageInfo : image buffer and information
		[IN] emGrabFmt : grab data format(raw or RGB)
		[IN] uiTimeOut : timeout value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGrab(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_IMAGE pImageInfo, IN ENeptuneGrabFormat emGrabFmt, IN _uint32_t uiTimeOut = 1000);
def ntcGrab(hCamHandle, pImage, eGrabFormat, nTimeout = 1000):
    pImg = ctypes.POINTER(NEPTUNE_IMAGE)
    Neptune_dll.ntcGrab.argtypes = [ctypes.c_void_p, pImg, ctypes.c_int32, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGrab(hCamHandle, pImg(pImage), eGrabFormat, nTimeout)
    return Neptune_Error
##########################################################################
"""
 	Description :
		grab single image from a camera.
		return when a frame data is received and wait if no frame until nTimeOut value(in mili-second)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pImageInfoEx : image buffer and information (added trigger count)
		[IN] emGrabFmt : grab data format(raw or RGB)
		[IN] uiTimeOut : timeout value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGrabEx(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_IMAGE_EX pImageInfoEx, IN ENeptuneGrabFormat emGrabFmt, IN _uint32_t uiTimeOut = 1000);
def ntcGrabEx(hCameraHandle, pImageInfoEx, emGrabFmt, uiTimeOut):
    Neptune_dll.ntcGrabEx.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_IMAGE_EX), ctypes.c_int, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGrabEx(hCameraHandle, pImageInfoEx, emGrabFmt, uiTimeOut)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the RGB image data, should be called in the FrameCallback function
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pBuffer : RGB image data
		[IN] uiBufSize : size of the buffer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetRGBData(IN NeptuneCamHandle hCameraHandle, OUT _uchar_t* pBuffer, IN _uint32_t uiBufSize);
def ntcGetRGBData(hCameraHandle, pBuffer, uiBufSize):
    Neptune_dll.ntcGetRGBData.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGetRGBData(hCameraHandle, pBuffer, uiBufSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the RGB32 image data, should be called in the FrameCallback function
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pBuffer : RGB32 image data
		[IN] uiBufSize : size of the buffer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetRGB32Data(IN NeptuneCamHandle hCameraHandle, OUT _uchar_t* pBuffer, IN _uint32_t uiBufSize);
def ntcGetRGB32Data(hCameraHandle, pBuffer, uiBufSize):
    Neptune_dll.ntcGetRGB32Data.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGetRGB32Data(hCameraHandle, pBuffer, uiBufSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the temperature data, should be called in the FrameCallback function
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pBuffer : temperature data
		[IN] uiBufSize : size of the buffer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetTemperatureData(IN NeptuneCamHandle hCameraHandle, OUT _uchar_t* pBuffer, IN _uint32_t uiBufSize);
def ntcGetTemperatureData(hCameraHandle, pBuffer, uiBufSize):
    Neptune_dll.ntcGetTemperatureData.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcGetTemperatureData(hCameraHandle, pBuffer, uiBufSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		save snapshot to an image(jpg, tiff, bmp)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszFilePathName : image file name(image format is identified by the extension of the filename)
		[IN] uiQuality : jpeg image quality(valid only when save to JPEG)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSaveImage(IN NeptuneCamHandle hCameraHandle, IN _char_t* pszFilePathName, IN _uint32_t uiQuality = 80);
def ntcSaveImage(hCameraHandle, pszFilePathName, uiQuality = 80):
    Neptune_dll.ntcSaveImage.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSaveImage(hCameraHandle, pszFilePathName, uiQuality)
    return Neptune_Error
##########################################################################
"""
 	Description :
		start AVI stream capture
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszFilePathName : filename to save an AVI
		[IN] emCompress : not used
		[IN] uiBitrate : bit rate
		[IN] fPlaySpeed : play speed
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcStartStreamCapture(IN NeptuneCamHandle hCameraHandle, IN _char_t* pszFilePathName, IN ENeptuneBoolean emCompress = NEPTUNE_BOOL_TRUE, IN _uint32_t uiBitrate = 1000, IN _float32_t fPlaySpeed = 1.0);
def ntcStartStreamCapture(hCameraHandle, pszFilePathName, emCompress, uiBitrate = 1000, fPlaySpeed = 1.0):
    Neptune_dll.ntcStartStreamCapture.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int32, ctypes.c_uint32, ctypes.c_float]
    Neptune_Error = Neptune_dll.ntcStartStreamCapture()
    return Neptune_Error
##########################################################################
"""
 	Description :
		start AVI stream capture
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszFilePathName : filename to save an AVI
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
		[IN] emCompress : not used
		[IN] iOuputWidth : output width (0 : original width)
		[IN] iOutputHeight : output height (0 : original height)
		[IN] uiRecordCnt : Record count (0 : continue)
		[IN] fPixFps : Record fps (0 : real fps)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcStartStreamCaptureEx(IN NeptuneCamHandle hCamHandle, IN _char_t* pszFilePathName, IN NeptuneCStopRecordCallback fpCallback, IN void* pContext, IN ENeptuneBoolean emCompress = NEPTUNE_BOOL_TRUE, IN int iOuputWidth = 0, IN int iOutputHeight = 0, IN _int64_t uiRecordCnt = 0, IN _float32_t fFixFps = 0.0);
def ntcStartStreamCaptureEx(hCameraHandle, pszFilePathName, callback, pContext, emCompress= ENeptuneBoolean.NEPTUNE_BOOL_TRUE.value, iOuputWidth = 0, iOutputHeight = 0, uiRecordCnt = 0, fPixFps = 0.0):
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int32)
    Neptune_dll.ntcStartStreamCaptureEx.argtypes = [ctypes.c_void_p, ctypes.c_char_p, callback_type,ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int64, ctypes.c_float]
    Neptune_Error = Neptune_dll.ntcStartStreamCaptureEx(hCameraHandle, pszFilePathName, callback, pContext, emCompress, iOuputWidth, iOutputHeight, uiRecordCnt, fPixFps)
    return Neptune_Error
##########################################################################
"""
 	Description :
		stop AVI stream capture
 	Parameters :
		[IN] hCameraHandle : camera handle to control
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcStopStreamCapture(IN NeptuneCamHandle hCameraHandle);
def ntcStopStreamCapture(hCameraHandle):
    Neptune_dll.ntcStopStreamCapture.argtypes = [ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcStopStreamCapture(hCameraHandle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of an selected feature
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emFeatureType : feature 
		[OUT] pFeatureInfo : feature information structure
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetFeature(IN NeptuneCamHandle hCameraHandle, IN ENeptuneFeature emFeatureType, OUT PNEPTUNE_FEATURE pFeatureInfo);
def ntcGetFeature(hCameraHandle, emFeatureType, pFeatureInfo):
    Neptune_dll.ntcGetFeature.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(NEPTUNE_FEATURE)]
    Neptune_Error = Neptune_dll.ntcGetFeature(hCameraHandle, emFeatureType, pFeatureInfo)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set feature value and auto control if supported
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] eFeature : feature
		[IN] Info : feature information structure
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetFeature(IN NeptuneCamHandle hCameraHandle, IN ENeptuneFeature emFeatureType, IN NEPTUNE_FEATURE stFeatureInfo);
def ntcSetFeature(hCameraHandle, eFeature, Info):
    Neptune_dll.ntcSetFeature.argtypes = [ctypes.c_void_p, ctypes.c_int32, NEPTUNE_FEATURE]
    Neptune_Error = Neptune_dll.ntcSetFeature(hCameraHandle, eFeature, Info)
    return Neptune_Error
##########################################################################
"""
 	Description : 
 	    get value to shutter, gamma, sharpness, contrast, black level, gain (Only GigE Camera)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pPackageFeature : Package feature Values
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetPackageFeature(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_PACKAGE_FEATURE pPackageFeature);
def ntcGetPackageFeature(hCameraHandle, pPackageFeature):
    Neptune_dll.ntcGetPackageFeature.argtypes = [ctypes.c_void_p,ctypes.POINTER(NEPTUNE_PACKAGE_FEATURE)]
    Neptune_Error = Neptune_dll.ntcGetPackageFeature(hCameraHandle, pPackageFeature)
    return Neptune_Error
##########################################################################
"""
 	Description : 
 	    set value to shutter, gamma, sharpness, contrast, black level, gain at the same time (Only GigE Camera)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stPackageFeature : Package feature Values
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetPackageFeature(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_PACKAGE_FEATURE stPackageFeature);
def ntcSetPackageFeature(hCameraHandle, stPackageFeature):
    Neptune_dll.ntcSetPackageFeature.argtypes = [ctypes.c_void_p,NEPTUNE_PACKAGE_FEATURE]
    Neptune_Error = Neptune_dll.ntcSetPackageFeature(hCameraHandle, stPackageFeature)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Get exposure time value
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiMicroSec : exposure time
		[OUT] puiMin : min of range
		[OUT] puiMax : max of range
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetExposureTime(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiMicroSec, OUT _uint32_t* puiMin = NULL, OUT _uint32_t* puiMax = NULL);
def ntcGetExposureTime(hCameraHandle, puiMicroSec, puiMin = None, puiMax = None):
    Neptune_dll.ntcGetExposureTime.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetExposureTime(hCameraHandle, puiMicroSec, puiMin, puiMax)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Set exposure time value
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] puiMicroSec : exposure time
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetExposureTime(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiMicroSec);
def ntcSetExposureTime(hCameraHandle, puiMicroSec):
    Neptune_dll.ntcSetExposureTime.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetExposureTime(hCameraHandle, puiMicroSec)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set shutter value with a string like as "100 ms"
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszShutter : shutter value string
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetShutterString(IN NeptuneCamHandle hCameraHandle, IN _char_t* pszExposureTime);
def ntcSetShutterString(hCameraHandle, pszShutter):
    Neptune_dll.ntcSetShutterString.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcSetShutterString(hCameraHandle, pszShutter)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set exposure time and interval for trigger mode14 
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiExposure : exposure time for trigger mode14
		[IN] uiInterval : interval time for trigger mode14
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetTriggerMode14Exposure(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiExposure, IN _uint32_t uiInterval);
def ntcSetTriggerMode14Exposure(hCameraHandle, uiExposure, uiInterval):
    Neptune_dll.ntcSetTriggerMode14Exposure.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetTriggerMode14Exposure(hCameraHandle, uiExposure, uiInterval)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get trigger information supported by a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pTriggerInfo : trigger information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetTriggerInfo(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_TRIGGER_INFO pTriggerInfo);
def ntcGetTriggerInfo(hCameraHandle, pTriggerInfo):
    Neptune_dll.ntcGetTriggerInfo.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_TRIGGER_INFO)]
    Neptune_Error = Neptune_dll.ntcGetTriggerInfo(hCameraHandle, pTriggerInfo)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get current trigger values
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pTrigger : trigger value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetTrigger(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_TRIGGER pTrigger);
def ntcGetTrigger(hCameraHandle, pTrigger):
    Neptune_dll.ntcGetTrigger.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_TRIGGER)]
    Neptune_Error = Neptune_dll.ntcGetTrigger(hCameraHandle, pTrigger)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set trigger values to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stTrigger : trigger value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetTrigger(IN NeptuneCamHandle hCameraHandle, OUT NEPTUNE_TRIGGER stTrigger);
def ntcSetTrigger(hCameraHandle, stTrigger):
    Neptune_dll.ntcSetTrigger.argtypes = [ctypes.c_void_p, NEPTUNE_TRIGGER]
    Neptune_Error = Neptune_dll.ntcSetTrigger(hCameraHandle, stTrigger)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get current trigger delay value
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiDelay : current trigger delay value
		[OUT] puiMin : minimum trigger value supported by a camera
		[OUT] puiMax : maximum trigger value supported by a camera
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetTriggerDelay(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiValue, OUT _uint32_t* puiMin = NULL, _uint32_t* puiMax = NULL);
def ntcGetTriggerDelay(hCameraHandle, puiDelay, puiMin = None, puiMax = None):
    Neptune_dll.ntcGetTriggerDelay.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32),ctypes.POINTER(ctypes.c_uint32),ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetTriggerDelay(hCameraHandle, puiDelay, puiMin, puiMax)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set trigger delay value to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] nDelay : trigger delay value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetTriggerDelay(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiValue);
def ntcSetTriggerDelay(hCameraHandle, nDelay):
    Neptune_dll.ntcSetTriggerDelay.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetTriggerDelay(hCameraHandle, nDelay)
    return Neptune_Error
##########################################################################
"""
 	Description :
		generate software trigger
 	Parameters :
		[IN] hCameraHandle : camera handle to control
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcRunSWTrigger(IN NeptuneCamHandle hCameraHandle);
def ntcRunSWTrigger(hCameraHandle):
    Neptune_dll.ntcRunSWTrigger.argtypes = [ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcRunSWTrigger(hCameraHandle)
    return Neptune_Error
##########################################################################
"""
 	Description :
		generate software trigger
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiTimeout : timeout value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcRunSWTriggerEx(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiTimeout);
def ntcRunSWTriggerEx(hCameraHandle, uiTimeout):
    Neptune_dll.ntcRunSWTriggerEx.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcRunSWTriggerEx(hCameraHandle, uiTimeout)
    return Neptune_Error
##########################################################################
"""
 	Description :
		read trigger table from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pTriggerTable : trigger table
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcReadTriggerTable(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_TRIGGER_TABLE pTriggerTable);
def ntcReadTriggerTable(hCameraHandle, pTriggerTable):
    Neptune_dll.ntcReadTriggerTable.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_TRIGGER_TABLE)]
    Neptune_Error = Neptune_dll.ntcReadTriggerTable(hCameraHandle, pTriggerTable)
    return Neptune_Error
##########################################################################
"""
 	Description :
		write and save trigger table to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stTriggerTable : trigger table
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSaveTriggerTable(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_TRIGGER_TABLE stTriggerTable);
def ntcSaveTriggerTable(hCameraHandle, stTriggerTable):
    Neptune_dll.ntcSaveTriggerTable.argtypes = [ctypes.c_void_p, NEPTUNE_TRIGGER_TABLE]
    Neptune_Error = Neptune_dll.ntcSaveTriggerTable(hCameraHandle, stTriggerTable)
    return Neptune_Error
##########################################################################
"""
 	Description :
		make camera to load specific trigger table
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] nIndex : index of trigger table to load
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcLoadTriggerTable(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiIndex);
def ntcLoadTriggerTable(hCameraHandle, nIndex):
    Neptune_dll.ntcLoadTriggerTable.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcLoadTriggerTable(hCameraHandle, nIndex)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the strobe information supported by a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pStrobeInfo : strobe information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStrobeInfo(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_STROBE_INFO pStrobeInfo);
def ntcGetStrobeInfo(hCameraHandle, pStrobeInfo):
    Neptune_dll.ntcGetStrobeInfo.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_STROBE_INFO)]
    Neptune_Error = Neptune_dll.ntcGetStrobeInfo(hCameraHandle, pStrobeInfo)
    return Neptune_Error
##########################################################################
"""
 	Description :
		read strobe value from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pStrobe : strobe value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStrobe(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_STROBE pStrobe);
def ntcGetStrobe(hCameraHandle, pStrobe):
    Neptune_dll.ntcGetStrobe.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_STROBE)]
    Neptune_Error = Neptune_dll.ntcGetStrobe(hCameraHandle, pStrobe)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set strobe value to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stStrobe : strobe value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStrobe(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_STROBE stStrobe);
def ntcSetStrobe(hCameraHandle, stStrobe):
    Neptune_dll.ntcSetStrobe.argtypes = [ctypes.c_void_p, NEPTUNE_STROBE]
    Neptune_Error = Neptune_dll.ntcSetStrobe(hCameraHandle, stStrobe)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of area for auto function(AutoExposure, AutoWhiteBalance, AutoFocus)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emSelect : auto control feature to get information
		[OUT] pAutoArea : auto area information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAutoAreaControl(IN NeptuneCamHandle hCameraHandle, IN ENeptuneAutoAreaSelect emSelect, OUT PNEPTUNE_AUTOAREA pAutoArea);
def ntcGetAutoAreaControl(hCameraHandle, emSelect, pAutoArea):
    Neptune_dll.ntcGetAutoAreaControl.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(NEPTUNE_AUTOAREA)]
    Neptune_Error = Neptune_dll.ntcGetAutoAreaControl(hCameraHandle, emSelect, pAutoArea)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set information of area for auto function(AutoExposure, AutoWhiteBalance, AutoFocus)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emSelect : auto control feature to get information
		[IN] stAutoArea : auto area information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAutoAreaControl(IN NeptuneCamHandle hCameraHandle, IN ENeptuneAutoAreaSelect emSelect, IN NEPTUNE_AUTOAREA stAutoArea);
def ntcSetAutoAreaControl(hCameraHandle, emSelect, stAutoArea):
    Neptune_dll.ntcSetAutoAreaControl.argtypes = [ctypes.c_void_p, ctypes.c_int32, NEPTUNE_AUTOAREA]
    Neptune_Error = Neptune_dll.ntcSetAutoAreaControl(hCameraHandle, emSelect, stAutoArea)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set Auto focus working mode
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emControlMode : auto focus control mode
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAFControl(IN NeptuneCamHandle hCameraHandle, IN ENeptuneAFMode emControlMode);
def ntcSetAFControl(hCameraHandle, emControlMode):
    Neptune_dll.ntcSetAFControl.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetAFControl(hCameraHandle, emControlMode)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set AutoIris mode
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emAutoIrisMode : AutoIris operation mode(Auto, Manual)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAutoIrisMode(IN NeptuneCamHandle hCameraHandle, IN ENeptuneAutoIrisMode emAutoIrisMode);
def ntcSetAutoIrisMode(hCameraHandle, emAutoIrisMode):
    Neptune_dll.ntcSetAutoIrisMode.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetAutoIrisMode(hCameraHandle, emAutoIrisMode)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get number of frames used for calculating brightness
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiValue : current AutoIris average frame value
		[OUT] puiMin : minimum AutoIris average frame value supported
		[OUT] puiMax : maximum AutoIris average frame value supported
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAutoIrisAverageFrame(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiValue, OUT _uint32_t* puiMin = NULL, OUT _uint32_t* puiMax = NULL);
def ntcGetAutoIrisAverageFrame(hCameraHandle, puiValue, puiMin = None, puiMax = None):
    Neptune_dll.ntcGetAutoIrisAverageFrame.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetAutoIrisAverageFrame(hCameraHandle, puiValue, puiMin, puiMax)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get number of frames used for calculating brightness
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiValue : AutoIris average frame value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAutoIrisAverageFrame(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiValue);
def ntcSetAutoIrisAverageFrame(hCameraHandle, uiValue):
    Neptune_dll.ntcSetAutoIrisAverageFrame.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetAutoIrisAverageFrame(hCameraHandle, uiValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get target brightness level of AutoIris
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiValue : current AutoIris target value
		[OUT] puiMin : minimum AutoIris target value
		[OUT] puiMax : maximum AutoIris target value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAutoIrisTargetValue(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiValue, OUT _uint32_t* puiMin = NULL, OUT _uint32_t* puiMax = NULL);
def ntcGetAutoIrisTargetValue(hCameraHandle, puiValue, puiMin = None, puiMax = None):
    Neptune_dll.ntcGetAutoIrisTargetValue.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetAutoIrisTargetValue(hCameraHandle, puiValue, puiMin, puiMax)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set target brightness level of AutoIris
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiValue : AutoIris target value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAutoIrisTargetValue(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiValue);
def ntcSetAutoIrisTargetValue(hCameraHandle, uiValue):
    Neptune_dll.ntcSetAutoIrisTargetValue.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetAutoIrisTargetValue(hCameraHandle, uiValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get data bits per image pixel
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiValue : data bits per image pixel
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetBitsPerPixel(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiValue);
def ntcGetBitsPerPixel(hCameraHandle, puiValue):
    Neptune_dll.ntcGetBitsPerPixel.argtypes = [ctypes.c_void_p,ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetBitsPerPixel(hCameraHandle, puiValue) 
    return Neptune_Error

##########################################################################
"""
 	Description :
		get the byte per packet information(for 1394 camera Format7 only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiValue : byte per packet value
		[OUT] puiMin : minimum byte per packet value supported
		[OUT] puiMax : maximum byte per packet value supported
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetBytePerPacket(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiValue, OUT _uint32_t* puiMin = NULL, OUT _uint32_t* puiMax = NULL);
def ntcGetBytePerPacket(hCameraHandle, puiValue, puiMin = None, puiMax = None):
    Neptune_dll.ntcGetBytePerPacket.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetBytePerPacket(hCameraHandle, puiValue, puiMin, puiMax)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set the byte per packet to a camera(for 1394 camera Format7 only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiValue : byte per packet value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetBytePerPacket(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiValue);
def ntcSetBytePerPacket(hCameraHandle, uiValue):
    Neptune_dll.ntcSetBytePerPacket.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetBytePerPacket(hCameraHandle, uiValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the current transfer packet size of GigE camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiValue : packet size value
		[OUT] puiMin : minimum packet size value supported
		[OUT] puiMax : maximum packet size value supported
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetPacketSize(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiValue, OUT _uint32_t* puiMin = NULL, OUT _uint32_t* puiMax = NULL);
def ntcGetPacketSize(hCameraHandle, puiValue, puiMin = None, puiMax = None):
    Neptune_dll.ntcGetPacketSize.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetPacketSize(hCameraHandle, puiValue, puiMin, puiMax)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set the transfer packet size of GigE camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiValue : size of the packet
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetPacketSize(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiValue);
def ntcSetPacketSize(hCameraHandle, uiValue):
    Neptune_dll.ntcSetPacketSize.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetPacketSize(hCameraHandle, uiValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Enable/Disable packet resend control
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emEnableResend : Enable/Disable flag
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetPacketResend(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emEnable);
def ntcSetPacketResend(hCameraHandle, emEnableResend):
    Neptune_dll.ntcSetPacketResend.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetPacketResend(hCameraHandle, emEnableResend)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get the number of image buffer of an NeptuneC API
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiCount : number of buffer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetBufferCount(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiCount);
def ntcGetBufferCount(hCameraHandle, puiCount):
    Neptune_dll.ntcGetBufferCount.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetBufferCount(hCameraHandle, puiCount)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set the number of image buffer of an NeptuneC API
		Default buffer count is 10.
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiCount : number of buffer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetBufferCount(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiCount);
def ntcSetBufferCount(hCameraHandle, uiCount):
    Neptune_dll.ntcSetBufferCount.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetBufferCount(hCameraHandle, uiCount)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set buffer count for trigger mode of USB camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiCount : number of buffers
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetUSBTriggerBufferCount(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiCount);
def ntcSetUSBTriggerBufferCount(hCameraHandle, uiCount):
    Neptune_dll.ntcSetUSBTriggerBufferCount.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetUSBTriggerBufferCount(hCameraHandle, uiCount)
    return Neptune_Error
##########################################################################
"""
 	Description
		get the size of one frame image data
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiSize : size of an image data
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetBufferSize(IN NeptuneCamHandle hCameraHandle, IN _uint32_t* puiSize);
def ntcGetBufferSize(hCameraHandle, puiSize):
    Neptune_dll.ntcGetBufferSize.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetBufferSize(hCameraHandle, puiSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		Enable/Disable receiving dropped frame data
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emEnable : Enable/Disable flag
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetRecvDroppedFrame(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emEnable);
def ntcSetRecvDroppedFrame(hCameraHandle, emEnable):
    Neptune_dll.ntcSetRecvDroppedFrame.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetRecvDroppedFrame(hCameraHandle, emEnable)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set the heartbeat time of GigE camera(GigE camera only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] ulMilliSecTime : heartbeat time in millisecond unit
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetHeartbeatTime(IN NeptuneCamHandle hCameraHandle, IN _ulong32_t ulMilliSecTime);
def ntcSetHeartbeatTime(hCameraHandle, ulMilliSecTime):
    Neptune_dll.ntcSetHeartbeatTime.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    Neptune_Error = Neptune_dll.ntcSetHeartbeatTime(hCameraHandle, ulMilliSecTime)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set multicast address
 	Parameter :
		[IN] hCameraHandle : camera handle to control
		[IN] pszAddress : multicast IP address
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetMulticastAddress(IN NeptuneCamHandle hCameraHandle, IN _char_t* pszAddress);
def ntcSetMulticastAddress(hCameraHandle, pszAddress):
    Neptune_dll.ntcSetMulticastAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcSetMulticastAddress(hCameraHandle, pszAddress)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get supported user set by a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pUserSet : user set information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetUserSet(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_USERSET pUserSet);
def ntcGetUserSet(hCameraHandle, pUserSet):
    Neptune_dll.ntcGetUserSet.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_USERSET)]
    Neptune_Error = Neptune_dll.ntcGetUserSet(hCameraHandle, pUserSet)
    return Neptune_Error
##########################################################################
"""
 	Description :
		save or load user set
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] UserSet : user set value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetUserSet(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_USERSET stUserSet);
def ntcSetUserSet(hCameraHandle, stUserSet):
    Neptune_dll.ntcSetUserSet.argtypes = [ctypes.c_void_p, NEPTUNE_USERSET]
    Neptune_Error = Neptune_dll.ntcSetUserSet(hCameraHandle, stUserSet)
    return Neptune_Error
##########################################################################
"""
 	Description :
		make specific user set as a default user set
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] eUserSet : user set value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetDefaultUserSet(IN NeptuneCamHandle hCameraHandle, IN ENeptuneUserSet emUserSet);
def ntcSetDefaultUserSet(hCameraHandle, eUserSet):
    Neptune_dll.ntcSetDefaultUserSet.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetDefaultUserSet(hCameraHandle, eUserSet)
    return Neptune_Error
##########################################################################
"""
 	Description :
		make specific user set as a default user set when camera is power on
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] eUserSet : user set value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetPowerOnDefaultUserSet(IN NeptuneCamHandle hCameraHandle, IN ENeptuneUserSet emUserSet);
def ntcSetPowerOnDefaultUserSet(hCameraHandle, eUserSet):
    Neptune_dll.ntcSetPowerOnDefaultUserSet.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetPowerOnDefaultUserSet(hCameraHandle, eUserSet)
    return Neptune_Error
##########################################################################
"""
 	Description :
		save camera parameter to a file
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszFilePathName : file name to save camera parameter
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSaveCameraParameter(IN NeptuneCamHandle hCameraHandle, IN _char_t* pszFilePathName);
def ntcSaveCameraParameter(hCameraHandle, pszFilePathName):
    Neptune_dll.ntcSaveCameraParameter.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcSaveCameraParameter(hCameraHandle, pszFilePathName)
    return Neptune_Error
##########################################################################
"""
 	Description :
		load camera parameter from a file
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszFilePathName : file name from which to load camera parameter
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcLoadCameraParameter(IN NeptuneCamHandle hCameraHandle, IN _char_t* pszFilePathName);
def ntcLoadCameraParameter(hCameraHandle, pszFilePathName):
    Neptune_dll.ntcLoadCameraParameter.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcLoadCameraParameter(hCameraHandle, pszFilePathName)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get 4-step knee table points
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pKneeLUT : 4-step knee table points
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetKneeLUT(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_KNEE_LUT pKneeLUT);
def ntcGetKneeLUT(hCameraHandle, pKneeLUT):
    Neptune_dll.ntcGetKneeLUT.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_KNEE_LUT)]
    Neptune_Error = Neptune_dll.ntcGetKneeLUT(hCameraHandle, pKneeLUT)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set 4-step knee table points
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stKneeLUT : 4-step knee table points
   
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetKneeLUT(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_KNEE_LUT stKneeLUT);
def ntcSetKneeLUT(hCameraHandle, stKneeLUT):
    Neptune_dll.ntcSetKneeLUT.argtypes = [ctypes.c_void_p, NEPTUNE_KNEE_LUT]
    Neptune_Error = Neptune_dll.ntcSetKneeLUT(hCameraHandle, stKneeLUT)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get user look-up-table value
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pUserLUT : user look-up-table value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetUserLUT(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_USER_LUT pUserLUT);
def ntcGetUserLUT(hCameraHandle, pUserLUT):
    Neptune_dll.ntcGetUserLUT.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_USER_LUT)]
    Neptune_Error = Neptune_dll.ntcGetUserLUT(hCameraHandle, pUserLUT)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set user look-up-table to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] stUserLUT : user look-up-table value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetUserLUT(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_USER_LUT stUserLUT);
def ntcSetUserLUT(hCameraHandle, stUserLUT):
    Neptune_dll.ntcSetUserLUT.argtypes = [ctypes.c_void_p, NEPTUNE_USER_LUT]
    Neptune_Error = Neptune_dll.ntcSetUserLUT(hCameraHandle, stUserLUT)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get frame save information from a camera (1394 camera only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemOnOff : frame save on/off state
		[OUT] puiFrameRemained : number of frames remained in the camera memory
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetFrameSave(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBoolean* pemOnOff, OUT _uint32_t* puiFrameRemained);
def ntcGetFrameSave(hCameraHandle, pemOnOff, puiFrameRemained):
    Neptune_dll.ntcGetFrameSave.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetFrameSave()
    return Neptune_Error
##########################################################################
"""
 	Description :
		control camera to transfer saved frames (1394 camera only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emOnOff : frame save on/off control
		[IN] emTransfer : transfer control
		[IN] uiFrames : number of frames to transfer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetFrameSave(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emOnOff, IN ENeptuneBoolean emTransfer, IN _uint32_t uiFrames);
def ntcSetFrameSave(hCameraHandle, emOnOff, emTransfer, uiFrames):
    Neptune_dll.ntcSetFrameSave.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetFrameSave(hCameraHandle, emOnOff, emTransfer, uiFrames)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set GPIO to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] Gpio : GPIO value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetGPIO(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_GPIO stGpio);
def ntcSetGPIO(hCameraHandle, Gpio):
    Neptune_dll.ntcSetGPIO.argtypes = [ctypes.c_void_p, NEPTUNE_GPIO]
    Neptune_Error = Neptune_dll.ntcSetGPIO(hCameraHandle, Gpio)
    return Neptune_Error
##########################################################################
"""
 	Description :
		read serial data from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pData : serial data
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcReadSIO(IN NeptuneCamHandle hCameraHandle, OUT PNEPTUNE_SIO pData);
def ntcReadSIO(hCameraHandle, pData):
    Neptune_dll.ntcReadSIO.argtypes = [ctypes.c_void_p, ctypes.POINTER(NEPTUNE_SIO)]
    Neptune_Error = Neptune_dll.ntcReadSIO(hCameraHandle, pData)
    return Neptune_Error
##########################################################################
"""
 	Description :
		write serial data to a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] Data : serial data
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcWriteSIO(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_SIO stData);
def ntcWriteSIO(hCameraHandle, Data):
    Neptune_dll.ntcWriteSIO.argtypes = [ctypes.c_void_p, NEPTUNE_SIO]
    Neptune_Error = Neptune_dll.ntcWriteSIO(hCameraHandle, Data)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set camera's serial output port information
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] Property : serial information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetSIO(IN NeptuneCamHandle hCameraHandle, IN NEPTUNE_SIO_PROPERTY stProperty);
def ntcSetSIO(hCameraHandle, Property):
    Neptune_dll.ntcSetSIO.argtypes = [ctypes.c_void_p, NEPTUNE_SIO_PROPERTY]
    Neptune_Error = Neptune_dll.ntcSetSIO(hCameraHandle, Property)
    return Neptune_Error
##########################################################################
"""
 	Description :
		read 4 bytes from a camera register
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] ulAddress : register address
		[OUT] pulValue : register value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcReadRegister(IN NeptuneCamHandle hCameraHandle, IN _ulong32_t ulAddress, OUT _ulong32_t* pulValue);
def ntcReadRegister(hCameraHandle, ulAddress, pulValue):
    Neptune_dll.ntcReadRegister.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)]
    Neptune_Error = Neptune_dll.ntcReadRegister(hCameraHandle, ulAddress, pulValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		write 4 bytes to a camera register
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] ulAddress : register address
		[IN] ulValue : value to write
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcWriteRegister(IN NeptuneCamHandle hCameraHandle, IN _ulong32_t ulAddress, IN _ulong32_t ulValue);
def ntcWriteRegister(hCameraHandle, ulAddress, ulValue):
    Neptune_dll.ntcWriteRegister.argtypes = [ctypes.c_void_p, ctypes.c_ulong,ctypes.c_ulong]
    Neptune_Error = Neptune_dll.ntcWriteRegister(hCameraHandle, ulAddress, ulValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		read data a camera register
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] ulAddress : start register address
		[OUT] pBuffer : buffer to read data
		[IN/OUT] pulBufSize : number of bytes to read
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcReadBlock(IN NeptuneCamHandle hCameraHandle, IN _ulong32_t ulAddress, OUT _uint8_t* pBuffer, IN OUT _ulong32_t* pulBufSize);
def ntcReadBlock(hCameraHandle, ulAddress, pBuffer, pulBufSize):
    Neptune_dll.ntcReadBlock.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint8),ctypes.POINTER(ctypes.c_ulong)]
    Neptune_Error = Neptune_dll.ntcReadBlock(hCameraHandle, ulAddress, pBuffer, pulBufSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		write data to a camera register
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] ulAddress : start register address
		[IN] pBuf : buffer to write
		[IN] nSize : size of the buffer
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcWriteBlock(IN NeptuneCamHandle hCameraHandle, IN _ulong32_t ulAddress, IN _uint8_t* pBuffer, IN _ulong32_t ulBufSize);
def ntcWriteBlock(hCameraHandle, ulAddress, pBuf, nSize):
    Neptune_dll.ntcWriteBlock.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint8), ctypes.c_ulong]
    Neptune_Error = Neptune_dll.ntcWriteBlock(hCameraHandle, ulAddress, pBuf, nSize)
    return Neptune_Error
##########################################################################
"""
 	Description :
		write broadcast to 1394 cameras
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] ulAddress : register address
		[IN] ulValue : value to write
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcWriteBroadcast(IN NeptuneCamHandle hCameraHandle, IN _ulong32_t ulAddress, IN _ulong32_t ulValue);
def ntcWriteBroadcast(hCameraHandle, ulAddress, ulValue):
    Neptune_dll.ntcWriteBroadcast.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong]
    Neptune_Error = Neptune_dll.ntcWriteBroadcast(hCameraHandle, ulAddress, ulValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get current visibility value of XML tree
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemVisibility : visibility (Beginner, Expert, Guru, Invisible)
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeVisibility(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneNodeVisibility* pemVisibility);
def ntcGetNodeVisibility(hCameraHandle, pemVisibility):
    Neptune_dll.ntcGetNodeVisibility.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetNodeVisibility(hCameraHandle, pemVisibility)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set visibility of XML tree
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emVisibility : visibility 
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeVisibility(IN NeptuneCamHandle hCameraHandle, IN ENeptuneNodeVisibility emVisibility);
def ntcSetNodeVisibility(hCameraHandle, emVisibility):
    Neptune_dll.ntcSetNodeVisibility.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetNodeVisibility(hCameraHandle, emVisibility)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get child tree of a given XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszParentNodeName : node
		[OUT] pNodeInfoList : child node tree
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeList(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszParentNodeName, OUT PNEPTUNE_XML_NODE_LIST pNodeInfoList);
def ntcGetNodeList(hCameraHandle, pszParentNodeName, pNodeInfoList):
    Neptune_dll.ntcGetNodeList.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(NEPTUNE_XML_NODE_LIST)]
    Neptune_Error = Neptune_dll.ntcGetNodeList(hCameraHandle, pszParentNodeName, pNodeInfoList)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get child tree of a given XML node (for C#)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszParentNodeName : node
		[OUT] pBuffer : child node tree
		[IN] uiStrLength : size of string
		[IN,OUT] puiCount : number of strings
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeListChar(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszParentNodeName, OUT _char_t* pBuffer, IN _uint32_t uiStrLength, IN OUT _uint32_t* puiCount);
def ntcGetNodeListChar(hCameraHandle, pszParentNodeName, pBuffer, uiStrLength, puiCount):
    Neptune_dll.ntcGetNodeListChar.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetNodeListChar(hCameraHandle, pszParentNodeName, pBuffer, uiStrLength, puiCount)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of a XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pNodeInfo : information of a XML node
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeInfo(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT PNEPTUNE_XML_NODE_INFO pNodeInfo);
def ntcGetNodeInfo(hCameraHandle, pszNodeName, pNodeInfo):
    Neptune_dll.ntcGetNodeInfo.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(NEPTUNE_XML_NODE_INFO)]
    Neptune_Error = Neptune_dll.ntcGetNodeInfo(hCameraHandle, pszNodeName, pNodeInfo)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of integer type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pValueInfo : integer value information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeInt(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT PNEPTUNE_XML_INT_VALUE_INFO pValueInfo);

#### NEPTUNE_XML_INT_VALUE_INFO 로 수정 ### 
def ntcGetNodeInt(hCameraHandle, pszNodeName, pValueInfo):
    Neptune_dll.ntcGetNodeInt.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(NEPTUNE_XML_INT_VALUE_INFO)]
    Neptune_Error = Neptune_dll.ntcGetNodeInt(hCameraHandle, pszNodeName, pValueInfo)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set value to an integer type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[IN] nValue : integer value to write
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeInt(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, IN _int64_t nValue);
def ntcSetNodeInt(hCameraHandle, pszNodeName, nValue):
    Neptune_dll.ntcSetNodeInt.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int64]
    Neptune_Error = Neptune_dll.ntcSetNodeInt(hCameraHandle, pszNodeName, nValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of float type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pValueInfo : float value information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeFloat(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT PNEPTUNE_XML_FLOAT_VALUE_INFO pValueInfo);
def ntcGetNodeFloat(hCameraHandle, pszNodeName, pValueInfo):
    Neptune_dll.ntcGetNodeFloat.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(NEPTUNE_XML_FLOAT_VALUE_INFO)]
    Neptune_Error = Neptune_dll.ntcGetNodeFloat(hCameraHandle, pszNodeName, pValueInfo)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set value to a float type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[IN] dbValue : float value to write
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeFloat(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, IN _double_t dbValue);
def ntcSetNodeFloat(hCameraHandle, pszNodeName, dbValue):
    Neptune_dll.ntcSetNodeFloat.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_double]
    Neptune_Error = Neptune_dll.ntcSetNodeFloat(hCameraHandle, pszNodeName, dbValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of enumeration type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pEnumList : enumeration value information
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeEnum(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT PNEPTUNE_XML_ENUM_LIST pEnumList);
def ntcGetNodeEnum(hCameraHandle, pszNodeName, pEnumList):
    Neptune_dll.ntcGetNodeEnum.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(NEPTUNE_XML_ENUM_LIST)]
    Neptune_Error = Neptune_dll.ntcGetNodeEnum(hCameraHandle, pszNodeName, pEnumList)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of enumeration type XML node(for C#)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pBuffer : enumeration value information (size is nSize*pnCount)
		[IN] uiStrLength : should be 256
		[IN, OUT] puiCount : number of strings
		[OUT] puiIndex : current enumeration string index
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeEnumChar(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT _char_t* pBuffer, IN _uint32_t uiStrLength, IN OUT _uint32_t* puiCount, OUT _uint32_t* puiIndex);
def ntcGetNodeEnumChar(hCameraHandle, pszNodeName, pBuffer, uiStrLength, puiCount, puiIndex):
    Neptune_dll.ntcGetNodeEnumChar.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32) ,ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetNodeEnumChar(hCameraHandle, pszNodeName, pBuffer, uiStrLength, puiCount, puiIndex)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set value to an enumeration type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[IN] pszValue : enumeration string to write
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeEnum(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, IN const _char_t* pszValue);
def ntcSetNodeEnum(hCameraHandle, pszNodeName, pszValue):
    Neptune_dll.ntcSetNodeEnum.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcSetNodeEnum(hCameraHandle, pszNodeName, pszValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get information of string type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pBuffer : string value
		[IN/OUT] puiBufSize : size of string
		[OUT] pemAccessMode : access mode of a node
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeString(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT _char_t* pBuffer, IN OUT _uint32_t* puiBufSize, OUT ENeptuneNodeAccessMode* pemAccessMode);
def ntcGetNodeString(hCameraHandle, pszNodeName, pBuffer, puiBufSize, pemAccessMode):
    Neptune_dll.ntcGetNodeString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetNodeString(hCameraHandle, pszNodeName, pBuffer, puiBufSize, pemAccessMode)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set value to a string type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[IN] pszValue : string value to write
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeString(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, IN const _char_t* pszValue);
def ntcSetNodeString(hCameraHandle, pszNodeName, pszValue):
    Neptune_dll.ntcSetNodeString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcSetNodeString(hCameraHandle, pszNodeName, pszValue)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get value of boolean type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[OUT] pemState : boolean value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNodeBoolean(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, OUT ENeptuneBoolean* pemState);
def ntcGetNodeBoolean(hCameraHandle, pszNodeName, pemState):
    Neptune_dll.ntcGetNodeBoolean.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetNodeBoolean(hCameraHandle, pszNodeName, pemState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set value to boolean type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
		[IN] emState : boolean value
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeBoolean(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName, IN ENeptuneBoolean emState);
def ntcSetNodeBoolean(hCameraHandle, pszNodeName, emState):
    Neptune_dll.ntcSetNodeBoolean.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetNodeBoolean(hCameraHandle, pszNodeName, emState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		make execute command type XML node
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pszNodeName : XML node
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNodeCommand(IN NeptuneCamHandle hCameraHandle, IN const _char_t* pszNodeName);
def ntcSetNodeCommand(hCameraHandle, pszNodeName):
    Neptune_dll.ntcSetNodeCommand.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    Neptune_Error = Neptune_dll.ntcSetNodeCommand(hCameraHandle, pszNodeName)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set callback function called when number of device changed
 	Parameters :
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
        
"""
# typedef void (CALLBACK *NeptuneCDevCheckCallback)(ENeptuneDeviceChangeState emState, void* pContext);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetDeviceCheckCallback(IN NeptuneCDevCheckCallback callback, IN void* pContext);
def ntcSetDeviceCheckCallback(callback, pContext):
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_void_p)
    Neptune_dll.ntcSetDeviceCheckCallback.argtypes = [callback_type, ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcSetDeviceCheckCallback(callback, pContext)
    return Neptune_Error
##########################################################################
"""
 	Description :
		register callback function which is called when selected camera is plugged off
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetUnplugCallback(IN NeptuneCamHandle hCameraHandle, IN NeptuneCUnplugCallback fpCallback, IN void* pContext);
def ntcSetUnplugCallback(hCameraHandle, callback, pContext):
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    Neptune_dll.ntcSetUnplugCallback.argtypes = [ctypes.c_void_p, callback_type, ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcSetUnplugCallback(hCameraHandle, callback, pContext)
    return Neptune_Error
##########################################################################
"""
 	Description :
		register callback function called when a new frame data is received
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetFrameCallback(IN NeptuneCamHandle hCameraHandle, IN NeptuneCFrameCallback fpCallback, IN void* pContext);



def ntcSetFrameCallback(hCameraHandle, callback, pContext):
    callback_type = ctypes.CFUNCTYPE(None, NEPTUNE_IMAGE, ctypes.c_void_p)
    Neptune_dll.ntcSetFrameCallback.argtypes = [ctypes.c_void_p,callback_type,ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcSetFrameCallback(hCameraHandle, callback, pContext)
    return Neptune_Error
##########################################################################
"""
 	Description :
		register callback function called when a frame data is dropped
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetFrameDropCallback(IN NeptuneCamHandle hCameraHandle, IN NeptuneCFrameDropCallback fpCallback, IN void* pContext);
def ntcSetFrameDropCallback(hCameraHandle, callback, pContext):
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    Neptune_dll.ntcSetFrameDropCallback.argtypes = [ctypes.c_void_p, callback_type, ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcSetFrameDropCallback(hCameraHandle, callback, pContext)
    return Neptune_Error
##########################################################################
"""
 	Description :
		register callback function called when a frame receive is timeout
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetRecvTimeoutCallback(IN NeptuneCamHandle hCameraHandle, IN NeptuneCRecvTimeoutCallback fpCallback, IN void* pContext);
def ntcSetRecvTimeoutCallback(hCameraHandle, callback, pContext):
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    Neptune_dll.ntcSetRecvTimeoutCallback.argtypes = [ctypes.c_void_p, callback_type, ctypes.c_void_p]
    Neptune_Error = Neptune_dll.ntcSetRecvTimeoutCallback(hCameraHandle, callback, pContext)
    return Neptune_Error
##########################################################################
"""
 	Description :
		register callback function called when a frame drawing
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] callback : callback function
		[IN] pContext : user parameter passed to the callback function
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetOverlayCallback(IN NeptuneCamHandle hCameraHandle, IN NeptuneCOverlayCallback fpCallback, IN void* pContext);
# def aaaaaaaa():
#     callback_type = ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_void_p)
#     Neptune_dll.aaaaaaaa.argtypes = []
#     Neptune_Error = Neptune_dll.aaaaaaaaa()
#     return Neptune_Error
##########################################################################
"""
 	Description :
		get temperature spread state from a camera (thermal camera only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemOnOff : spread on/off state
		[OUT] pnUserMinTemperature : user min temperature
		[OUT] pnUserMaxTemperature : user max temperature
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetTemperatureSpread(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBoolean* pemOnOff, OUT _int64_t* pnUserMinTemperature, OUT _int64_t* pnUserMaxTemperature);
def ntcGetTemperatureSpread(hCameraHandle, pemOnOff, pnUserMinTemperature, pnUserMaxTemperature):
    Neptune_dll.ntcGetTemperatureSpread.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64)]
    Neptune_Error = Neptune_dll.ntcGetTemperatureSpread(hCameraHandle, pemOnOff, pnUserMinTemperature, pnUserMaxTemperature)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set temperature spread state from a camera (thermal camera only)
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emOnOff : spread on/off control
		[IN] nUserMinTemperature : user min temperature
		[IN] nUserMaxTemperature : user max temperature
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetTemperatureSpread(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emOnOff, IN _int64_t nUserMinTemperature, IN _int64_t nUserMaxTemperature);
def ntcSetTemperatureSpread(hCameraHandle, emOnOff, nUserMinTemperature, nUserMaxTemperature):
    Neptune_dll.ntcSetTemperatureSpread.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.c_int64, ctypes.c_int64]
    Neptune_Error = Neptune_dll.ntcSetTemperatureSpread(hCameraHandle, emOnOff, nUserMinTemperature, nUserMaxTemperature)
    return Neptune_Error
##########################################################################
''' for Cam4 ALT Led System'''
##########################################################################
# NEPTUNE_C_API ENeptuneError __stdcall ntcInitCam4AltLed(IN NeptuneCamHandle hCameraHandle);
# NEPTUNE_C_API ENeptuneError __stdcall ntcUpdateCam4AltLedTable(IN NeptuneCamHandle hCameraHandle, IN _int32_t* piData, IN _int32_t iSize/* 255*64*sizeof(_int32_t) */);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetCam4AltLedIndex(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean bAutoRun, IN _int32_t iStart, IN _int32_t iEnd);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetCam4AltLedDirect(IN NeptuneCamHandle hCameraHandle, IN _int32_t iIndex);
##########################################################################
##########################################################################
''' for Stacked ROI '''
##########################################################################
"""
 	Description :
		get state of stacked roi from a camera 
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemState : enable/disable state
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiControl(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBoolean* pemState);
def ntcGetStackedRoiControl(hCameraHandle, pemState):
    Neptune_dll.ntcGetStackedRoiControl.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiControl(hCameraHandle, pemState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set state of stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] pemState : stacked ROI enable/disable control
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiControl(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emState);
def ntcSetStackedRoiControl(hCameraHandle, emState):
    Neptune_dll.ntcSetStackedRoiControl.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiControl(hCameraHandle, emState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get index of stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiStackedRoiIdx : index of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiSelector(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiStackedRoiIdx);
def ntcGetStackedRoiSelector(hCameraHandle, puiStackedRoiIdx):
    Neptune_dll.ntcGetStackedRoiSelector.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiSelector(hCameraHandle, puiStackedRoiIdx)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set index of stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiStackedRoiIdx : index of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiSelector(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiStackedRoiIdx);
def ntcSetStackedRoiSelector(hCameraHandle, uiStackedRoiIdx):
    Neptune_dll.ntcSetStackedRoiSelector.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiSelector(hCameraHandle, uiStackedRoiIdx)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get state of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] pemState : enable/disable state
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiSelectedEnable(IN NeptuneCamHandle hCameraHandle, OUT ENeptuneBoolean* pemState);
def ntcGetStackedRoiSelectedEnable(hCameraHandle, pemState):
    Neptune_dll.ntcGetStackedRoiSelectedEnable.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiSelectedEnable(hCameraHandle, pemState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set state of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] emState : stacked ROI enable/disable control
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiSelectedEnable(IN NeptuneCamHandle hCameraHandle, IN ENeptuneBoolean emState);
def ntcSetStackedRoiSelectedEnable(hCameraHandle, emState):
    Neptune_dll.ntcSetStackedRoiSelectedEnable.argtypes = [ctypes.c_void_p, ctypes.c_int32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiSelectedEnable(hCameraHandle, emState)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get offset X of selected stacked roi from a camera 
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiOffsetX :  offset X of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiOffsetX(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiOffsetX);
def ntcGetStackedRoiOffsetX(hCameraHandle, puiOffsetX):
    Neptune_dll.ntcGetStackedRoiOffsetX.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiOffsetX(hCameraHandle, puiOffsetX)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set offset X of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiOffsetX :  offset X of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiOffsetX(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiOffsetX);
def ntcSetStackedRoiOffsetX(hCameraHandle, uiOffsetX):
    Neptune_dll.ntcSetStackedRoiOffsetX.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiOffsetX(hCameraHandle, uiOffsetX)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set offset X of all stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiOffsetX : offset X of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiOffsetXAll(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiOffsetX);
def ntcSetStackedRoiOffsetXAll(hCameraHandle, uiOffsetX):
    Neptune_dll.ntcSetStackedRoiOffsetXAll.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiOffsetXAll(hCameraHandle, uiOffsetX)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get width of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiWidth : width of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiWidth(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiWidth);
def ntcGetStackedRoiWidth(hCameraHandle, puiWidth):
    Neptune_dll.ntcGetStackedRoiWidth.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiWidth(hCameraHandle, puiWidth)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set width of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiWidth : width of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiWidth(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiWidth);
def ntcSetStackedRoiWidth(hCameraHandle, uiWidth):
    Neptune_dll.ntcSetStackedRoiWidth.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiWidth(hCameraHandle, uiWidth)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set width of all stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiWidth : width of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiWidthAll(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiWidth);
def ntcSetStackedRoiWidthAll(hCameraHandle, uiWidth):
    Neptune_dll.ntcSetStackedRoiWidthAll.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiWidthAll(hCameraHandle, uiWidth)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get offset Y of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiOffsetY : offset Y of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiOffsetY(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiOffsetY);
def ntcGetStackedRoiOffsetY(hCameraHandle, puiOffsetY):
    Neptune_dll.ntcGetStackedRoiOffsetY.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiOffsetY(hCameraHandle, puiOffsetY)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set offset Y of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiOffsetY : offset Y of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiOffsetY(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiOffsetY);
def ntcSetStackedRoiOffsetY(hCameraHandle, uiOffsetY):
    Neptune_dll.ntcSetStackedRoiOffsetY.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiOffsetY(hCameraHandle, uiOffsetY)
    return Neptune_Error
##########################################################################
"""
 	Description :
		get Height of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[OUT] puiHeight : Height of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetStackedRoiHeight(IN NeptuneCamHandle hCameraHandle, OUT _uint32_t* puiHeight);
def ntcGetStackedRoiHeight(hCameraHandle, puiHeight):
    Neptune_dll.ntcGetStackedRoiHeight.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    Neptune_Error = Neptune_dll.ntcGetStackedRoiHeight(hCameraHandle, puiHeight)
    return Neptune_Error
##########################################################################
"""
 	Description :
		set Height of selected stacked roi from a camera
 	Parameters :
		[IN] hCameraHandle : camera handle to control
		[IN] uiHeight : Height of stacked roi
        
"""
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetStackedRoiHeight(IN NeptuneCamHandle hCameraHandle, IN _uint32_t uiHeight);
def ntcSetStackedRoiHeight(hCameraHandle, uiHeight):
    Neptune_dll.ntcSetStackedRoiHeight.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    Neptune_Error = Neptune_dll.ntcSetStackedRoiHeight(hCameraHandle, uiHeight)
    return Neptune_Error
##########################################################################






##########################################################################
''' Not Supported '''
##########################################################################
# typedef enum _tagENeptuneVideoMode
# {
# 	NEPTUNE_VIDEOMODE_NTSC	= 0,
# 	NEPTUNE_VIDEOMODE_PAL	= 1,
# } ENeptuneVideoMode;
# typedef enum _tagENeptuneAcqFPS
# {
# 	NEPTUNE_FPS_30or25	= 0,
# 	NEPTUNE_FPS_60or50	= 1,
# } ENeptuneAcqFPS;
# typedef enum _tagENeptuneResolution
# {
# 	NEPTUNE_RESOLUTION_1280x720 = 0,
# 	NEPTUNE_RESOLUTION_1920x1080 = 1,
# } ENeptuneResolution;
# typedef enum _tagENeptuneDayNightMode
# {
# 	NEPTUNE_DAYNIGHT_AUTO = 0,
# 	NEPTUNE_DAYNIGHT_COLOR = 1,
# 	NEPTUNE_DAYNIGHT_MONO = 2,
# 	NEPTUNE_DAYNIGHT_EXT = 3,
# } ENeptuneDayNightMode;
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetUserBuffer(NeptuneCamHandle hCamHandle, void* pBuffer, _uint32_t nSize, _uint32_t nCount);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetNTSCPALSelector(NeptuneCamHandle hCamHandle, ENeptuneVideoMode eVideoMode);   
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetNTSCPALSelector(NeptuneCamHandle hCamHandle, ENeptuneVideoMode* peVideMode);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetAcquisitionFrameRateSel(NeptuneCamHandle hCamHandle, ENeptuneAcqFPS eFPS);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAcquisitionFrameRateSel(NeptuneCamHandle hCamHandle, ENeptuneAcqFPS* peFPS);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetAcquisitionFrameRateList(NeptuneCamHandle hCamHandle, ENeptuneAcqFPS* peList, _uint32_t* pnSize);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetResolutionSelector(NeptuneCamHandle hCamHandle, ENeptuneResolution eResolution);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetResolutionSelector(NeptuneCamHandle hCamHandle, ENeptuneResolution* peResolution);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetResolutionList(NeptuneCamHandle hCamHandle, ENeptuneResolution* peList, _uint32_t* pnSize);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetDayNightModeSelector(NeptuneCamHandle hCamHandle, ENeptuneDayNightMode eMode);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetDayNightModeSelector(NeptuneCamHandle hCamHandle, ENeptuneDayNightMode* peMode);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetProfileFeature(NeptuneCamHandle hCamHandle, _ulong32_t* pulLowTh, _ulong32_t* pulHighThr, _ulong32_t* pulMaxDiff, _ulong32_t* pulMinLaserWidth);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetProfileLowThreshold(NeptuneCamHandle hCamHandle, _ulong32_t ulVal);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetProfileHighThreshold(NeptuneCamHandle hCamHandle, _ulong32_t ulVal);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetProfileMaxDifference(NeptuneCamHandle hCamHandle, _ulong32_t ulVal);
# NEPTUNE_C_API ENeptuneError __stdcall ntcSetProfileMinLaserWidth(NeptuneCamHandle hCamHandle, _ulong32_t ulVal);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetProfileMaxLaserWidth(NeptuneCamHandle hCamHandle, _ulong32_t* pulVal);
# NEPTUNE_C_API ENeptuneError __stdcall ntcGetElapsedTimeAfterReceivedLastFrame(NeptuneCamHandle hCamHandle, _uint32_t * pnElapsedTime /*msec*/);    
    
    
    
    
