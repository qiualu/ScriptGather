import socket
import configparser
import time
import pyautogui
def read_ini():
    #实例化一个configparser对象
    config = configparser.ConfigParser()
    #path为ini文件的存放路径，最好为绝对路径，获取文件绝对路径的方法，另有文详细描述
    config.read("配置文件.ini", encoding='utf8')
    return config

pz = read_ini()
ip1 = pz['host']['ipsend1']
ip2 = pz['host']['ipsend2']
ip3 = pz['host']['ipsend3']
ip4 = pz['host']['ipsend4']
pcip = pz['host']['pcip']
port = int(pz['host']['port'])
cPCID = int(pz['host']['cPCID'])
portTD = int(pz['host']['portTD'])



ip_portClient1 = (ip1, port)
ip_portClient2 = (ip2, port)
ip_portClient3 = (ip3, port)
ip_portClient4 = (ip4, port)
iplist = [ip_portClient1,ip_portClient2,ip_portClient3,ip_portClient4]
ip14 = [ip1,ip2,ip3,ip4]
SC = int(pz['host']['SC'])
PCID = int(pz['host']['PCID'])
if SC == 1:
    PC = PCID

zt = "f0x1"
pcx = 1


BUFSIZE = 1024
ip_port = ('127.0.0.1', 1001)

ip_portclient = (pcip, port)

ip_zl = ('127.0.0.1', 7000)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def seletPC(index):
    global zt,pcx
    if index == PCID:
        client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)
        zt = "f0x1"
        pcx = PCID
        time.sleep(1)
    elif index == 1:
        client.sendto("f1x1,100,100".encode('utf-8'), ip_zl)
        zt = "f1x1"
        pcx = 1
        # 发给单片机
        client.sendto("arduino,1,1".encode('utf-8'),('127.0.0.1', portTD))
        time.sleep(1)
    elif index == 2:
        client.sendto("f1x1,100,100".encode('utf-8'), ip_zl)
        zt = "f1x1"
        pcx = 2
        # 发给单片机
        client.sendto("arduino,2,1".encode('utf-8'), ('127.0.0.1', portTD))
        time.sleep(1)
    elif index == 3:
        client.sendto("f1x1,100,100".encode('utf-8'), ip_zl)
        zt = "f1x1"
        pcx = 3
        # 发给单片机
        client.sendto("arduino,3,1".encode('utf-8'), ('127.0.0.1', portTD))
        time.sleep(1)
    elif index == 4:
        client.sendto("f1x1,100,100".encode('utf-8'), ip_zl)
        zt = "f1x1"
        pcx = 4
        client.sendto("arduino,4,1".encode('utf-8'), ('127.0.0.1', portTD))
        # 发给单片机
        time.sleep(1)

def seletclientPC(index):
    global zt
    if PCID == index:
        client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)
        zt = "f0x1"
        return
    else:
        sendDate = "client,"+str(index)+",0,0"
        client.sendto(sendDate.encode('utf-8'), (ip14[index-1],1001))
        zt = "f0x1"
        client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)

def ServerRun():
    global zt,pcx
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
    server.bind(ip_port)
    a = 0
    sj = 0
    jgTime = 5
    while True:
        data, client_addr = server.recvfrom(BUFSIZE)
        zl = data.decode().split(",")
        # server.sendto(data.upper(), client_addr)
        x = int(float(zl[1]))
        y = int(float(zl[2]))
        # print('server收到的数据',type(zl[2]),y, zl)
        # client.sendto(data, ip_portClient1)
        if zl[0] == "mouse":
            if zt == "f0x1":
                # print(" 打开过度动画 sj ", time.time()-sj)
                if time.time()-sj > jgTime:
                    print(" 打开选项 sj ", sj)
                    sj = time.time()
                    client.sendto("f0p1,100,100".encode('utf-8'), ip_zl)
                    zt = "f0p1"
                    time.sleep(1)
            elif zt == "f0p1":
                # print(" 打开过度动画 sj ", time.time()-sj)
                if time.time()-sj > jgTime:
                    # sj = 0
                    if y < 200:
                        print("1")
                        seletPC(1)
                    elif y < 400:
                        print("2")
                        seletPC(2)
                    elif y < 600:
                        print("3")
                        seletPC(3)
                    elif y < 800:
                        print("4")
                        seletPC(4)

                    # client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)
                    # zt = "f0x1"
                    # time.sleep(1)
            elif zt == "f1x1":
                client.sendto(data, iplist[pcx-1])
        elif zl[0] == "client":
            pcx = x
            # 发给单片机
            daardino = "arduino,"+ str(x) +",1"
            client.sendto(daardino.encode('utf-8'), ('127.0.0.1', portTD))
            if PCID == x:
                client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)
                zt = "f0x1"
        if a == 1:
            break
        print("zt:",zt, " 子客户 ",pcx," 当前状态坐标",x,y,zl[0])

    server.close()
def ClientRun():
    global zt
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
    server.bind(ip_portclient)

    a = 0
    sj = 0
    jgTime = 5
    print("ClientRun",ip_portclient)

    while True:
        data, client_addr = server.recvfrom(BUFSIZE)
        zl = data.decode().split(",")
        # server.sendto(data.upper(), client_addr)
        # print(data,zl)
        x = int(float(zl[1]))
        y = int(float(zl[2]))
        print('server收到的数据',x,y, zl)
        # client.sendto(data, ip_portClient1)

        if zl[0] == "mouse":
            if zt == "f0x1":
                if x < 1720 or y > 200:
                    pyautogui.click(x, y)
                    # print("move Mouse")
                    # pyautogui.moveTo(x, y)
                else:
                    client.sendto("f0p1,100,100".encode('utf-8'), ip_zl)
                    zt = "f0p1"
            elif zt == "f0p1":
                if y < 200:
                    print("1")
                    seletclientPC(1)
                elif y < 400:
                    print("2")
                    seletclientPC(2)
                elif y < 600:
                    print("3")
                    seletclientPC(3)
                elif y < 800:
                    print("4")
                    seletclientPC(4)
        if a == 1:
            break

    server.close()


def Start():
    time.sleep(1)
    client.sendto("f1x1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f0p1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f1p1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f1x1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f1p1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f0p1,100,100".encode('utf-8'), ip_zl)
    time.sleep(1)
    client.sendto("f0x1,100,100".encode('utf-8'), ip_zl)


if __name__ == '__main__':
    Start()
    if SC == 1:
        ServerRun()
    else:
        ClientRun()





# # 单击鼠标左键
# pyautogui.click()
#
# # 双击鼠标左键
# pyautogui.doubleClick()
#
# # 单击鼠标右键
# pyautogui.rightClick()
#
# # 在屏幕坐标为(x, y)的位置单击鼠标左键
# pyautogui.click(x, y)


# # 移动鼠标到屏幕坐标为(x, y)的位置
# pyautogui.moveTo(x, y)
#
# # 相对当前鼠标位置移动(dx, dy)个像素
# pyautogui.move(dx, dy)

# pyautogui.moveTo(2000, 200)
# # pyautogui.doubleClick()
#
# import time
# for i in range(100):
#     time.sleep(0.2)
#     pyautogui.moveTo(i*50, 200)
#     print(i*50)





