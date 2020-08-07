#! /usr/bin/env python
# coding=utf-8

#! /usr/bin/env python
# coding=utf-8

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#判断是否静音，mute为1代表是静音，为0代表不是静音
mute = volume.GetMute()

#获取音量值，0.0代表最大，-65.25代表最小
vl = volume.GetMasterVolumeLevel()

#获取音量范围，我的电脑经测试是(-65.25, 0.0, 0.03125)，第一个应该代表最小值，第二个代表最大值，第三个不知道是干嘛的。也就是音量从大到小是0.0到-65.25这个范围
vr = volume.GetVolumeRange()
print(vl,vr)
#设置音量, 比如-13.6代表音量是40，0.0代表音量是100

# print(vr[0],vr[1])
# x = 98
# Yl =vr[0] + (x * ((vr[1] - vr[0]) / 100))
# print(Yl)
# volume.SetMasterVolumeLevel(Yl, None)



import ctypes
import tkinter

winmm=ctypes.wind11.winmm
user32=ctypes.wind11.user32

WM_APPCOMMAND=0x319

APPCOMMAND_VOLUME_UP=0X0a0000
APPCOMMAND_VOLUME_DOWN=0X090000
APPCOMMAND_VOLUME_MUTE =0x080000


#增加音量，每次增加2%
def volume_up():
    hwnd = user32.GetForegroundWindow()
    user32.PostMessageA(hwnd,WM_APPCOMMAND,0,APPCOMMAND_VOLUME_UP)


volume_up()














