# coding:utf-8
import json
import os
import win32api,win32con,win32gui
import time
import win32gui,win32con

handle = win32gui.FindWindow(None, "*桌面图像处理.txt - 记事本")
print(handle)
win32gui.SetForegroundWindow(handle)  #激活窗口
time.sleep(5)
print(5)
# win32api.SendMessage(handle,win32con.WM_KEYDOWN,'a',0)
# time.sleep(0.01)
# win32api.SendMessage(handle,win32con.WM_KEYUP,'a',0)
# win32api.PostMessage(handle,win32con.WM_CHAR,'c',0);

win32api.keybd_event(0x0D, handle, 0, 0)
