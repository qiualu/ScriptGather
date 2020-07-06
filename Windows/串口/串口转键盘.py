# coding:utf-8
import json
import os
import win32api,win32con,win32gui
import time
import win32gui,win32con

import serial
from time import sleep
import time


# print(handle)

# time.sleep(5)
# print(5)
# win32api.SendMessage(handle,win32con.WM_KEYDOWN,'a',0)
# time.sleep(0.01)
# win32api.SendMessage(handle,win32con.WM_KEYUP,'a',0)
# win32api.PostMessage(handle,win32con.WM_CHAR,'c',0);




def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        time.sleep(0.02)
    return data

if __name__ == '__main__':
    TIT = input("请输入标题 : ")
    handle = win32gui.FindWindow(None, TIT)
    Com = input("请输入COM号 : ")
    print("标题 : " ,TIT,"   COM : ",Com)
    serial = serial.Serial(Com, 9600, timeout=0.5)  #/dev/ttyUSB0
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")

    while True:
        data =recv(serial)
        if data != b'' :
            print("收到 receive : ",data)
            # serial.write(data) #数据写回
            win32api.keybd_event(0x0D, handle, 0, 0)








