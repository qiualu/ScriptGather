# coding:utf-8

import win32api
import win32con
import time
import ctypes

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
