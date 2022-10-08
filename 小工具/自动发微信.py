# -*- coding: utf-8 -*-

import win32clipboard as w
import win32con
import win32api
import win32gui
import time
import requests
from lxml import etree


# 把文字放入剪贴板
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


# 模拟ctrl+V
def ctrlV():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, 0, 0)  # V
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟alt+s
def altS():
    win32api.keybd_event(18, 0, 0, 0)
    win32api.keybd_event(83, 0, 0, 0)
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟enter
def enter():
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟单击
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 移动鼠标的位置
def movePos(x, y):
    win32api.SetCursorPos((x, y))


def 找个人发信息(名字="",信息="",debug = 0):
    # 获取鼠标当前位置
    # hwnd=win32gui.FindWindow("MozillaWindowClass",None)
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
    if debug == 1:
        print("hwnd句柄 WeChatMainWndForPC : ",hwnd)
    if hwnd > 0:
        win32gui.SetForegroundWindow(hwnd)  # 激活窗口
    else:
        print("未登录微信")
        return
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    # 获取窗口左上角和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 移动窗口
    # win32gui.MoveWindow(hwnd, 0, 0, 1000, 700, True)
    #获得当前鼠标位置
    mouseX, mouseY = win32api.GetCursorPos()
    if debug == 1:
        print(mouseX, mouseY)

    time.sleep(0.01)
    # 1.移动鼠标到通讯录位置，单击打开通讯录
    movePos(left + 28, top + 147)
    click()
    # 2.移动鼠标到搜索框，单击，输入要搜索的名字
    movePos(left + 148, top + 35)
    click()
    setText(名字)
    ctrlV()
    time.sleep(1)  # 别问我为什么要停1秒，问就是给微信一个反应的时间，他反应慢反应不过来，其他位置暂停的原因同样
    enter()
    time.sleep(1)
    # 3.复制要发送的消息，发送
    setText(信息)
    ctrlV()
    altS()
    # 鼠标移动回原位
    movePos(mouseX, mouseY)


def GetHead():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    return headers

def 获取沙雕文案( url = 'https://api.shadiao.pro/chp'):
    # print("获取彩虹屁")

    # url = 'https://api.shadiao.pro/chp'

    headers = GetHead()

    try:
        response = requests.get(url, headers=headers)
    except BaseException as e:
        return "爱你"
    # res = response.text
    res = response.json()['data']['text']
    return res





if __name__ == "__main__":


    """
        彩虹屁 =	"https://api.shadiao.pro/chp"
        朋友圈文案 =	"https://api.shadiao.pro/pyq"
        毒鸡汤 =	"https://api.shadiao.pro/du"
    """

    彩虹屁 = r"https://api.shadiao.pro/chp"
    朋友圈文案 = r"https://api.shadiao.pro/pyq"
    毒鸡汤 = r"https://api.shadiao.pro/du"

    彩虹 = 获取沙雕文案(彩虹屁)
    # 彩虹 = 获取沙雕文案(朋友圈文案)
    # 彩虹 = 获取沙雕文案(毒鸡汤)

    print("彩虹",彩虹)

    dd = 10
    if 彩虹 != "爱你":
        while dd:
            time.sleep(1)
            print("等待", dd)
            dd -= 1
        找个人发信息('张敏', 彩虹)






# 最近在学习python，发现一个微信自动发消息的小demo感觉很有意思，试了一下，不成功，因为demo中用的是itchat这个库来操作微信，而这个库是通过微信网页版来操作微信的，现在微信网页版已经不能登录了所以失败，我又试了第二种方法，我试图找到微信界面上的搜索框控件，使用搜索框控件找到想法消息的人，然后发送消息，结果就是又失败了，为啥呢？经过我翻翻翻，找找找，发现微信的界面是使用duilib实现的，界面都是画上去的，控件只是逻辑上存在，而实际没有，我们根本获取不到，然后我只能通过手动移动鼠标的方式来实现了
#
# 1.打开微信，固定在左上角，这样便于我们固定微信上各个控件所在坐标
#
# 2.把鼠标移动到微信左边的何柳桦 / light“通讯录”按钮上，单击，打开通讯录
#
# 3.把鼠标移动到搜索框把你要找的人的微信名复制进去，回车，打开对话框（你要问我为什么要先打开通讯录再去搜索框搜？问就是不知道，其实是经过我的实验这样比较稳定，直接搜有bug,如果你能找到其他的解决办法请告诉我，谢谢啦）
#
# 4.把你要发送的话复制到对话框，回车或者alt+s 发送



