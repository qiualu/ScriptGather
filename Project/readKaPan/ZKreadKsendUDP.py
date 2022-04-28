from ctypes import *
import os
import socket

import threading
from threading import current_thread

import serial
from time import sleep
import time
import configparser

import serial.tools.list_ports

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ----------import M M -------------

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

sy = {
    0: -65.25, 1: -56.99, 2: -51.67, 3: -47.74, 4: -44.62, 5: -42.03, 6: -39.82, 7: -37.89, 8: -36.17, 9: -34.63, 10: -33.24,
    11: -31.96, 12: -30.78, 13: -29.68, 14: -28.66, 15: -27.7, 16: -26.8, 17: -25.95, 18: -25.15, 19: -24.38, 20: -23.65,
    21: -22.96, 22: -22.3, 23: -21.66, 24: -21.05, 25: -20.46, 26: -19.9, 27: -19.35, 28: -18.82, 29: -18.32, 30: -17.82,
    31: -17.35, 32: -16.88, 33: -16.44, 34: -16.0, 35: -15.58, 36: -15.16, 37: -14.76, 38: -14.37, 39: -13.99, 40: -13.62,
    41: -13.26, 42: -12.9, 43: -12.56, 44: -12.22, 45: -11.89, 46: -11.56, 47: -11.24, 48: -10.93, 49: -10.63, 50: -10.33,
    51: -10.04, 52: -9.75, 53: -9.47, 54: -9.19, 55: -8.92, 56: -8.65, 57: -8.39, 58: -8.13, 59: -7.88, 60: -7.63,
    61: -7.38, 62: -7.14, 63: -6.9, 64: -6.67, 65: -6.44, 66: -6.21, 67: -5.99, 68: -5.76, 69: -5.55, 70: -5.33,
    71: -5.12, 72: -4.91, 73: -4.71, 74: -4.5, 75: -4.3, 76: -4.11, 77: -3.91, 78: -3.72, 79: -3.53, 80: -3.34,
    81: -3.15, 82: -2.97, 83: -2.79, 84: -2.61, 85: -2.43, 86: -2.26, 87: -2.09, 88: -1.91, 89: -1.75, 90: -1.58,
    91: -1.41, 92: -1.25, 93: -1.09, 94: -0.93, 95: -0.77, 96: -0.61, 97: -0.46, 98: -0.3, 99: -0.15, 100: 0.0
}

class LotusCardParamStruct(Structure):
    _fields_ = [("nCardType", c_int),
                ("arrCardNo", c_ubyte * 8),
                ("nCardSize", c_int),
                ("arrBuffer", c_ubyte * 64),
                ("nBufferSize", c_int),
                ("arrKeys", c_ubyte * 64),
                ("nKeysSize", c_int),
                ("arrCosResultBuffer", c_ubyte * 256),
                ("unCosReultBufferLength", c_int),
                ("arrCosSendBuffer", c_ubyte * 256),
                ("unCosSendBufferLength", c_int)]



print("Read satart main")

