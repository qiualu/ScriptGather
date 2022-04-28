# read_config.py文件
from __future__ import print_function
from pycaw.pycaw import AudioUtilities

import configparser
import socket
# 引入库
import pyaudio
import wave
import sys
import socket
import threading
import time

import pygame

paly_tf = 0
endplay = 0

zhongduan = 0

config = configparser.ConfigParser()
config.read("声音配置文件.ini", encoding="utf-8")
ip = config.get("Home", "ip")
port = int(config.get("Home", "port"))
shengyin = config.get("Home", "声音")

bof = config.get("Home", "播放")
boz = config.get("Home", "停止")

间隔时间 = config.get("Home", "间隔时间")

audioyliang = config.get("Home", "降低程序音量")

设置程序音量 = int(config.get("Home", "设置程序音量"))

audioyliang_zuixiao = int(config.get("Home", "降低程序音量最小"))
audioyliang_time = int(config.get("Home", "降低程序音量时间"))

本机端口port = int(config.get("Home", "本机端口port"))



print(ip, type(ip), repr(ip))
print(port, type(port), repr(port))
print(shengyin, type(shengyin), repr(shengyin))


class AudioController(object):
    def __init__(self, process_name):
        self.process_name = process_name
        self.volume = self.process_volume()

    def process_volume(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                print('Volume:', interface.GetMasterVolume())  # debug
                return interface.GetMasterVolume()

    def set_volume(self, decibels):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                # only set volume in the range 0.0 to 1.0
                self.volume = min(1.0, max(0.0, decibels))
                interface.SetMasterVolume(self.volume, None)
                print('Volume set to', self.volume)  # debug

audio_controller = AudioController(audioyliang)



def udp_send(udp_socket,ip,port):
    while True:
        try:
            # 获取发送的信息
            data = input('请输入要发送的信息：')
            udp_socket.sendto(data.encode('gbk'), (ip,port))
        except Exception as erro:
            print('错误类型：',erro)

def udp_recv(udp_socket):
    global paly_tf,endplay,zhongduan,本机端口port
    while True:
        # 接收信息
        try:
            recv_data = udp_socket.recvfrom(1024)
        except:
            print("断开链接")
            #udp_socket.bind(('', 本机端口port))
            continue
        da = recv_data[0].decode('gbk')
        print("UDP read : ",da,recv_data)
        if da == bof: # bof 12
            print("bofang")
            paly_tf = 1
        elif da == boz: # boz 13
            endplay = 1
            zhongduan = 1
            data = boz
            udp_socket.sendto(data.encode('gbk'), (ip, port))
            #print("播放  1113")
        print('接收的信息：', recv_data[0].decode('gbk'),da)

def paly():
    global endplay


    # 定义数据流块
    chunk = 1024
    # 只读方式打开wav文件
    f = wave.open(shengyin, "rb")
    p = pyaudio.PyAudio()
    # 打开数据流
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # 读取数据
    data = f.readframes(chunk)

    # 播放
    while data != b'':
        stream.write(data)
        data = f.readframes(chunk)
        # audio_controller2.set_volume(0.2)
        if endplay == 1:
            break
    # 停止数据流
    stream.stop_stream()
    stream.close()
    # 关闭 PyAudio
    p.terminate()

# 调节音量
def tiaojie(sj):
    ys = 1
    sjlj = 0

    if sj == 0:
        降低到 = (1 - (audioyliang_zuixiao / 100))
        print("降低到  ", 降低到)
        zyl = 1
        shj = (1 - (audioyliang_zuixiao / 100)) / (audioyliang_time / 0.03)
        jsjs = 0
        while True:
            time.sleep(0.03)
            sjlj += 0.03
            zyl = zyl - shj
            jsjs += 1
            if audioyliang_time < sjlj:
                break
            audio_controller.set_volume(zyl)
            #print(" shudu ", jsjs, audioyliang_time, zyl)
        audio_controller.set_volume(audioyliang_zuixiao / 100)
        print("xxx  ", audioyliang_zuixiao / 100)
    else:
        降低到 = (1 - (audioyliang_zuixiao / 100))
        print("降低到  ", 降低到)
        zyl = audioyliang_zuixiao / 100
        shj = (1 - (audioyliang_zuixiao / 100)) / (audioyliang_time / 0.03)
        jsjs = 0
        while True:
            time.sleep(0.03)
            sjlj += 0.03
            zyl = zyl + shj
            jsjs += 1
            if audioyliang_time < sjlj:
                break
            audio_controller.set_volume(zyl)
            #print(" shudu ", jsjs, audioyliang_time, zyl)
        audio_controller.set_volume(1.0)
        print("xxx  ", 1.0)
    print("调音 ")


def main():
    global paly_tf, endplay, zhongduan
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(('',本机端口port))
    t2 = threading.Thread(target=udp_recv, args=(udp_socket,))
    t2.start()

    print("123")

    while True:
        time.sleep(3)
        # print("等待指令")
        if paly_tf == 1:
            print("有消息")
            zhongduan = 0
            endplay = 0
            tiaojie(0)
            paly()
            tiaojie(1)
            paly_tf = 0
            if zhongduan == 0:
                data = bof # 12
                jstime = 0
                while True:
                    time.sleep(1)
                    jstime += 1
                    if zhongduan == 1:
                        break
                    elif jstime > int(间隔时间):
                        udp_socket.sendto(data.encode('gbk'), (ip, port))
                        break
            print("播放  1113")



if __name__ == '__main__':

    main()

    # pygame.init()










