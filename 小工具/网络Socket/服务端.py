#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    c.send(bytes('欢迎服务器！',encoding='utf-8'))
    while True:
        data = c.recv(1024)  # 接收数据
        print(str(data, encoding="utf-8"))

        if data == "关机":
            print("结束服务器,开始关机")
            break

    c.close()  # 关闭连接
    break
