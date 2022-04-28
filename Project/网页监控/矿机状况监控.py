
import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
import requests
from urllib.request import urlopen

# myURL = urlopen("https://www.runoob.com/")

# -*-coding:utf-8 -*-


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

# 返回一个随机的请求头 headers
def getheaders():
    # 各种PC端
    user_agent_list_2 = [
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
    # 各种移动端
    user_agent_list_3 = [
        # IPhone
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPod
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPAD
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # Android
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # QQ浏览器 Android版本
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # Android Opera Mobile
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        # Android Pad Moto Xoom
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        # BlackBerry
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        # WebOS HP Touchpad
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        # Nokia N97
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        # Windows Phone Mango
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        # UC浏览器
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        # UCOpenwave
        "Openwave/ UCWEB7.0.2.37/28/999",
        # UC Opera
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
    ]
    # 一部分 PC端的
    user_agent_list_1 = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    # user_agent_list = user_agent_list_1 + user_agent_list_2 + user_agent_list_3
    user_agent_list = user_agent_list_1

    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers



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


# headers = getheaders()
#
# # myURL = urlopen(r"https://www.f2pool.com/dcr/DskgMgpmtMgMt9bq6qSCaUDnYUEP6L8cC1h",headers = headers)
# res = requests.get(r"https://ezil.me/personal_stats?wallet=0x3CBC3c9EA6fD4486c94e8Ce4Cd5E6B73A7AeC79e.zil1gjqexhafnm5ljrq5g2cdnk2gtykygmss87wkhc&coin=eth",headers = headers)
#
# # print(myURL.read())
# # print(myURL.getcode())   # 200
# print(res,res.text)


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

url =  r"https://ezil.me/personal_stats?wallet=0x3CBC3c9EA6fD4486c94e8Ce4Cd5E6B73A7AeC79e.zil1gjqexhafnm5ljrq5g2cdnk2gtykygmss87wkhc&coin=eth"



driver = webdriver.Chrome()  # 调用chrome浏览器
# driver.maximize_window() #窗口最大化
driver.get(url) #访问页面如 www.baidu.com
time.sleep(10)  #线程休眠30秒，防止一下打开太多谷歌浏览器

实时算力 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]')
time.sleep(10)  #线程休眠30秒，防止一下打开太多谷歌浏览器

矿机详情 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[2]/div[2]/span/span')[0].click()
time.sleep(10)  #线程休眠30秒，防止一下打开太多谷歌浏览器

矿机列表 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr')
time.sleep(10)  #线程休眠30秒，防止一下打开太多谷歌浏览器

# //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]
# //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]

for i in 矿机列表:
    #找出标签中的文本内容
    name = i.get_attribute('textContent')
    #打印出获取到的文本
    print(name)


找个人发信息('露', "矿机监控开始")


Rx6700 = 矿机列表[1].get_attribute('textContent')
print("监测",Rx6700 ,Rx6700[:8])
if Rx6700[:8] != "Rx6700JL":
    找个人发信息('露', "Rx6700JL矿机掉线")


while True:
    # driver.refresh()
    矿机详情 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[2]/div[2]/span/span')[0].click()
    time.sleep(20)  # 线程休眠30秒，防止一下打开太多谷歌浏览器
    矿机列表 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr')
    time.sleep(3)  # 线程休眠30秒，防止一下打开太多谷歌浏览器

    # //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]
    # //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]

    for i in 矿机列表:
        # 找出标签中的文本内容
        name = i.get_attribute('textContent')
        # 打印出获取到的文本
        print(name)
    print(len(矿机列表))

    Rx6700 = 矿机列表[1].get_attribute('textContent')
    print("监测", Rx6700, Rx6700[:8])
    if Rx6700[:8] != "Rx6700JL":
        print("发送微信消息")
        找个人发信息('露', "Rx6700JL掉线")
    else:
        print("机器在线",Rx6700)
    time.sleep(1200)


driver.quit() #退出谷歌浏览器




