# coding:utf-8

import win32api
import win32con
import time
import ctypes

print("  start   驱动级 模拟键盘按键  ")
# 按键虚拟码
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
# 数字小键盘的键
key_xia_o = {
    "0": 0x60, "1": 0x61, "2": 0x62, "3": 0x63, "4": 0x64, "5": 0x65, "6": 0x66, "7": 0x67, "8": 0x68, "9": 0x69,
    "*": 0x6a, "+": 0x6b, "Enter": 0x6c, "-": 0x6d, ".": 0x6e, "/": 0x6f,
             }

# 模拟按键按下抬起的方法：

def keydownup(num):
    MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    #time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    #time.sleep(0.02)
    win32api.keybd_event(num, MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0)

    # 其中MapVirtualkey是扫描码,一般不使用这个，如果要制作控制游戏人物的脚本时一定要填入扫描码才能在游戏中实现硬件级键盘模拟。
    # 方法很简单
    # win32api.keybd_event(虚拟码，扫描码，0，0）
    # 第一个参数是虚拟码有一些是不太一样的，需要自己根据自己的电脑测出相关的虚拟码，其中一些虚拟码，
    # 第二个参数是扫描码，如果一个一个去寻找扫描码会很麻烦，可以像我那样，在方法开始处或者程序起始处添加这么一句
    # 然后就可以传入虚拟码来寻找相应的扫描码
    # MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    # 第三个是参数是作为判断按下与抬起的标识，按下时为0即可，因为键盘的全过程是按下与抬起，所有两个keybd_event才是一个完整的过程，其中一定要给其中添加一个时间暂停的，不然还是无法使用，即使在操作台或者pycharm上可以输入，在游戏中便没有效果了，时间自己可以传参数进去，也可以规定一个固定的值，这个时间便是你按住的时间

# li = [chr(i) for i in range(ord("A"),ord("Z")+1)]
time.sleep(3)
# for i in li:
#     print(i)
#     keydownup(key_num[i])

keydownup(0x1)
keydownup(0x1)
keydownup(0x1)
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz




# 待考究

"""

值 描述
0x1 鼠标左键
0x2 鼠标右键
0x3 CANCEL 键
0x4 鼠标中键
0x8 BACKSPACE 键
0x9 TAB 键
0xC CLEAR 键
0xD ENTER 键
0x10 SHIFT 键
0x11 CTRL 键
0x12 MENU 键
0x13 PAUSE 键
0x14 CAPS LOCK 键
0x1B ESC 键
0x20 SPACEBAR 键
0x21 PAGE UP 键
0x22 PAGE DOWN 键
0x23 END 键
0x24 HOME 键
0x25 LEFT ARROW 键
0x26 UP ARROW 键
0x27 RIGHT ARROW 键
0x28 DOWN ARROW 键
0x29 SELECT 键
0x2A PRINT SCREEN 键
0x2B EXECUTE 键
0x2C SNAPSHOT 键
0x2D INSERT 键
0x2E DELETE 键
0x2F HELP 键
0x90 NUM LOCK 键

"""
