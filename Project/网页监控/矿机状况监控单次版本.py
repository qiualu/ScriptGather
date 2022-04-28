# -*-coding:utf-8 -*-

import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
import requests
from urllib.request import urlopen



import win32clipboard as w
import win32con
import win32api
import win32gui
import time
import requests
from lxml import etree




import random
from selenium import webdriver
import time


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


def 找个人发信息(名字="",信息=""):
    # 获取鼠标当前位置
    # hwnd=win32gui.FindWindow("MozillaWindowClass",None)
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

    # 获取窗口左上角和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 移动窗口
    # win32gui.MoveWindow(hwnd, 0, 0, 1000, 700, True)
    #获得当前鼠标位置
    mouseX, mouseY = win32api.GetCursorPos()
    #print(mouseX, mouseY)
    if hwnd > 0:
        try:
            win32gui.SetForegroundWindow(hwnd)  # 激活窗口
        except:
            print("激活 出错")
    else:
        print("未登录微信")
        return
    time.sleep(0.01)
    # 1.移动鼠标到通讯录位置，单击打开通讯录
    movePos(left + 28, top + 147)
    click()
    # 2.移动鼠标到搜索框，单击，输入要搜索的名字
    movePos(left + 148, top + 35)
    click()
    #setText('张敏/zxc')
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

def 获取彩虹屁():
    # print("获取彩虹屁")

    url = 'https://chp.shadiao.app/api.php'

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    res = response.text

    return res

# 口吐莲花
def 获得祖安问候():
    # https: // zuanbot.com /
    # print("获取彩虹屁")
    # url = 'https://chp.shadiao.app/api.php'
    #  https://zuanbot.com/api.php?level=min&lang=zh_cn
    url = 'https://zuanbot.com/api.php?level=min&lang=zh_cn'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    head = {
    "accept": "* / *",
    "accept - encoding": "gzip, deflate, br",
    "accept - language": "zh - CN, zh; q = 0.9",
    "referer": "https: // zuanbot.com /",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.141Safari / 537.36",
    "x-requested-with": "XMLHttpRequest"
    }
    response = requests.get(url, headers=head)
    res = response.text
    print(res)
    return res



def Mail_qq(mail_content):

    # 发信方：qq邮箱
    sender_qq = '1626816865@qq.com'
    # 发信方：邮箱授权码
    authorization_code = 'dqiqxalbobcxbjea'

    # 设置收信方邮箱
    # receiver_qq = '494436488@qq.com'
    receiver_qq = '1626816865@qq.com'
    # 设置发信服务器
    pop_smtp = 'smtp.qq.com'

    '''邮箱发送的内容：
            mail_content：参数为发送的正文内容，
            plain：参数为设置格式(plain 为纯文本)，
            utf-8：参数为正文的编码'''
    open_values = MIMEText(mail_content, 'plain', 'utf-8')

    # 设置邮件中头部显示的内容
    open_values['From'] = Header(sender_qq)
    open_values['To'] = Header(receiver_qq)
    open_values['Subject'] = Header('自动化执行结果')

    # 开启发信的服务，传输方式为加密传输
    open_get = smtplib.SMTP_SSL(pop_smtp)
    open_get.connect(pop_smtp, 465)

    # 登录发信邮箱
    open_get.login(sender_qq, authorization_code)
    # 发送邮件
    open_get.sendmail(sender_qq, receiver_qq, open_values.as_string())
    # 关闭服务器
    open_get.quit()


def 查询矿机情况():

    url =  r"https://ezil.me/personal_stats?wallet=0x3CBC3c9EA6fD4486c94e8Ce4Cd5E6B73A7AeC79e.zil1gjqexhafnm5ljrq5g2cdnk2gtykygmss87wkhc&coin=eth"

    driver = webdriver.Chrome()  # 调用chrome浏览器
    # driver.maximize_window() #窗口最大化
    driver.minimize_window()  #窗口最小化
    driver.get(url) #访问页面如 www.baidu.com
    time.sleep(30)  #线程休眠30秒，防止一下打开太多谷歌浏览器
    # 实时算力 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]')
    实时算力 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[4]/section/section[2]/section[2]/article[2]/div/article[1]/div/p[1]')
                                            #'//*[@id="__next"]/div/div[4]/section/section[2]/section[2]/article[2]/div/article[1]/div/p[1]'
    try:
        data = float(实时算力[0].get_attribute('textContent'))
    except EnvironmentError as e:
        print("转换算力异常",e)
        driver.quit()  # 退出谷歌浏览器
        return
    print("实时算力", data , 实时算力, type(实时算力))
    if data < 500:
        sendXh = "算力降低过多 - " + str(data)
        print("sendXh :  ",sendXh  ,type(sendXh),type(data))
        找个人发信息('露', sendXh)
    else:
        print("算力打表")

    time.sleep(10)  # 线程休眠30秒，防止一下打开太多谷歌浏览器

time.sleep(2)
print("send 开始监控")
找个人发信息('露', "开始监控")
while True:
    try:
        查询矿机情况()
        time.sleep(1200)
    except EnvironmentError as e:
        print("本轮查询出错",e)





# while True:
#     # driver.refresh()
#     矿机详情 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[2]/div[2]/span/span')[0].click()
#     time.sleep(20)  # 线程休眠30秒，防止一下打开太多谷歌浏览器
#     矿机列表 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr')
#     time.sleep(3)  # 线程休眠30秒，防止一下打开太多谷歌浏览器
#
#     # //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]
#     # //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]
#
#     for i in 矿机列表:
#         # 找出标签中的文本内容
#         name = i.get_attribute('textContent')
#         # 打印出获取到的文本
露
开始监控#     print(len(矿机列表))
#
#     Rx6700 = 矿机列表[1].get_attribute('textContent')
#     print("监测", Rx6700, Rx6700[:8])
#     if Rx6700[:8] != "Rx6700JL":
#         print("发送微信消息")
#         找个人发信息('露', "Rx6700JL掉线")
#     else:
#         print("机器在线",Rx6700)
#     time.sleep(1200)







