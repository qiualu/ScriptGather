
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
# from .ui.sanb import Ui_MainWindow
from datetime import datetime


"""
绘制 折线图
绘制 点 时间x轴 1 
绘制 点 时间x轴 2 
"""

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)

    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()

    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)



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
    # 绘制 折线图 时间轴 可刷新
    def initV1(self):
        pass
        self.axis1 = pg.DateAxisItem(orientation='bottom')
        self.vb1 = CustomViewBox()
        self.pw1 = pg.PlotWidget(viewBox=self.vb1, axisItems={'bottom': self.axis1}, enableMenu=False, title="三金")
        self.v1.addWidget(self.pw1)
        dates = np.arange(8) * (24 * 356)
        self.curve1 =  self.pw1.plot(x=dates, y=[1, 6, 2, 4, 3, 5, 6, 8], symbol='o')

    # 绘制 点 时间x轴
    def initV2(self):
        self.axis2 = pg.DateAxisItem(orientation='bottom')
        self.pw2 = pg.PlotWidget( axisItems={'bottom': self.axis2}, enableMenu=False, title="三金")
        self.v2.addWidget(self.pw2)

        self.pw2datax = [0]
        self.pw2datay = [0]
        self.curve2 = self.pw2.plot(x=self.pw2datax, y=self.pw2datay, symbol='o')

    # 禁用鼠标滚轮，但保持鼠标的其他功能不变
    def initV3(self):
        pass
        self.axis3 = pg.DateAxisItem(orientation='bottom')
        self.vb3 = CustomViewBox()
        self.pw3 = pg.PlotWidget(viewBox=self.vb3, axisItems={'bottom': self.axis3}, enableMenu=False,title="三金")
        self.v3.addWidget(self.pw3)
        self.pw3datax = [0]
        self.pw3datay = [0]

        self.curve3 = self.pw3.plot(x=self.pw3datax, y=self.pw3datay, symbol='o')

    def undateV1(self):
        self.data = np.random.random(size=50)
        # self.pw2datax = [0]
        # self.pw2datay = [0]
        self.curve1.setData(self.data)  #给图形对象设置数据---图形对象重新绘图

    def undateV2(self):
        self.pw2datax.append(self.pw2datax[-1] + 600)
        self.pw2datay.append(random.randint(-9, 9))
        self.curve2.setData(self.pw2datax,self.pw2datay)  #给图形对象设置数据---图形对象重新绘图

        pass
    def undateV3(self):
        pass
        self.pw3datax.append(self.pw3datax[-1] + 600)
        self.pw3datay.append(random.randint(-9, 9))
        self.curve3.setData(self.pw3datax[-50:], self.pw3datay[-50:])  # 给图形对象设置数据---图形对象重新绘图

    def btn1_Fun(self):
        print("btn1_Fun")
        pass

    def update(self):
        # print("123")
        self.undateV1()
        self.undateV2()
        self.undateV3()

    # 事件过滤器
    def eventFilter(self, watched, event):
        if event.type() == QEvent.GraphicsSceneWheel:
            return True
        return self.Dialog.eventFilter(watched, event)

if __name__ == '__main__':
    appexit = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGui(MainWindow)
    MainWindow.show()
    sys.exit(appexit.exec_())