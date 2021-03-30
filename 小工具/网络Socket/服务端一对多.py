
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket 模块
import threading




class MainGui(object):
    def __init__(self):
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12345  # 设置端口
        s.bind((host, port))  # 绑定端口

        s.listen(5)  # 等待客户端连接
    def btn2_def(self):

        t = threading.Thread(target=self.whileRunnum, name='funciton')
        t.start()

from socket import *
import threading

import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息
    tcp_server_socket.bind(('', 1234))

    # 3.让默认的套接字变为被动 listen
    tcp_server_socket.listen(128)

    while True:    # 为多个客户端服务
        # 4.等待客户的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        try:
            while True:    # 为这个客户多次服务
                # 5.接受客户段发过来的请求
                recv_data = new_client_socket.recv(1024)
                print(recv_data, recv_data.decode('gbk'))#前面传递回来的是bytes类型， 后面进行解码

                if recv_data:
                    # 6.回送一部分数据给客户端
                    new_client_socket.send('It\'s ok'.encode('utf-8'))
                else:
                    print('已经为这个客户端服务完毕')
                    break
        except EnvironmentError as e:
            print("用户主动断开连接")
        # 7.关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()




