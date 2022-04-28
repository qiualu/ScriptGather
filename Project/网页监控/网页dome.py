# -*-coding:utf-8 -*-

import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

from selenium import webdriver
import time



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
time.sleep(30)  #线程休眠30秒，防止一下打开太多谷歌浏览器

实时算力 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]')
time.sleep(30)  #线程休眠30秒，防止一下打开太多谷歌浏览器

矿机详情 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[2]/div[2]/span/span')[0].click()
time.sleep(30)  #线程休眠30秒，防止一下打开太多谷歌浏览器

矿机列表 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr')
time.sleep(30)  #线程休眠30秒，防止一下打开太多谷歌浏览器

# //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]
# //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]

for i in 矿机列表:
    #找出标签中的文本内容
    name = i.get_attribute('textContent')
    #打印出获取到的文本
    print(name)


while True:

    矿机列表 = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr')
    time.sleep(30)  # 线程休眠30秒，防止一下打开太多谷歌浏览器

    # //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]
    # //*[@id="__next"]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]

    for i in 矿机列表:
        # 找出标签中的文本内容
        name = i.get_attribute('textContent')
        # 打印出获取到的文本
        print(name)
    print(len(矿机列表))

    if len(矿机列表) < 8:


    time.sleep(1200)

driver.quit() #退出谷歌浏览器




