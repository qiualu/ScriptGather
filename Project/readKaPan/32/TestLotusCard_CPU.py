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
strATS =""
strCOSResult =""
strTmp =""
nPos = 0;
if -1 != hLotusCard:
    bResult = Objdll.LotusCardGetCardNo(hLotusCard,nRequestType, byref(sttLotusCardParam))
    if 1==bResult:
        #print(sttLotusCardParam.arrCardNo)
        print("%d" %(sttLotusCardParam.nBufferSize))
        print("CardNo(HEX) %.2X%.2X%.2X%.2X" %(sttLotusCardParam.arrCardNo[0],sttLotusCardParam.arrCardNo[1],sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[3]))
        print("CardNo(HEX) %.2X%.2X%.2X%.2X" %(sttLotusCardParam.arrCardNo[3],sttLotusCardParam.arrCardNo[2],sttLotusCardParam.arrCardNo[1],sttLotusCardParam.arrCardNo[0]))
    else:
        print("LotusCardGetCardNo Error")
    Objdll.LotusCardBeep(hLotusCard, 10)
    bResult = Objdll.LotusCardResetCpuCardNoGetCardNo(hLotusCard, byref(sttLotusCardParam))
    if 1==bResult:
        print("LotusCardResetCpuCardNoGetCardNo OK")
        for nIndex in range(0,sttLotusCardParam.nBufferSize):
            strTmp = hex(sttLotusCardParam.arrBuffer[nIndex])
            strTmp = strTmp[2:]
            strTmp = "00" + strTmp
            nPos = len(strTmp)-2
            strTmp = strTmp[nPos:]
            strATS += strTmp
        print("ATS(HEX) %s" %strATS.upper())
    else:
        print("LotusCardResetCpuCardNoGetCardNo Error")
    #随机数0084000004
    strCOSResult = ""
    sttLotusCardParam.arrCosSendBuffer[0]=0x00
    sttLotusCardParam.arrCosSendBuffer[1]=0x84
    sttLotusCardParam.arrCosSendBuffer[2]=0x00
    sttLotusCardParam.arrCosSendBuffer[3]=0x00
    sttLotusCardParam.arrCosSendBuffer[4]=0x04
    sttLotusCardParam.unCosSendBufferLength = 5
    bResult = Objdll.LotusCardSendCOSCommand(hLotusCard, byref(sttLotusCardParam))
    if 1==bResult:
        print("LotusCardSendCOSCommand OK")
        for nIndex in range(0,sttLotusCardParam.unCosReultBufferLength):
            strTmp = hex(sttLotusCardParam.arrCosResultBuffer[nIndex])
            strTmp = strTmp[2:]
            strTmp = "00" + strTmp
            nPos = len(strTmp)-2
            strTmp = strTmp[nPos:]
            strCOSResult += strTmp
        print("随机数(HEX) %s" %strCOSResult.upper())
    else:
        print("LotusCardSendCOSCommand Error")    
    Objdll.LotusCardCloseDevice(hLotusCard)
    
else:
	print("LotusCardOpenDevice ERROR")
print(bResult)
print("hello world!")
input("wait input")
