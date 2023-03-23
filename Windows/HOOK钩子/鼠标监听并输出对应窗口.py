import win32gui
from pynput.mouse import Listener
def on_click(x, y, button, pressed):
    if button == button.left:
        if pressed:
            # 获取鼠标指针当前所在的窗口句柄
            hwnd = win32gui.WindowFromPoint((x, y))
            # 获取窗口标题
            title = win32gui.GetWindowText(hwnd)
            # 获取窗口类名
            classname = win32gui.GetClassName(hwnd)
            print('Left mouse button pressed at ({0}, {1}) in window {2} ({3})'.format(x, y, title, classname))

with Listener(on_click=on_click) as listener:
    listener.join()
