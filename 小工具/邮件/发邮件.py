

import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header


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


Mail_qq("第一次测试通道开启")

