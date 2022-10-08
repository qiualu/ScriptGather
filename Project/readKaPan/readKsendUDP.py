from ctypes import *
import os
import  time
import socket

BUFSIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import serial
from time import sleep
import time


# -----------------------
with open("配置文件.ini", 'r') as f:
    comindex = f.readline().strip()
    # print(zf,type(zf),len(zf))
    ipindex = f.readline().strip()
    # print(zf,type(zf),len(zf))


# -----------------------

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        time.sleep(0.02)
    return data

serial = serial.Serial(comindex, 9600, timeout=0.5)  #/dev/ttyUSB0
if serial.isOpen() :
    print("open success")
else :
    print("open failed")

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


print(os.getcwd() + "\LotusCardDriver.dll")
# Objdll = windll.LoadLibrary("LotusCardDriver.dll")
Objdll = windll.LoadLibrary(os.getcwd() + "\LotusCardDriver.dll")
sttLotusCardParam = LotusCardParamStruct()
# int _stdcall LotusCardOpenDevice(char * pszDeviceName, int nVID, int nPID, LotusCardExtendReadWriteCallBack  pLotusCardExtendReadWriteCallBack);
# LotusHandle WINAPI LotusCardOpenDevice(char * pszDeviceName, int nVID, int nPID, int nUsbDeviceIndex, unsigned int unRecvTimeOut, LotusCardExtendReadWriteCallBack  pLotusCardExtendReadWriteCallBack);
# strServerIp = '192.168.1.252'
strServerIp = ''
hLotusCard = -1
print(hLotusCard)
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
print(hLotusCard)
RT_ALL = 0x52
RT_NOT_HALT = 0x26
AM_A = 0x60
AM_B = 0x61
szTwoGenerationID = bytes(64)
nRequestType = RT_NOT_HALT
bResult = 0
# input("wait input")

hh = ['0488B502',"048EB502","0491B502",'048BB502','535859BF']

if -1 != hLotusCard:

    bResult = Objdll.LotusCardGetCardNo(hLotusCard, nRequestType, byref(sttLotusCardParam))
    if 1 == bResult:
        # print(sttLotusCardParam.arrCardNo)
        print("%d" % (len(sttLotusCardParam.arrCardNo)))
        # print("CardNo(HEX) %.2x%.2x%.2x%.2x" %(sttLotusCardParam.arrCardNo[0],sttLotusCardParam.arrCardNo[1],sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[3]))
        print("CardNo(HEX) %.2X%.2X%.2X%.2X" % (
        sttLotusCardParam.arrCardNo[0], sttLotusCardParam.arrCardNo[1], sttLotusCardParam.arrCardNo[2],
        sttLotusCardParam.arrCardNo[3]))
        print("CardNo(HEX) %.2X%.2X%.2X%.2X" % (
        sttLotusCardParam.arrCardNo[3], sttLotusCardParam.arrCardNo[2], sttLotusCardParam.arrCardNo[1],
        sttLotusCardParam.arrCardNo[0]))

        data = "%.2X%.2X%.2X%.2X" % (
        sttLotusCardParam.arrCardNo[0], sttLotusCardParam.arrCardNo[1], sttLotusCardParam.arrCardNo[2],
        sttLotusCardParam.arrCardNo[3])
        print("data " ,data)
    else:
        print("LotusCardGetCardNo Error")
    killa = 1
    while killa:
        time.sleep(1)
        bResult = Objdll.LotusCardGetCardNo(hLotusCard, nRequestType, byref(sttLotusCardParam))
        if 1 == bResult:
            data = "%.2X%.2X%.2X%.2X" % (sttLotusCardParam.arrCardNo[0], sttLotusCardParam.arrCardNo[1], sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[3])
            print("data ", data)
            biaohao = 0
            for i in hh:
                biaohao += 1
                if data == i:
                    print("biaohao", biaohao)
                    ip_port = (ipindex, 9999)
                    msg = str(biaohao)
                    client.sendto(msg.encode('utf-8'), ip_port)
                    data = "A"
                    serial.write(data.encode('utf-8'))  # 数据写回
        else:
            print("LotusCardGetCardNo Error")
            ip_port = (ipindex, 9999)
            msg = str(88)
            client.sendto(msg.encode('utf-8'), ip_port)

            data = "B"
            serial.write(data.encode('utf-8'))  # 数据写回


    Objdll.LotusCardCloseDevice(hLotusCard)

else:
    print("LotusCardOpenDevice ERROR")
print(bResult)
print("hello world!")
# input("wait input")
