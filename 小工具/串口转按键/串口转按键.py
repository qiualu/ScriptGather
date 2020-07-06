# coding:utf-8
import json
import os
import win32api
import time,ctypes
import win32gui,win32con
import serial
import sys


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
def keydownup(num):
    MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    #time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    #time.sleep(0.02)
    win32api.keybd_event(num, MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0)

class serial_change_key():
    def __init__(self):
        self.get_json()
        self.handle = win32gui.FindWindow(None, self.title)
        print("窗口句柄",self.handle)
        self.sk = self.res["串口转按键"]
        self.open_serial()


    def open_serial(self):
        import serial
        print("打开串口")
        try:
            self.serial = serial.Serial(self.com, 9600, timeout=0.5)  # /dev/ttyUSB0
        except EnvironmentError:
            print("串口打开失败",EnvironmentError)
            exec(sys.exit())
        if self.serial.isOpen() :
            print("串口",self.com,"打开成功")
        else :
            print("串口",self.com,"打开失败")

    def get_json(self):
        print("读取配置文件")
        with open("配置文件.txt", "r", encoding="UTF-8") as f:
            st = f.read()
            self.res = json.loads(st)
            self.title = self.res["title"]
            self.com = self.res["com"]
            print(self.res)
            # return res

    def dianji(self,chuankou):
        wd = int.from_bytes(chuankou, byteorder='big', signed=False)
        if self.handle:
            for key in self.sk:
                if wd == self.sk[key]:
                    print("send -> ", self.handle,key)
                    try:
                        win32gui.SetForegroundWindow(self.handle)  # //根据句柄将窗口放在最前
                    except:
                        print("窗口ExSetForegroundWindow")
                    keydownup(key_num[key])
        else:
            self.handle = win32gui.FindWindow(None, self.title)

    def recv(self):
        while True:
            data = self.serial.read_all()
            if data == '':
                continue
            else:
                break
            time.sleep(0.02)
        return data

    def while_xx(self):
        print("开始接受串口信息")
        while True:
            data = self.recv()
            # print("")
            if data == b'\xf4':
                print("关机")
                os.system("shutdown -s -t 2")
            elif data != b'':
                self.dianji(data)
                print("收到信号 : ",data,int.from_bytes(data, byteorder='big', signed=False))



if __name__ == '__main__':
    zs = serial_change_key()
    zs.while_xx()
