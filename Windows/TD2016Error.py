# coding:utf-8

import json
import os
import win32api,win32con,win32gui
import time
from win32gui import *
import pymouse

titles = set()
def foo(hwnd,mouse):
    #去掉下面这句就所有都输出了，但是我不需要那么多
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        titles.add(GetWindowText(hwnd))
# stus = {'xiaojun':'123456','xiaohei':'7891','abc':'11111'}
# res2 = json.dumps(stus)   #先把字典转成json
# print(res2)
# print(type(res2))

# with open("TDXY.json","w") as f:
#     f.write(res2)

TDx,TDy,Ys = 0,0,10
print(TDx,TDy)

with open("TDXY.json","r",encoding="UTF-8") as f:
    st = f.read()
    res = json.loads(st)
    TDx = res["TDX"]
    TDy = res["TDY"]
    Ys = res["延时启动"]
    TDtime = res["TD启动时间"]

print(TDx,TDy,Ys)
# 1481 1605
TDx,TDy = 645,30
m = pymouse.PyMouse()
def Three_Click():
    # （6）设置鼠标位置
    print(TDx, TDy, Ys)
    win32api.SetCursorPos((TDx, TDy))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # win32api.SetCursorPos((TDx, TDy))
    #m.move(TDx, TDy)
    # m.click(TDx, TDy, 1)
    # m.click(TDx, TDy) #双击
    m.press(TDx, TDy)
    time.sleep(0.2)
    m.release(TDx, TDy)
    # # （2）鼠标左键按下
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # time.sleep(0.05)
    # # （3）鼠标左键放开
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    # time.sleep(0.08)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # time.sleep(0.05)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    # time.sleep(0.3)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # time.sleep(0.05)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def get_windows_title():
    EnumWindows(foo, 0)
    lt = [t for t in titles if t]
    lt.sort()
    for t in lt:
        if t == "Fatal Error" or t == "TouchDesigner" or t == "TouchDesigner Error":
            print("Show ErrorWindows : **** ",t)
            return 1
    for t in lt:

        #print(t)
        # if t == "/perform":
        #     return 0
        #if ("perform" in t) or t == "/perform":

        if t == "/perform":
            print("***  OK windows : *** ", t)
            return 0
    print("***  Null windows  *** ")
    return 1



# 正常   /perform
# TouchDesigner
# Fatal Error

start = time.time() + 600

try:
    # time.sleep(Ys)
    print("ClickThree")
    while True:
        endTime = time.time()
        Three_Click()
        print(" 等待启动 ... ")
        time.sleep(TDtime)
        print(" 查看启动情况 ")
        a = get_windows_title()
        if a == 0:
            break
        else:
            print("Kill TD")
            # os.system('taskkill /f /im TouchDesigner099.exe')
            # os.system('taskkill /f /im TouchDesigner099.exe')
            # time.sleep(2)
            # os.system('taskkill /f /im TouchDesigner099.exe')
            # os.system('taskkill /f /im TouchDesigner099.exe')
            os.system('taskkill /f /im TouchPlayer099.exe')
            time.sleep(2)
            os.system('taskkill /f /im TouchPlayer099.exe')

        if endTime > start:
            os.system("shutdown -r -t 1")

    # time.sleep(60)
    #
    # a = get_windows_title()
    # if a == 1:
    #     os.system("shutdown -r -t 1")

    handle = win32gui.FindWindow(None, "/perform")
    win32gui.SetForegroundWindow(handle)

except EnvironmentError:
    print("我真的好南Error",EnvironmentError)


print("yes wancheng ")

# print(st,type(st))
#
# print(res)  # 打印字典
# print(type(res))  #打印res类型
# print(res.keys())  #打印字典的所有key
# print(res["TDX"])
# print("kaiji")
# 722 126
# import os
# os.system('taskkill /f /im TouchDesigner099.exe')






