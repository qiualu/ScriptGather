from ctypes import *
import os
import socket
import threading
from threading import current_thread
import serial
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


class udpmanage():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("中控管理配置.ini",encoding="utf-8")


        self.udpinip = config.get("socket","udpinip")
        self.udpinport = int(config.get("socket","udpinport"))

        self.ipIn_port = (self.udpinip, self.udpinport)
        print(self.udpinip,self.udpinport)
        self.BUFSIZE = 1024
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议

        self.serverUDP()

    def serverUDP(self):
        try:
            print("serverUDP线程状态 : ", current_thread().getName(), 'start')  # 显示当前线程的状态
            self.server.bind(self.ipIn_port)
            while True:
                data, client_addr = self.server.recvfrom(self.BUFSIZE)
                shengy = data.decode()[0:3]
                print('server收到的数据', data,data.upper(), client_addr,shengy)
                if data == b'OFF':
                    print("关机")
                    self.endexe = 1
                    time.sleep(1)
                    os.system("shutdown -s -t 10")
                elif shengy == "vol":
                    sydxx = int(data.decode()[4:])
                    print("sydxx : ",sydxx)
                    volume.SetMasterVolumeLevel(sy[sydxx], None)

        except EnvironmentError as e:
            print("------------------------------ serverUDP except  EnvironmentError------------------------------")
            print("serverUDP Error ",e)


    def endproject(self):
        self.server.close()

if __name__ == '__main__':
    udpmanage()




