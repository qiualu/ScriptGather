#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))
s.send(bytes("你好",encoding="utf-8"))
s.send(bytes("你23456好",encoding="utf-8"))
print(str(s.recv(1024),encoding="utf-8"))

while True:
    a = input("你好,请输入 : ")
    if a == "z":
        break
    else:
        s.send(bytes(a, encoding="utf-8"))

s.close()