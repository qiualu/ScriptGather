# coding:utf-8

import json
import os
import win32api,win32con,win32gui
import time,random
from win32gui import *
from pymouse import PyMouse

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
print("start ",TDx,TDy,Ys)

with open("TDXY.json", "r", encoding="UTF-8") as f:
    st = f.read()
    res = json.loads(st)
    TDx = res["TDX"]
    TDy = res["TDY"]
    Ys = res["延时启动"]
    TDtime = res["TD启动时间"]
    TDgvTouchDesigner = res["过滤TouchDesigner"]
    TDgvFatalError = res["过滤FatalError"]




print("起始参数 : ",TDx,TDy,Ys,TDtime)
# 1481 1605
# TDx,TDy = 645,30

def ClickMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def Three_Click(a = 0):
    # （6）设置鼠标位置
    print("操作 : ",TDx, TDy,a)
    win32api.SetCursorPos((TDx, TDy))
    print("点击 01")

    # m = PyMouse()
    # m.click(TDx, TDy)
    # m.click(TDx, TDy)
    # time.sleep(0.5)
    # m.click(TDx, TDy)

    # m.click(TDx, TDy, 1)  # (x坐标，y坐标，左键，点击次数)
    # time.sleep(0.5)

    ClickMouse()
    ClickMouse()
    time.sleep(0.5)
    ClickMouse()



def get_windows_title():
    print("窗口检测_start")
    EnumWindows(foo, 0)
    lt = [t for t in titles if t]
    lt.sort()

    # for t in lt:
    #     print("所有窗口之 : ", t)

    for t in lt:
        if t == "Fatal Error" or t == "TouchDesigner":
            print("处理窗口KillTD  : ", t)
            return 1
    for t in lt:
        print("处理窗口 : ",t)
        # if t == "/perform":
        #     return 0
        if ("perform" in t) or t == "/perform" or ("perform" in str(t)):
            print("完成启动 : ", t)
            return 0
    return 1


# 正常   /perform
# TouchDesigner
# Fatal Error
time.sleep(Ys)
start = time.time() + 600
qihua = 0
try:
    # time.sleep(Ys)
    print("ClickThree")
    while True:
        endTime = time.time()

        Three_Click(qihua)
        qihua += 1
        if qihua > 4:
            qihua = 0

        print(" 等待启动 ... ")
        time.sleep(TDtime)
        print(" 查看启动情况 ")
        a = get_windows_title()
        if a == 0:
            break
        else:
            print("Kill TD")
            performhandle = win32gui.FindWindow(None, "/perform")
            FatalErrorhandle = win32gui.FindWindow(None, "Fatal Error")
            TouchDesignerhandle = win32gui.FindWindow(None, "TouchDesigner")
            print("/perform TD handle : ",performhandle,"Fatal Error TD handle : ", FatalErrorhandle,"TouchDesigner TD handle : ", TouchDesignerhandle)
            if performhandle and not((TDgvTouchDesigner and TouchDesignerhandle) or (TDgvFatalError and FatalErrorhandle)):
                print("过滤Kill 结束任务")
                break
            else:
                # os.system('taskkill /f /im TouchDesigner099.exe')
                os.system('taskkill /f /im TouchDesigner099.exe')
                time.sleep(2)
                os.system('taskkill /f /im TouchDesigner099.exe')
                # os.system('taskkill /f /im TouchDesigner099.exe')
                os.system('taskkill /f /im TouchPlayer099.exe')
                time.sleep(2)
                os.system('taskkill /f /im TouchPlayer099.exe')


        print("计时 : ",start - endTime,"s")
        if endTime > start:
            os.system("shutdown -r -t 1")

    # time.sleep(60)
    #
    # a = get_windows_title()
    # if a == 1:
    #     os.system("shutdown -r -t 1")

    handle = win32gui.FindWindow(None, "/perform")
    win32gui.SetForegroundWindow(handle)

except:
    print("未知Error")


print("结束任务")

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