class zkread():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("中控读卡配置文件.ini",encoding="utf-8")

        self.udpoutip = config.get("socket","udpoutip")
        self.udpoutprot = int(config.get("socket","udpoutprot"))
        self.udpinip = config.get("socket","udpinip")
        self.udpinport = int(config.get("socket","udpinport"))

        self.ipOut_port = (self.udpoutip, self.udpoutprot)
        self.ipIn_port = (self.udpinip, self.udpinport)

        self.serialopen = 0
        self.serialcom = config.get("serial","com")

        self.BUFSIZE = 1024
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.rank1 = config.get("readKapan", "rank1")
        self.rank2 = config.get("readKapan", "rank2")
        self.rank3 = config.get("readKapan", "rank3")
        self.rank4 = config.get("readKapan", "rank4")
        self.rank5 = config.get("readKapan", "rank5")
        self.rank6 = config.get("readKapan", "rank6")


        self.sendABCD = "A"
        self.sendIndex = 0

        self.readKanOpen = 0

        self.endexe = 0

        # 开启串口
        self.initSerial()
        # # 开启线程
        # self.print_base_class()

        self.openTh()
        #

        print("init 完成 开启本类循环")
        self.classloop()


    def initSerial(self):

        try:
            self.serialopen = 0
            self.serial = serial.Serial(self.serialcom, 9600, timeout=0.5)  #/dev/ttyUSB0
            if self.serial.isOpen():
                print("open success")
                self.serialopen = 1
            else:
                print("open failed")
                self.serialopen = 0
        except EnvironmentError as e:
            print("串口 : ",e)



    def print_base_class(self):
        print("udpoutip",self.udpoutip)
        print("udpoutprot", self.udpoutprot)
        print("udpinip", self.udpinip)
        print("udpinport", self.udpinport)
        print("serialcom", self.serialcom)

    def classloop(self):
        num = 0
        while True:
            num += 1
            print(" 本类计时 classloop : ",num)
            time.sleep(20)

            if self.readKanOpen == 0:
                print("重启 读卡进程 ")
                read = threading.Thread(target=self.readloop)
                read.start()
                # 测试
                self.clientUDP(str(88))
            # self.clientUDP(str(num))

    def openTh(self):
        sUdp = threading.Thread(target=self.serverUDP)
        sUdp.start()
        print("打开读卡进程")
        read = threading.Thread(target=self.readloop)
        read.start()

        # cUdp = threading.Thread(target=self.clientUDP)
        # cUdp.start()

    def readloop(self):
        print("readloop线程状态 : ",current_thread().getName(),'start') #显示当前线程的状态
        self.readKanOpen = 0
        print("readloop  : ",os.getcwd() + "\LotusCardDriver.dll")
        # Objdll = windll.LoadLibrary("LotusCardDriver.dll")
        Objdll = windll.LoadLibrary(os.getcwd() + "\LotusCardDriver.dll")
        sttLotusCardParam = LotusCardParamStruct()
        # int _stdcall LotusCardOpenDevice(char * pszDeviceName, int nVID, int nPID, LotusCardExtendReadWriteCallBack  pLotusCardExtendReadWriteCallBack);
        # LotusHandle WINAPI LotusCardOpenDevice(char * pszDeviceName, int nVID, int nPID, int nUsbDeviceIndex, unsigned int unRecvTimeOut, LotusCardExtendReadWriteCallBack  pLotusCardExtendReadWriteCallBack);
        # strServerIp = '192.168.1.252'
        strServerIp = ''
        hLotusCard = -1
        print("readloop  hLotusCard: ",hLotusCard)
        Objdll.LotusCardOpenDevice.restype = c_longlong
        Objdll.LotusCardGetCardNo.argtypes = [c_longlong, c_int, c_void_p]
        Objdll.LotusCardLoadKey.argtypes = [c_longlong, c_int, c_int, c_void_p]
        Objdll.LotusCardAuthentication.argtypes = [c_longlong, c_int, c_int, c_void_p]
        Objdll.LotusCardRead.argtypes = [c_longlong, c_int, c_void_p]
        Objdll.LotusCardWrite.argtypes = [c_longlong, c_int, c_void_p]
        Objdll.LotusCardCloseDevice.argtypes = [c_longlong]
        Objdll.LotusCardSetCardType.argtypes = [c_longlong, c_byte]
        Objdll.LotusCardGetTwoGenerationIDCardNo.argtypes = [c_longlong, c_char_p, c_int]
        hLotusCard = Objdll.LotusCardOpenDevice(strServerIp.encode('gb2312'), 0, 0, 0, 2000, 0)
        print("readloop  hLotusCard: ", hLotusCard)
        RT_ALL = 0x52
        RT_NOT_HALT = 0x26
        AM_A = 0x60
        AM_B = 0x61
        szTwoGenerationID = bytes(64)
        nRequestType = RT_NOT_HALT
        bResult = 0
        # input("wait input")

        hh = [self.rank1, self.rank2, self.rank3, self.rank4, self.rank5, self.rank6]
        if -1 != hLotusCard:
            bResult = Objdll.LotusCardGetCardNo(hLotusCard, nRequestType, byref(sttLotusCardParam))
            if 1 == bResult:
                data = "%.2X%.2X%.2X%.2X" % (
                    sttLotusCardParam.arrCardNo[0], sttLotusCardParam.arrCardNo[1], sttLotusCardParam.arrCardNo[2],
                    sttLotusCardParam.arrCardNo[3])
                print("readloop  : ", "data ", data)
            else:
                print("LotusCardGetCardNo Error")
            self.readKanOpen = 1
            killa = 1
            self.SendSerial("D") # 开灯
            index = 0
            jishi = 100
            while killa:

                if self.endexe == 1: # 关机退出了
                    self.readKanOpen = 1
                    self.SendSerial("C")
                    break

                time.sleep(0.3)
                bResult = Objdll.LotusCardGetCardNo(hLotusCard, nRequestType, byref(sttLotusCardParam))
                if 1 == bResult:
                    data = "%.2X%.2X%.2X%.2X" % (
                    sttLotusCardParam.arrCardNo[0], sttLotusCardParam.arrCardNo[1], sttLotusCardParam.arrCardNo[2],
                    sttLotusCardParam.arrCardNo[3])
                    if index > jishi:
                        index = 0
                        print("data ", data)

                    biaohao = 0
                    for i in hh:
                        biaohao += 1
                        if data == i:
                            self.clientUDP(str(biaohao))
                            self.SendSerial("A")
                else:

                    self.clientUDP(str(88))
                    self.SendSerial("B")
                    index += 1
                    if index > jishi:
                        print("LotusCardGetCardNo 卡片未放置")
                        index = 0
                        self.SendSerial("D")

            print("退出循环 ",killa)
            Objdll.LotusCardCloseDevice(hLotusCard)

        else:
            print("readloop  : ", "LotusCardOpenDevice ERROR")
        print("readloop  bResult: ", bResult)
        print("readloop  : ", "hello world!")
        self.readKanOpen = 0

    def serverUDP(self):
        try:
            print("serverUDP线程状态 : ", current_thread().getName(), 'start')  # 显示当前线程的状态
            self.server.bind(self.ipIn_port)
            while True:
                data, client_addr = self.server.recvfrom(self.BUFSIZE)

                shengy = data.decode()[0:-3]

                print('server收到的数据', data,data.upper(), client_addr,shengy)
                #self.server.sendto(data.upper(), client_addr)
                self.clientUDP(data.decode())

                if data == b'OFF':
                    print("关机")
                    self.SendSerial("C")
                    self.endexe = 1
                    time.sleep(1)
                    os.system("shutdown -s -t 10")
                elif shengy == "vol":
                    sydxx = int(data.decode()[4:])



                    volume.SetMasterVolumeLevel(sy[sydxx], None)
                elif data == b'A\x00':
                    self.SendSerial("A")
                elif data == b'B\x00':
                    self.SendSerial("B")

                # if self.endexe == 1: # 关机退出了
                #     #self.readKanOpen = 1
                #     break
        except EnvironmentError as e:
            print("------------------------------ serverUDP except  EnvironmentError------------------------------")
            print("serverUDP Error ",e)



    def SendSerial(self,data):
        try:
            # print("SendSerial",data)
            if self.serialopen == 0:
                self.initSerial()
                return

            if self.sendABCD == data and self.sendIndex < 30:
                self.sendIndex += 1
            elif self.sendIndex > 30:
                self.sendIndex = 0
                self.sendABCD = data
                self.serial.write(data.encode('utf-8'))  # 数据写回
            else:
                self.sendABCD = data
                self.serial.write(data.encode('utf-8'))  # 数据写回

        except EnvironmentError as e:
            print("------------------------------ SendSerial except  EnvironmentError------------------------------")
            print("SendSerial Error ", e)
            self.initSerial()

    def clientUDP(self,msg):
        self.client.sendto(msg.encode('utf-8'), self.ipOut_port)
        # print('client send --> ', msg)
        #time.sleep(5)



    def endproject(self):
        self.server.close()
        self.client.close()

if __name__ == '__main__':
    zkread()




