# -*- coding: utf-8 -*-

# from .ui import Ui_MainWindow
# import ui.Ui_MainWindow as Ui_MainWindow

import win32api, win32con, win32gui
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.xui import Ui_MainWindow
from ui.dw import ScreenShot
import pytesseract
from PIL import Image
import time
import pyautogui
import cv2
import cv2 as cv
import win32gui
import threading
import os
import configparser
import numpy
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

import winsound

config = configparser.ConfigParser()
filepath = os.path.join(os.getcwd(), "配置文件.ini")

print(filepath)

# from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

import random

class MainGui(Ui_MainWindow):
    def __init__(self, Dialog):
        super().setupUi(Dialog)
        self.initUISet()
        self.initConnect()
        self.initDate()
        # self.initKNN()
        Dialog.setWindowTitle("股票数据采集")
        Dialog.setWindowIcon(QIcon('ui/back.jpg'))  # 设置图标

        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(Dialog.backgroundRole(), QBrush(QPixmap('ui/back.jpg')))  # 设置背景图片
        Dialog.setPalette(palette1)

        self.whlie_run = False

        # cw = QtGui.QWidget()
        # Dialog.setCentralWidget(cw)
        #
        # l = QtGui.QVBoxLayout()
        # cw.setLayout(self.l1)
        #
        self.pw = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
        self.l1.addWidget(self.pw)
        self.pw2 = pg.PlotWidget(name='Plot2')
        self.l2.addWidget(self.pw2)

        self.pw3 = pg.PlotWidget()

        self.l3.addWidget(self.pw3)

        # rect = QtGui.QGraphicsRectItem(QtCore.QRectF(0, 0, 1, 5e-11))
        # rect.setPen(pg.mkPen(100, 200, 100))
        # pw.addItem(rect)
        self.pw.setLabel('left', 'Value', units='V')
        self.pw.setLabel('bottom', 'Time', units='s')
        self.pw.setXRange(0, 2)
        self.pw.setYRange(0, 1e-10)

        da ,n  = self.rand(3)
        print("data --- > ", da, n,np.random.normal(size=5) * 1e0)
        # print("好好-- > ",np.random.normal(size=3))
        # self.data = np.random.normal(size=5) * 1e0
        self.data = [10]
        print("type(self.data)  -- > ",type(self.data))
        # curve = self.pw3(np.random.normal(size=100) * 1e0, clickable=True)
        # curve.curve.setClickable(True)
        # curve.setPen('w')  ## white pen
        # curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))


    def rand(self,n):
        data = np.random.random(n)
        data[int(n * 0.1):int(n * 0.13)] += .5
        data[int(n * 0.18)] += 2
        data[int(n * 0.1):int(n * 0.13)] *= 5
        data[int(n * 0.18)] *= 20
        data *= 1e-12
        return data, np.arange(n, n + len(data)) / float(n)

    def updateData(self):
        yd, xd = rand(10000)
        p1.setData(y=yd, x=xd)
        print("data 1")

    def initDate(self):
        config.read("配置文件.ini", encoding="utf-8-sig")
        R1 = config["R1"]
        R2 = config["R2"]
        self.R1_zb = []
        self.R2_zb = []
        self.R1_zb = [int(R1.getfloat("x")), int(R1.getfloat("y")), int(R1.getfloat("w")), int(R1.getfloat("h"))]
        self.R2_zb = [int(R2.getfloat("x")), int(R2.getfloat("y")), int(R2.getfloat("w")), int(R2.getfloat("h"))]
        Rrj1 = config["Rrj1"]
        Rrj2 = config["Rrj2"]
        self.Rrj1_zb = [int(Rrj1.getfloat("x")), int(Rrj1.getfloat("y")), int(Rrj1.getfloat("w")),
                        int(Rrj1.getfloat("h"))]
        self.Rrj2_zb = [int(Rrj2.getfloat("x")), int(Rrj2.getfloat("y")), int(Rrj2.getfloat("w")),
                        int(Rrj2.getfloat("h"))]

        print(" self.R1_zb  ", self.R1_zb)
        print(" self.R2_zb  ", self.R2_zb)
        print(" self.Rrj1_zb  ", self.Rrj1_zb)
        print(" self.Rrj2_zb  ", self.Rrj2_zb)
        #  ----  软件标题 -----
        self.rj1 = config["配置文件"]["软件1"]
        self.rj2 = config["配置文件"]["软件2"]

        inp11 = config["RJinput"]["num1"]
        inp12 = config["RJinput"]["num2"]
        inp13 = config["RJinput"]["num3"]
        self.l_input.setText(inp11)
        self.ts_input.setText(inp12)
        self.h_input.setText(inp13)

        # 报警形式
        bj1 = config["配置文件"]["声音警报"]
        bj2 = config["配置文件"]["闪烁警报"]

        if bj1 == "开":
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        if bj2 == "开":
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setChecked(False)

        self.rj1_hwnd = win32gui.FindWindow(None, self.rj1)  # 获取句柄
        self.rj2_hwnd = win32gui.FindWindow(None, self.rj2)  # 获取句柄

        self.rj1_date = 0  # 数据存储 运算显示
        self.rj2_date = 0  # 数据存储

        self.rj1_bj_index = 0  # 警报累计计数标志
        self.rj2_bj_index = 0  # 警报累计计数标志
        self.sansuo_True_False = False
        self.leiji_CF = 3  # 累计多少次触发

    def initUISet(self):
        # 初始化一个定时器 用于更新数据
        self.Pz_timer_update = QTimer()
        self.Pz_up_bz = None
        # 设置输入框输入形式 范围和 保留小数位
        self.l_input.setValidator(QDoubleValidator(-1000, 65535, 2))
        self.h_input.setValidator(QDoubleValidator(-1000, 65535, 2))
        self.ts_input.setValidator(QDoubleValidator(-1000, 65535, 2))
        self.btn2.setText("开始计算")

        # self.
        # self.setWindowIcon(QIcon('img/back.jpg'))  # 设置图标
        # self.setWindowTitle("股票数据采集")

        self.label.setText("0")
        self.label.setStyleSheet("background-color:0")
        self.label2.setText("0")
        self.label2.setStyleSheet("background-color:0")
        self.label3.setText("0")
        self.label3.setStyleSheet("background-color:0")

        self.Pz_update_img = QTimer()
    def initConnect(self):
        # 绑定 按钮
        self.btn1.clicked.connect(self.btn1_def)
        self.btn2.clicked.connect(self.btn2_def)
        self.btn3.clicked.connect(self.btn3_def)
        self.btn4.clicked.connect(self.btn4_def)
        self.Pz_timer_update.timeout.connect(self.Pz_init)
        self.checkBox.stateChanged.connect(self.checkBox_def)
        self.checkBox_2.stateChanged.connect(self.checkBox_2_def)

        self.Pz_update_img.timeout.connect(self.updata_img)
        self.Pz_update_img.start(30)

    def initKNN(self):
        initKNNstart = time.time()
        data = []
        target = []
        for index in range(0, 11):
            for i in range(0, 400):  # 0 (1).png
                # print("./datanum3/%d/%d.png"%(index,i))
                try:
                    digits = plt.imread("./data/%d/%d.png" % (index, i))
                    data.append(digits)
                    target.append(index)
                except EnvironmentError as e:
                    print("File open Error ", e)

        data = np.array(data)
        target = np.array(target)
        print("data data.shape[0] : ", data.shape[0])
        self.shapew = data.shape[1]
        self.shapeh = data.shape[2]
        x_data = data.reshape((data.shape[0], -1))  # 结构整形
        self.knn = KNeighborsClassifier(20)  #
        self.knn.fit(x_data, target)  # 训练
        # y_ = self.knn.predict(x_data) # 预测
        print(self.knn.score(x_data, target))
        initKNNend = time.time()
        print("initKNN run time : ", initKNNend - initKNNstart)

    def updata_img(self):

        kk = random.random()   * 1e0
        # self.data = np.append(self.data, np.array([kk], dtype=dtype))
        #self.data.append(kk)
        # np.append(self.data,kk)
        # print("-- > 前  ", self.data)
        # np.concatenate((self.data, [kk]))
        # print("-- > 后  ", self.data)
        self.data.append(kk)
        hui = np.array(self.data)

        self.pw3.clear()
        self.pw3.plot(hui , clickable=True)

        # print("-- > ok updata_img  ",self.data,kk)


    def btn1_def(self):
        self.ts_label1.setText("")
        self.ts_label2.setText("")
        # self.get_img_TWO()

        in_data_low = self.l_input.text()
        in_data_ts = self.ts_input.text()
        in_data_high = self.h_input.text()

        # 保存输入框

        config.read("配置文件.ini", encoding="utf-8-sig")
        config.set("RJinput", "num1", in_data_low)
        config.set("RJinput", "num2", in_data_ts)
        config.set("RJinput", "num3", in_data_high)

        jb1 = self.checkBox.isChecked()
        jb2 = self.checkBox_2.isChecked()

        zt = [in_data_low, in_data_ts, in_data_high, jb1, jb2]
        # writefile(zt)

        # t = threading.Thread(target=self.writefile, args=(zt,), name='funciton')
        # 如果线程有参数
        # t = threading.Thread(target=threadFunction, args=(), name='funciton')
        # t.start()

        if jb1:
            config.set("配置文件", "声音警报", "开")
        else:
            config.set("配置文件", "声音警报", "关")

        if jb2:
            config.set("配置文件", "闪烁警报", "开")
        else:
            config.set("配置文件", "闪烁警报", "关")

        print("更改配置文件 - > 保存当前设置 ")

        config.write(open(filepath, "w", encoding="utf-8-sig"))

        # print("输入低价文本 ", in_data_low,type(in_data_low),float(in_data_low))
        # print("输入提示文本 ", in_data_ts,type(in_data_ts),float(in_data_ts))
        # print("输入高价文本 ", in_data_high,type(in_data_high),float(in_data_high))

        # if self.rj_bj_index == 0:
        #     self.rj_bj_index = 1
        #     self.label.setText("label1")
        #     self.label.setStyleSheet("background-color:0")
        #     self.label2.setText("label2")
        #     self.label2.setStyleSheet("background-color:0")
        #     self.label3.setText("label3")
        #     self.label3.setStyleSheet("background-color:0")
        #
        # else:
        #     self.rj_bj_index = 0
        #     self.label.setText("labelonn")
        #     self.label.setStyleSheet("background-color:red")
        #     self.label2.setText("label2onn")
        #     self.label2.setStyleSheet("background-color:red")
        #     self.label3.setText("label3onn")
        #     self.label3.setStyleSheet("background-color:red")

        # self.l_input.setText("")
        # self.ts_input.setText("")
        # self.h_input.setText("")

        return

    def btn2_def(self):
        self.ts_label1.setText("")
        self.ts_label2.setText("")
        print("Heool  2 ", self.checkBox.isChecked())
        if self.btn2.text() == "开始计算":
            self.btn2.setText("停止计算")
            self.whlie_run = True
            t = threading.Thread(target=self.whileRunnum, name='funciton')
            t.start()
        else:
            self.btn2.setText("开始计算")
            self.whlie_run = False

    # 配置 1 - 2
    def btn3_def(self):  # 配置 软件坐标
        self.ts_label1.setText("")
        self.ts_label2.setText("")
        titlename = self.rj1
        # titlename = "网易有道词典"
        hwnd = win32gui.FindWindow(None, titlename)  # 获取句柄
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取窗口左上角和右下角坐标
        if hwnd == 0:
            self.ts_label1.setText("未找到窗口")
            return
        else:
            self.ts_label1.setText("")
        print(" ---  hwnd  --- ")
        print(hwnd, left, top, right, bottom)
        # x = int((right - left)/2)
        x = right - left
        y = bottom - top
        # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, x, y, win32con.SWP_SHOWWINDOW)
        # HWND_TOPMOST:将窗口置于所有非顶层窗口之上。即使窗口未被激活窗口也将保持顶级位置。
        # SWP_SHOWWINDOW：显示窗口。
        # HWND_TOP:将窗口置于Z序的顶部。
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, x, y, win32con.SWP_SHOWWINDOW)

        config.read(filepath, encoding="utf-8-sig")
        config.set("Rrj1", "x", str(0))
        config.set("Rrj1", "y", str(0))
        config.set("Rrj1", "w", str(x))
        config.set("Rrj1", "h", str(y))
        config.write(open(filepath, "w", encoding="utf-8-sig"))

        self.Pz_up_bz = None
        self.Pz_timer_update.start(1000)
        t = threading.Thread(target=self.jietu, args=("R1",), name='funciton')
        # 如果线程有参数
        # t = threading.Thread(target=threadFunction, args=(), name='funciton')
        t.start()

    def btn4_def(self):
        self.ts_label1.setText("")
        self.ts_label2.setText("")
        titlename = self.rj2
        # titlename = "网易有道词典"
        hwnd = win32gui.FindWindow(None, titlename)  # 获取句柄
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取窗口左上角和右下角坐标
        if hwnd == 0:
            self.ts_label1.setText("未找到窗口")
            return
        else:
            self.ts_label1.setText("")
        print(" ---  hwnd  --- ")
        print(hwnd, left, top, right, bottom)
        # x = int((right - left)/2)
        x = right - left
        y = bottom - top
        # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, x, y, win32con.SWP_SHOWWINDOW)
        # HWND_TOPMOST:将窗口置于所有非顶层窗口之上。即使窗口未被激活窗口也将保持顶级位置。
        # SWP_SHOWWINDOW：显示窗口。
        # HWND_TOP:将窗口置于Z序的顶部。
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, x, y, win32con.SWP_SHOWWINDOW)

        config.read(filepath, encoding="utf-8-sig")
        config.set("Rrj2", "x", str(0))
        config.set("Rrj2", "y", str(0))
        config.set("Rrj2", "w", str(x))
        config.set("Rrj2", "h", str(y))
        config.write(open(filepath, "w", encoding="utf-8-sig"))

        self.Pz_up_bz = None
        self.Pz_timer_update.start(1000)
        t = threading.Thread(target=self.jietu, args=("R2",), name='funciton')
        # 如果线程有参数
        # t = threading.Thread(target=threadFunction, args=(), name='funciton')
        t.start()

    # 识别数据 解析
    def data_jiexi(self, strnum):
        # print("解析 strnum",strnum)
        numstr = ""
        numlist = list(filter(lambda ch: ch in "-0123456789.", strnum))
        if len(numlist) < 1:
            return None
        # print("data_jiexi -- 1")
        if numlist[0] == ".":  # 去除头点误差
            numlist.pop(0)
        # print("data_jiexi -- 2",numlist,len(numlist))
        for i in range(len(numlist)):
            # print(numlist[i],i)
            if numlist[i] == "-" and i != 0:  # 去除头点误差
                numstr += "."
                continue
            numstr += numlist[i]
        # print("data_jiexi -- 3")
        try:
            numdata = float(numstr)
        except:
            print("识别误差+", numstr)
            numdata = None

        return numdata

    # 子线程播放 警示
    def play(self):
        t = threading.Thread(target=self.playau, name='funciton')
        t.start()


    def playau(self):
        print("start -- > 0")
        winsound.Beep(2015, 1000)
        print("end -- > 0")

    def whileRunnum(self):
        while self.whlie_run:
            try:
                hwnd = win32gui.FindWindow(None, "股票数据采集")  # 获取句柄 结束进程
                if hwnd == 0:
                    break  # 结束进程 终结循环
                time.sleep(0.05)
                text1, text2 = self.get_img_TWO()
                if text1 != None:
                    self.rj1_date = text1
                    self.ts_label1.setText("软件1 - >" + str(text1))
                else:
                    self.ts_label1.setText("")
                if text1 != None:
                    self.rj2_date = text2
                    self.ts_label2.setText("软件2 - >" + str(text2))
                else:
                    self.ts_label2.setText("")

                in_data_low = float(self.l_input.text())
                in_data_ts = float(self.ts_input.text())
                in_data_high = float(self.h_input.text())

                # print("运算 -> ",self.rj1_date,type(self.rj1_date),self.rj2_date,type(self.rj2_date))
                if self.rj2_date == None or self.rj1_date == None:
                    continue

                cj = self.rj2_date - self.rj1_date
                low_jia = in_data_low - cj
                hjia_jia = in_data_high - cj

                cj = round(cj, 2)  # 保留两位小数，1.01

                # print("运算 -> cj ", cj, low_jia, hjia_jia)
                jb1 = self.checkBox.isChecked()
                jb2 = self.checkBox_2.isChecked()

                if in_data_low > cj:
                    low_jia = in_data_low - cj
                    low_jia = round(low_jia, 2)  # 保留两位小数，1.01
                    self.label.setText(str(low_jia))
                    # self.label3.setStyleSheet("background-color:0")
                    # print("警报 : ",jb1,jb2)
                    if self.rj1_bj_index > self.leiji_CF:
                        if jb1:
                            self.play()
                        if self.sansuo_True_False and jb2:
                            self.sansuo_True_False = False
                            self.label.setStyleSheet("background-color:red")
                        else:
                            self.sansuo_True_False = True
                            self.label.setStyleSheet("background-color:0")
                    else:
                        self.rj1_bj_index += 1
                else:
                    self.label.setText(str(0))
                    self.rj1_bj_index = 0
                    self.label.setStyleSheet("background-color:0")

                if in_data_high < cj:
                    hjia_jia = cj - in_data_high
                    hjia_jia = round(hjia_jia, 2)  # 保留两位小数，1.01
                    self.label3.setText(str(hjia_jia))
                    # self.label3.setStyleSheet("background-color:0")

                    if self.rj2_bj_index > self.leiji_CF:
                        if jb1:
                            self.play()
                        if self.sansuo_True_False and jb2:
                            self.sansuo_True_False = False
                            self.label3.setStyleSheet("background-color:red")
                        else:
                            self.sansuo_True_False = True
                            self.label3.setStyleSheet("background-color:0")

                    else:
                        self.rj2_bj_index += 1
                else:
                    self.label3.setText(str(0))
                    self.rj2_bj_index = 0
                    self.label3.setStyleSheet("background-color:0")
                self.label2.setText(str(cj))

            except:
                print("input ERROR")
                break

        self.ts_label1.setText("")
        self.ts_label2.setText("")
        self.btn2.setText("开始计算")

        # self.rj1_date = 0
        # self.rj2_date = 0
        # self.rj_bj_index = 0
        # print()
        # try:
        #     num = float(text1)
        #     self.ts_label1.setText(str(num))
        #     print("Yes num1 ",text1,self.whlie_run)
        # except:
        #     print("No num1 Fsk1 -> ",text1,self.whlie_run)
        # try:
        #     num = float(text2)
        #     self.ts_label2.setText(str(num))
        #     print("Yes num2 ",text2,self.whlie_run)
        # except:
        #     print("No Fsk2 -> ",text2,self.whlie_run)

    def checkBox_def(self):
        print("checkBox_def ")

    def checkBox_2_def(self):
        print("checkBox_2_def ")
        # isChecked() # setChecked()  # 设置是否选择，True为选中

    # 更新数据
    def Pz_init(self):
        if self.Pz_up_bz == None:
            self.Pz_timer_update.start(1000)
            return
        # print("Pz_init_endtime",self.Pz_up_bz)  # self.Pz_timer_update.start(1000)  # 两秒钟后更新
        self.Pz_timer_update.stop()  # self.timer.start(1000) 每隔1000毫秒  self.timer.stop() 停止timer
        config.read("配置文件.ini", encoding="utf-8-sig")
        if self.Pz_up_bz == "R1":
            self.R1_zb = [int(config.getfloat(self.Pz_up_bz, "x")),
                          int(config.getfloat(self.Pz_up_bz, "y")),
                          int(config.getfloat(self.Pz_up_bz, "w")),
                          int(config.getfloat(self.Pz_up_bz, "h"))]
        else:
            self.R2_zb = [int(config.getfloat(self.Pz_up_bz, "x")),
                          int(config.getfloat(self.Pz_up_bz, "y")),
                          int(config.getfloat(self.Pz_up_bz, "w")),
                          int(config.getfloat(self.Pz_up_bz, "h"))]
        print(" ------ 配置数据变更 ------------  ")
        print(" self.R1_zb  ", self.R1_zb)
        print(" self.R2_zb  ", self.R2_zb)
        self.Pz_up_bz = None
        return

    def jietu(self, name):
        print("你说", name)
        config.read("配置文件.ini", encoding="utf-8-sig")
        print("更新 配置 ", config[name]["x"], config[name]["y"], config[name]["w"], config[name]["h"])
        ScreenShot(filepath, name)
        print("更新xywh")
        self.Pz_up_bz = name

    def get_img_TWO(self):
        # print("btn1  1 ", self.R1_zb, self.R2_zb, self.rj1_hwnd, type(self.rj1_hwnd))
        if self.rj1_hwnd <= 0:
            self.rj1_hwnd = win32gui.FindWindow(None, self.rj1)  # 获取句柄
            self.rj2_hwnd = win32gui.FindWindow(None, self.rj2)  # 获取句柄
        if self.rj1_hwnd == 0 or self.rj2_hwnd == 0:
            self.ts_label1.setText("未找到窗口,请确认软件已打开")
            return
        left1, top1, right1, bottom1 = win32gui.GetWindowRect(self.rj1_hwnd)  # 获取窗口左上角和右下角坐标
        left2, top2, right2, bottom2 = win32gui.GetWindowRect(self.rj2_hwnd)  # 获取窗口左上角和右下角坐标

        x1 = left1 + self.R1_zb[0]
        y1 = top1 + self.R1_zb[1]
        w1 = self.R1_zb[2] - self.R1_zb[0]
        h1 = self.R1_zb[3] - self.R1_zb[1]

        x2 = left2 + self.R2_zb[0]
        y2 = top2 + self.R2_zb[1]
        w2 = self.R2_zb[2] - self.R2_zb[0]
        h2 = self.R2_zb[3] - self.R2_zb[1]

        Jtxyhw1 = [x1, y1, w1, h1]
        Jtxyhw2 = [x2, y2, w2, h2]

        img1 = pyautogui.screenshot(region=Jtxyhw1)
        img2 = pyautogui.screenshot(region=Jtxyhw2)

        cvimg1 = cv2.cvtColor(numpy.asarray(img1), cv2.COLOR_RGB2BGR)  # 转opencv
        cvimg2 = cv2.cvtColor(numpy.asarray(img2), cv2.COLOR_RGB2BGR)  # 转opencv
        cvimg1 = self.imgThreshold(cvimg1, True)  # 二值化
        cvimg2 = self.imgThreshold(cvimg2, True)  # 二值化
        cvimg1 = cv2.resize(cvimg1, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)  # 图像放大
        cvimg2 = cv2.resize(cvimg2, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)  # 图像放大

        image1 = Image.fromarray(cv2.cvtColor(cvimg1, cv2.COLOR_BGR2RGB))  # 转回PIL
        image2 = Image.fromarray(cv2.cvtColor(cvimg2, cv2.COLOR_BGR2RGB))  # 转回PIL
        # 识别
        text1 = pytesseract.image_to_string(image1, lang="fontyp")
        text2 = pytesseract.image_to_string(image2, lang="fontyp")

        # 数据加工去除特殊符号
        text1 = self.data_jiexi(text1)
        text2 = self.data_jiexi(text2)

        print("get_img_TWO 识别 : ", text1, text2)
        return text1, text2
        # cv.imshow("cvimg1 : ", cvimg1)
        # cv.imshow("cvimg2 : ", cvimg2)

    # -----------  cv2 图片处理  -----------
    # 图像二值化处理
    def imgThreshold(self, img, bitFZ=False):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 要二值化图像，要先进行灰度化处理
        ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 去掉噪，例如过滤很小或很大像素值的图像点。
        if bitFZ == True:
            binary = cv.bitwise_not(binary)  # 即将二值图像白色部分变为黑色，黑色部分变为白色
        return binary

    def verticalCut(self, img, img_num="te"):

        #  去除顶上和底部
        (x, y) = img.shape  # 返回的分别是矩阵的行数和列数，x是行数，y是列数 (646, 83)
        pointCount = np.zeros(x, dtype=np.uint8)  # 每行黑色的个数
        x_axes = np.arange(0, x)
        # print((x, y), pointCount)
        for i in range(0, x):
            for j in range(0, y):
                if (img[i, j] == 0):
                    # print(i)
                    pointCount[i] = pointCount[i] + 1
        plt.plot(x_axes, pointCount)
        start = []
        end = []
        for index in range(1, x):
            # 上个为0当前不为0，即为开始
            if ((pointCount[index] != 0) & (pointCount[index - 1] == 0)):
                start.append(index)
            # 上个不为0当前为0，即为结束
            elif ((pointCount[index] == 0) & (pointCount[index - 1] != 0)):
                end.append(index)
        if len(start) == 1 and len(end) == 1:
            img = img[start[0]:end[0], :]
        else:
            print("垂直截取图片失败,请确认截图区域完整")
            return None

        # # 对照片进行分割
        # print(pointCount)
        #
        # print("垂直")
        # print(start,end)
        # print("--------------------")

        (x, y) = img.shape  # 返回的分别是矩阵的行数和列数，x是行数，y是列数
        pointCount = np.zeros(y, dtype=np.float32)  # 每列黑色的个数
        x_axes = np.arange(0, y)
        # i是列数，j是行数
        tempimg = img.copy()
        for i in range(0, y):
            for j in range(0, x):
                # if j<15:
                if (tempimg[j, i] == 0):
                    pointCount[i] = pointCount[i] + 1
        figure = plt.figure(str(img_num))
        # for num in range(pointCount.size):
        #     pointCount[num]=pointCount[num]
        #     if(pointCount[num]<0):
        #         pointCount[num]=0
        plt.plot(x_axes, pointCount)
        start = []
        end = []
        # 对照片进行分割
        # print(pointCount)
        for index in range(1, y - 1):
            # 上个为0当前不为0，即为开始
            if ((pointCount[index - 1] == 0) & (pointCount[index] != 0)):
                start.append(index)
            # 上个不为0当前为0，即为结束
            elif ((pointCount[index] != 0) & (pointCount[index + 1] == 0)):
                if len(end) < len(start):
                    end.append(index)
        imgArr = []
        bz = 0
        cv2.imshow(str(1555) + "_" + str(1622), img)
        print(" -1-- ---  -- ", start, end, img.shape)
        for idx in range(0, len(start)):
            print(" --2- ---  -- ")
            tempimg = img[:, start[idx]:end[idx]]
            print("tempimg ", tempimg.shape)

            if tempimg.shape[0] == 0 or tempimg.shape[1] == 0:
                print("跳过")
                continue

            img_test1 = cv.resize(tempimg, (self.shapeh, self.shapew))
            print(" ---23 ---  -- ")
            bx = img_test1.reshape((1, -1))  # 结构整形

            # print("img_test1 ",img_test1.shape)

            # cv2.imshow(str(img_num) + "_" + str(idx), img_test1)
            # imgArr.append(tempimg)

            bx_yc = self.knn.predict(bx)
            bz += 1
            cv2.imwrite(img_num + '_' + str(bx_yc) + '.png', tempimg)
            print("预测 ", bz, "  -- ", bx_yc)
            imgArr.append(bx_yc)
        print("预测 bz所有", "  -- ", imgArr)

        # self.shapew

        print("imgArr end", self.shapew, self.shapeh)
        # return imgArr

    # 重构退出
    def closeEvent(self, event):
        print("开始结束")
        self.exitTrheadwhile_kk = False
        self.whlie_run = False
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# mail = self.mailEdit.text()


