
import os
import time
a = 0


while a < 15:
    a += 1
    # os.popen("adb shell screencap -p /sdcard/screen.png")
    # os.popen("adb pull /sdcard/screen.png")
    time.sleep(1)
    print(" ----------New yilun -------- ",a)
    print(" 扫码 ")
    os.popen("adb shell input tap 159 333 ")
    time.sleep(7)
    print(" 金额 ")
    os.popen("adb shell input tap 135  1742 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 375  1914 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 286  2264 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 950  2052 ")
    time.sleep(4.5)

    print(" 监管 ")
    os.popen("adb shell input tap 540 1620 ")
    time.sleep(4.5)



    print(" 密码 ")
    os.popen("adb shell input tap 959 1158 ")
    time.sleep(3.5)
    print(" 数值 ")

    os.popen("adb shell input tap 519  1744 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 177  1749 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 902 1890 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 177  1749 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 177  1749 ")
    time.sleep(0.5)
    os.popen("adb shell input tap 565  2251 ")
    time.sleep(0.5)

    time.sleep(5)
    os.popen("adb shell input tap 540  2266 ")
    time.sleep(3)

    print(" -----------------------  ")
# adb shell am start pkgName/.activityName
# packageName = com.eg.android.AlipayGphone

# 雨落山南:
# className = android.widget.TextView
#
# 雨落山南:
# packageName = com.huawei.android.launcher


# 159 385

# 135  1742
# 375  1914
# 286  2264
# 950  2052
#
#
# 959 1158
#
# 519  1744
# 177  1749
# 902 1890
# 177  1749
# 177  1749
# 565  2251



