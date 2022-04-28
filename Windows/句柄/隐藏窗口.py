

# 获得句柄
import win32gui,win32con


def show():
    # windows handlers
    hwnd = handle
    win32gui.SetForegroundWindow(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 1000, 1000, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW)

def hide(handle):

    # windows handlers
    hwnd = handle
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_HIDEWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER)


import  time

a = 0

while True:
    try:
        handle = win32gui.FindWindow(None, "Fatal Error")
        print("当前Fatal Error句柄",handle)
        hide(handle)
    except:
        time.sleep(30)
        a += 1
        print("没有",a)
        if a > 2000:
            break
# show()













