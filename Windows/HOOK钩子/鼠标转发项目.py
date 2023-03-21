import win32api
import win32con
import win32gui
import pythoncom
import pyHook
import threading

def on_mouse_event(event):
    if event.MessageName == 'mouse left down':
        # 防止将鼠标事件传递给其他程序
        return -1
    # 如果不是鼠标左键按下事件，则返回None，将事件传递给其他程序
    return None

def stop_hooking():
    # 停止全局鼠标钩子
    hm.UnhookMouse()
    print('Stopped hooking after 5 seconds.')

# 创建全局鼠标钩子
hm = pyHook.HookManager()
hm.MouseAll = on_mouse_event
hm.HookMouse()

# 启动一个定时器，在5秒后调用stop_hooking函数停止拦截
timer = threading.Timer(5, stop_hooking)
timer.start()

# 进入消息循环
pythoncom.PumpMessages()
