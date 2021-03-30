
import win32gui,win32con
import time

time.sleep(1)

wrHd=win32gui.FindWindow(None, '/perform')
win32gui.ShowWindow(wrHd,win32con.SW_SHOWNORMAL)
win32gui.SetForegroundWindow(wrHd)
# 1212121212121212121111111111111112
print(wrHd)