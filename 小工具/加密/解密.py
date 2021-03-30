
import zlib,win32api,win32con


if __name__ == "__main__":
    #     a = get_cpu_info()
    # mima = get_disk_info()
    # mmfpath = r"C:\Users\yl\AppData\Local\GP\解锁秘钥.txt"
    # mmfpath = r"C:\Users\yl\AppData\Local\GP\解锁密码.txt"
    mm = ""
    mima = ""
    try:
        with open("秘钥", "r") as f:
            mm = f.read()
            mima = str(zlib.adler32(mm.encode()))
            print(mima)

        if len(mima) > 1:
            ##提醒OK消息框
            with open("key", "w") as fwr:
                fwr.write(mima)
                fwr.flush()
            win32api.MessageBox(0, "完成", "秘钥导出", win32con.MB_OK)
        else:
            win32api.MessageBox(0, "生成失败w", "秘钥导出", win32con.MB_OK)

    except EnvironmentError as e:
        win32api.MessageBox(0, "生成失败t", "秘钥导出", win32con.MB_OK)
        print(e)



    # with open(pathinfo, "r") as f:
    #     mm = f.read()
    #     print(mm)
    #     print(zlib.adler32(mm.encode()))