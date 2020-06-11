# coding:utf-8

import win32api
import win32con,win32com
import time
import ctypes

VK_CODE = {
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
# 一、pywin32常用函数
# （1）获取鼠标位置
win32api.GetCursorPos()
#
# （2）鼠标左键按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#
# （3）鼠标左键放开
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#
# （4）鼠标右键按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

# （5）鼠标右键放开
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# （6）设置鼠标位置
win32api.SetCursorPos((x, y))

# （7）键盘输入事件
word = 'a'
win32api.keybd_event(VK_CODE[word], 0, 0, 0)
win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)


# 二、封装接口
# （1）获取当前鼠标位置
class mouseClass():
    def cursor_point(self):
            """
             获取当前鼠标位置
            """
            pos = win32api.GetCursorPos()
            return int(pos[0]), int(pos[1])

        # （2）鼠标左击事件
    def mouse_left_click(self, new_x=None, new_y=None, times=1):
        """
            鼠标左击事件
            :param new_x: 新移动的坐标x轴坐标
            :param new_y: 新移动的坐标y轴坐标1506240215
            :param times: 点击次数
            """
        self.mouse_move(new_x, new_y)
        time.sleep(0.05)
        while times:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            times -= 1

    # （3）鼠标右击事件
    def mouse_right_click(self, new_x=None, new_y=None):
        """
        鼠标右击事件
        :param new_x: 新移动的坐标x轴坐标
        :param new_y: 新移动的坐标y轴坐标
        """
        self.mouse_move(new_x, new_y)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # （4）移动鼠标位置
    def mouse_move(self, new_x, new_y):
        if new_y is not None and new_x is not None:
            point = (new_x, new_y)
            win32api.SetCursorPos(point)
            self.x = new_x
            self.y = new_y

    # （5）键盘输入文本
    def key_input(self, input_words=''):
        for word in input_words:
            win32api.keybd_event(VK_CODE[word], 0, 0, 0)
            win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.1)

    # （6）键盘输入事件
    def key_even(self, input_key):
        win32api.keybd_event(VK_CODE[input_key], 0, 0, 0)
        win32api.keybd_event(VK_CODE[input_key], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
