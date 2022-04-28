import win32gui

handle = win32gui.FindWindow("Shell_TrayWnd", None)
print(handle)
if handle != 0:
    # 显示窗口
    win32gui.ShowWindow(handle, 1)
    # 隐藏窗口
    # win32gui.ShowWindow(handle, 0)
