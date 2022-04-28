
import serial
from time import sleep
import time

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        time.sleep(0.02)
    return data

if __name__ == '__main__':

    serial = serial.Serial("com5", 9600, timeout=0.5)  #/dev/ttyUSB0
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")
    while True:
        # data =recv(serial)
        # if data != b'' :
        # print("收到 receive : ",data)
        data = input(">>")

        serial.write(data.encode('utf-8')) #数据写回








