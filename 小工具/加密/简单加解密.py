

import os, sys
import time
import wmi,zlib
import win32api
import getpass
import  os

print(getpass.getuser())
user = getpass.getuser()
exepath = r'C:\Users' + "\\"
exepath += user
exepath += r"\AppData\Local\GP"
print(exepath)
if not os.path.exists(exepath):
      os.makedirs(exepath)
pathinfo = os.path.join(exepath,"path.txt")


def get_cpu_info():
    tmpdict = {}
    tmpdict["CpuCores"] = 0
    c = wmi.WMI()
    #          print c.Win32_Processor().['ProcessorId']
    #          print c.Win32_DiskDrive()
    for cpu in c.Win32_Processor():
        #                print cpu
        print("cpu id:", cpu.ProcessorId.strip())
        tmpdict["CpuType"] = cpu.Name
        try:
            tmpdict["CpuCores"] = cpu.NumberOfCores
        except:
            tmpdict["CpuCores"] += 1
            tmpdict["CpuClock"] = cpu.MaxClockSpeed
            return tmpdict

def _read_cpu_usage():
    c = wmi.WMI()
    for cpu in c.Win32_Processor():
        return cpu.LoadPercentage


def get_cpu_usage():
    cpustr1 = _read_cpu_usage()
    if not cpustr1:
        return 0
    time.sleep(2)
    cpustr2 = _read_cpu_usage()
    if not cpustr2:
        return 0
    cpuper = int(cpustr1) + int(cpustr2) / 2
    return cpuper


def get_disk_info():
    tmplist = []
    encrypt_str = ""
    c = wmi.WMI()
    for cpu in c.Win32_Processor():
        # cpu 序列号
        encrypt_str = encrypt_str + cpu.ProcessorId.strip()
        print("cpu id:", cpu.ProcessorId.strip())
    for physical_disk in c.Win32_DiskDrive():
        encrypt_str = encrypt_str + physical_disk.SerialNumber.strip()

        # 硬盘序列号
        print('disk id:', physical_disk.SerialNumber.strip())
        tmpdict = {}
        tmpdict["Caption"] = physical_disk.Caption
        tmpdict["Size"] = int(physical_disk.Size) / 1000 / 1000 / 1000
        tmplist.append(tmpdict)
    for board_id in c.Win32_BaseBoard():
        # 主板序列号
        encrypt_str = encrypt_str + board_id.SerialNumber.strip()
        print("main board id:", board_id.SerialNumber.strip())
    #          for mac in c.Win32_NetworkAdapter():

    # mac 地址（包括虚拟机的）
    #                    print "mac addr:", mac.MACAddress:
    for bios_id in c.Win32_BIOS():
        # bios 序列号
        encrypt_str = encrypt_str + bios_id.SerialNumber.strip()
        print("bios number:", bios_id.SerialNumber.strip())
    print("encrypt_str:", encrypt_str,type(encrypt_str))
    # encrypt_str: BFEBFBFF000906E9WD-WCC6Y6CDLRLTS3JENX0JB00766JDefault stringDefault string <class 'str'>


    # 加密算法
    print(zlib.adler32(encrypt_str.encode())) # // 4187690684
    mama = zlib.adler32(encrypt_str.encode())
    # return mama  # 密码
    return encrypt_str  # 秘钥


if __name__ == "__main__":
    #     a = get_cpu_info()
    mima = get_disk_info()
    # mmfpath = r"C:\Users\yl\AppData\Local\GP\解锁秘钥.txt"
    # mmfpath = r"C:\Users\yl\AppData\Local\GP\解锁密码.txt"
    with open("秘钥", "w") as f:
        f.write(str(mima))
        f.flush()

    # with open(mmfpath, "r") as f:
    #     mm = f.read()
    #     print(mm)
    #     # print(zlib.adler32(mm.encode()))
    #
    # if mima == mm or str(mima) == mm:
    #     print("解锁成功")
    # else:
    #     print("解锁失败",mima,mm)
    # print(mima)




