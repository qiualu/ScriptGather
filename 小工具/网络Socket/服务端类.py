# encoding=utf-8
# auther：lsj
# 服务端

from multiprocessing import Process
from threading import Thread
import socket

"""
服务端的三个条件：
    1、有固定的IP和PORT。
    2、24小时不间断提供服务。
    3、能够支持并发。
"""
server = socket.socket()  # 括号内不加参数默认就是TCP协议
host = socket.gethostname()  # 获取本地主机名
port = 8080  # 设置端口
server.bind((host, port))  # 绑定端口
server.listen(5)


# 将服务的代码单独封装成一个函数
def talk(conn):
    # 通讯循环
    print('开启客户端服务线程 ',conn)
    while True:
        try:
            data = conn.recv(1024)
            # 针对mac linux客户端断开链接后
            if len(data) == 0:break
            print(data.decode('utf8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()

# 链接循环

while True:
    print("等待链接")
    conn, addr = server.accept()  # 接客
    print('连接地址：', addr)
    # t = Thread(target=talk,args=(conn,)) # 叫其他人来服务客户(线程版)
    t = Process(target=talk,args=(conn,))  # 叫其他人来服务客户(线程版)
    t.start()






