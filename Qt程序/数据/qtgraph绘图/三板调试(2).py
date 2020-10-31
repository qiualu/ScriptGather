
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import random
from ui.sanb import Ui_MainWindow


"""


"""


class MainGui(Ui_MainWindow):
    def __init__(self,Dialog):
        super().setupUi(Dialog)
        self.updateTime = QTimer()
        self.updateTime.timeout.connect(self.update)
        self.updateTime.start(500)
        self.Dialog = Dialog
        self.initV1()
        self.initV2()
        self.initV3()
        self.initBtn()

    def initBtn(self):
        self.btn1.clicked.connect(self.btn1_Fun)

    def initV1(self):
        # pw = pg.PlotWidget(self.Dialog,title="绘图")  # 创建一个绘图控件
        self.pw = pg.PlotWidget(title="绘图")  # 创建一个绘图控件
        self.v1.addWidget(self.pw) # 添加到容器中
        # self.pw.resize(600, 300) # 充满容器
        self.data = np.random.random(size=50)
        self.curve1 = self.pw.plot(self.data)  # 在绘图控件中绘制图形

    def initV2(self):
        a = np.random.random(50)
        b = np.random.random(10)
        c = np.r_[a, b]
        pg.plot(a, title='Plot a')  # 产生一个窗口并绘制图形

        # y轴的值就是数组a的值
        # x轴的值就是a中的第几个数据
        # 把各点连成一条曲线
        pg.plot(b, title='Plot b')

    def initV3(self):
        pass

    def undateV1(self):
        self.data = np.random.random(size=50)
        self.curve1.setData(self.data)  #给图形对象设置数据---图形对象重新绘图


    def undateV2(self):
        pass
    def undateV3(self):
        pass

    def btn1_Fun(self):
        print("btn1_Fun")
        pass

    def update(self):
        # print("123")
        self.undateV1()
        self.undateV2()
        self.undateV3()


if __name__ == '__main__':
    appexit = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGui(MainWindow)
    MainWindow.show()
    sys.exit(appexit.exec_())