# coding:utf-8
import win32gui,win32con,win32api,ctypes
import time

key_num = {
    # 字母和数字键　
    "a": 0x41, "b": 0x42, "c": 0x43, "d": 0x44, "e": 0x45, "f": 0x46, "g": 0x47, "h": 0x48, "i": 0x49, "j": 0x4a, "k": 0x4b, "l": 0x4c, "m": 0x4d, "n": 0x4e, "o": 0x4f, "p": 0x50, "q": 0x51, "r": 0x52, "s": 0x53, "t": 0x54, "u": 0x55, "v": 0x56, "w": 0x57, "x": 0x58, "y": 0x59, "z": 0x5a,
    "A": 0x41, "B": 0x42, "C": 0x43, "D": 0x44, "E": 0x45, "F": 0x46, "G": 0x47, "H": 0x48, "I": 0x49, "J": 0x4a, "K": 0x4b, "L": 0x4c, "M": 0x4d, "N": 0x4e, "O": 0x4f, "P": 0x50, "Q": 0x51, "R": 0x52, "S": 0x53, "T": 0x54, "U": 0x55, "V": 0x56, "W": 0x57, "X": 0x58, "Y": 0x59, "Z": 0x5a,
    "0": 0x30, "1": 0x31, "2": 0x32, "3": 0x33, "4": 0x34, "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39,
    # 数字小键盘的键
    "*": 0x6a, "+": 0x6b, "-": 0x6d, ".": 0x6e, "/": 0x6f,
    # 功能键
    "F1": 0x70, "F2": 0x71, "F3": 0x72, "F4": 0x73, "F5": 0x74, "F6": 0x75, "F7": 0x76, "F8": 0x77, "F9": 0x78, "F10": 0x79, "F11": 0x7a, "F12": 0x7b,
    # 其它键
    "Left Arrow": 0x25, "End": 0x23, "Page Up": 0x21, "Backspace": 0x8, "Up Arrow": 0x26, "Page Down": 0x22, "Caps Lock": 0x14, "Insert": 0x2d, "Shift": 0x10, "Clear": 0xc, "Num Lock": 0x90, "Enter": 0xd, "Esc": 0x1b, "Spacebar": 0x20, "Delete": 0x2e, "Control": 0x11, "Right Arrow": 0x27, "Help": 0x2f, "Down Arrow": 0x28, "Tab": 0x9, "Home": 0x24, "Alt": 0x12,
}

handle = win32gui.FindWindow(None, "Resolume Arena - Example (1280 x 720)")
print(handle)
def keydownup(num):
    MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    #time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    #time.sleep(0.02)
    win32api.keybd_event(num, MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0)

#parent为父窗口句柄id
def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList
zi = get_child_windows(handle)[0]

print(get_child_windows(zi))
win32gui.SetForegroundWindow(handle)  #激活窗口
# ----------------------------------  发送窗口信息 ----------------------------------------------------
# win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)
# time.sleep(3)
# win32gui.PostMessage(zi, win32con.WM_KEYDOWN, 'q', 0)
# win32gui.PostMessage(zi, win32con.WM_KEYUP, 'q', 0)
win32gui.SetForegroundWindow(handle) # //根据句柄将窗口放在最前
keydownup(key_num["q"])
time.sleep(3)
keydownup(key_num["w"])
time.sleep(3)
keydownup(key_num["e"])
# keydownup(key_num["2"])
# win32api.SendMessage(handle,win32con.WM_KEYDOWN,'a',0)
# time.sleep(0.01)
# win32api.SendMessage(handle,win32con.WM_KEYUP,'a',0)
# win32api.PostMessage(handle,win32con.WM_CHAR,'c',0);

#---------------------------------- 获得窗口大小 ---------------------------------------------------------
left, top, right, bottom = win32gui.GetWindowRect(handle)
print(left , top, right, bottom)
#---------------------------------- 移动 left, top, 设置大小 right, bottom ||  置顶---------------------------------------------------------
win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, left, top, right, bottom, win32con.SWP_SHOWWINDOW)








