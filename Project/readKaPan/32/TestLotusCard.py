from ctypes import *
import os
class LotusCardParamStruct(Structure): 
    _fields_ = [ ("nCardType", c_int), 
              ("arrCardNo", c_ubyte * 8),
              ("nCardSize",c_int) ,
              ("arrBuffer", c_ubyte * 64),
              ("nBufferSize", c_int),
              ("arrKeys", c_ubyte * 64),
              ("nKeysSize", c_int),
              ("arrCosResultBuffer", c_ubyte * 256),
              ("unCosReultBufferLength", c_int),
              ("arrCosSendBuffer", c_ubyte * 256),
              ("unCosSendBufferLength", c_int)] 
print(os.getcwd()+"\LotusCardDriver.dll")
#Objdll = windll.LoadLibrary("LotusCardDriver.dll")
Objdll = windll.LoadLibrary(os.getcwd()+"\LotusCardDriver.dll")
sttLotusCardParam = LotusCardParamStruct()
#int _stdcall LotusCardOpenDevice(char * pszDeviceName, int nVID, int nPID, LotusCardExtendReadWriteCallBack  pLotusCardExtendReadWriteCallBack);
#LotusHandle WINAPI LotusCardOpenDevice(char * pszDeviceName, int nVID, int nPID, int nUsbDeviceIndex, unsigned int unRecvTimeOut, LotusCardExtendReadWriteCallBack  pLotusCardExtendReadWriteCallBack);
hLotusCard = Objdll.LotusCardOpenDevice("",0,0,0,2000,0)
print(hLotusCard)
RT_ALL = 0x52
RT_NOT_HALT = 0x26
AM_A = 0x60
AM_B = 0x61
nRequestType = RT_NOT_HALT
bResult = 0
if -1 != hLotusCard:
    bResult = Objdll.LotusCardGetCardNo(hLotusCard,nRequestType, byref(sttLotusCardParam))
    if 1==bResult:
        #print(sttLotusCardParam.arrCardNo)
        print("%d" %(len(sttLotusCardParam.arrCardNo)))
        #print("CardNo(HEX) %.2x%.2x%.2x%.2x" %(sttLotusCardParam.arrCardNo[0],sttLotusCardParam.arrCardNo[1],sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[3]))
        print("CardNo(HEX) %.2X%.2X%.2X%.2X" %(sttLotusCardParam.arrCardNo[0],sttLotusCardParam.arrCardNo[1],sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[3]))
        print("CardNo(HEX) %.2X%.2X%.2X%.2X" %(sttLotusCardParam.arrCardNo[3],sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[1],sttLotusCardParam.arrCardNo[0]))
    else:
        print("LotusCardGetCardNo Error")
    if 1==bResult:
        #sttLotusCardParam.arrKeys = "\xff\xff\xff\xff\xff\xff"
        sttLotusCardParam.arrKeys[0] = 0xff
        sttLotusCardParam.arrKeys[1] = 0xff
        sttLotusCardParam.arrKeys[2] = 0xff
        sttLotusCardParam.arrKeys[3] = 0xff
        sttLotusCardParam.arrKeys[4] = 0xff
        sttLotusCardParam.arrKeys[5] = 0xff
        bResult =Objdll.LotusCardLoadKey(hLotusCard, AM_A, 0, byref(sttLotusCardParam))
    if 1==bResult:
        print("LotusCardLoadKey OK")
    else:
        print("LotusCardLoadKey Error")
    if 1==bResult:
        bResult =Objdll.LotusCardAuthentication(hLotusCard, AM_A, 0, byref(sttLotusCardParam))
    if 1==bResult:
        print("LotusCardAuthentication OK")
    else:
        print("LotusCardAuthentication Error")
                    
    if 1==bResult:
        bResult =Objdll.LotusCardRead(hLotusCard, 2, byref(sttLotusCardParam))
    if 1==bResult:
        print("LotusCardRead OK")
        #print(sttLotusCardParam.arrBuffer)
        print("ReadData(HEX):%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x%.2x" %(sttLotusCardParam.arrBuffer[0],sttLotusCardParam.arrBuffer[1],sttLotusCardParam.arrBuffer[2],sttLotusCardParam.arrBuffer[3],
            sttLotusCardParam.arrBuffer[4],sttLotusCardParam.arrBuffer[5],sttLotusCardParam.arrBuffer[6],sttLotusCardParam.arrBuffer[7],
            sttLotusCardParam.arrBuffer[8],sttLotusCardParam.arrBuffer[9],sttLotusCardParam.arrBuffer[10],sttLotusCardParam.arrBuffer[11],
            sttLotusCardParam.arrBuffer[12],sttLotusCardParam.arrBuffer[13],sttLotusCardParam.arrBuffer[14],sttLotusCardParam.arrBuffer[15]))
    else:
        print("LotusCardRead Error")
    if 1==bResult:
        sttLotusCardParam.arrBuffer[0] = 0x00
        sttLotusCardParam.arrBuffer[1] = 0x01
        sttLotusCardParam.arrBuffer[2] = 0x02
        sttLotusCardParam.arrBuffer[3] = 0x03
        sttLotusCardParam.arrBuffer[4] = 0x04
        sttLotusCardParam.arrBuffer[5] = 0x05
        sttLotusCardParam.arrBuffer[6] = 0x06
        sttLotusCardParam.arrBuffer[7] = 0x07
        sttLotusCardParam.arrBuffer[8] = 0x08
        sttLotusCardParam.arrBuffer[9] = 0x09
        sttLotusCardParam.arrBuffer[10] = 0x0A
        sttLotusCardParam.arrBuffer[11] = 0x0B
        sttLotusCardParam.arrBuffer[12] = 0x0C
        sttLotusCardParam.arrBuffer[13] = 0x0D
        sttLotusCardParam.arrBuffer[14] = 0x0E
        sttLotusCardParam.arrBuffer[15] = 0x0F
        
        sttLotusCardParam.nKeysSize = 16
        bResult =Objdll.LotusCardWrite(hLotusCard, 2, byref(sttLotusCardParam))
    if 1==bResult:
        print("LotusCardWrite OK")
    else:
        print("LotusCardWrite Error")
    Objdll.LotusCardCloseDevice(hLotusCard)
    
else:
	print("LotusCardOpenDevice ERROR")
print(bResult)
print("hello world!")
input("wait input")
