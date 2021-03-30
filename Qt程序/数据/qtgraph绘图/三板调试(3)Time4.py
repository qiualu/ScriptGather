
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import random
# from ui.sanb import Ui_MainWindow
# from .ui.sanb import Ui_MainWindow
from datetime import datetime
from ui.xbui import Ui_MainWindow

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
        self.curve1 =  self.pw1.plot(x=dates, y=[1, 6, 2, 4, 3, 5, 6, 8], pen=(255,0,0), name="Red curve") # ,  # , symbol='o'

    # 绘制 点 时间x轴
    def initV2(self):
        self.axis2 = pg.DateAxisItem(orientation='bottom')
        self.pw2 = pg.PlotWidget( axisItems={'bottom': self.axis2}, enableMenu=False, title="三金")
        self.LEFT_X = 0
        self.RIGHT_X = 60
        self.pw2.setXRange(self.LEFT_X, self.RIGHT_X) #  设置边界范围

        self.v1.addWidget(self.pw2)

        self.pw2datax = [0]
        self.pw2datay = [0]
        self.curve2 = self.pw2.plot(x=self.pw2datax, y=self.pw2datay)  # , symbol='o'
        # 设置颜色
        self.crosshair_color = (196, 220, 255)
        self.pw2.plotItem.setAutoVisible(y=True)
        self.vertical_line = pg.InfiniteLine(angle=90)
        self.horizontal_line = pg.InfiniteLine(angle=0, movable=False)
        self.vertical_line.setPen(self.crosshair_color)
        self.horizontal_line.setPen(self.crosshair_color)
        self.pw2.setAutoVisible(y=True)
        # self.crosshair_plot_widget.setAutoVisible(y=True)
        self.pw2.addItem(self.vertical_line, ignoreBounds=True)
        self.pw2.addItem(self.horizontal_line, ignoreBounds=True)
        self.crosshair_update = pg.SignalProxy(self.pw2.scene().sigMouseMoved, rateLimit=60,
                                               slot=self.update_XY_V2)
    # 禁用鼠标滚轮，但保持鼠标的其他功能不变
    def initV3(self):
        pass
        self.axis3 = pg.DateAxisItem(orientation='bottom')
        self.vb3 = CustomViewBox()
        self.pw3 = pg.PlotWidget(viewBox=self.vb3, axisItems={'bottom': self.axis3}, enableMenu=False,title="三金")
        self.v1.addWidget(self.pw3)
        self.pw3datax = [0]
        self.pw3datay = [0]

        self.curve3 = self.pw3.plot(x=self.pw3datax, y=self.pw3datay, symbol='o')
    def undateV1(self):
        self.data = np.random.random(size=50)
        # self.pw2datax = [0]
        # self.pw2datay = [0]

        # self.curve1.setData(self.data[0:25], pen="r")  #给图形对象设置数据---图形对象重新绘图

        self.curve1.setData(self.data)
        # self.curve12

    def undateV2(self):
        self.pw2datax.append(self.pw2datax[-1] + 600)
        self.RIGHT_X += 600
        self.pw2.setXRange(self.LEFT_X, self.RIGHT_X)  # 设置边界范围
        self.pw2datay.append(random.randint(-9, 9))
        self.curve2.setData(self.pw2datax,self.pw2datay)  #给图形对象设置数据---图形对象重新绘图

        pass
    def undateV3(self):
        pass
        self.pw3datax.append(self.pw3datax[-1] + 600)
        self.pw3datay.append(random.randint(-9, 9))
        self.curve3.setData(self.pw3datax[-50:], self.pw3datay[-50:])  # 给图形对象设置数据---图形对象重新绘图

    def update_XY_V2(self ,event):
        coordinates = event[0]
        if self.pw2.sceneBoundingRect().contains(coordinates):
            mouse_point = self.pw2.plotItem.vb.mapSceneToView(coordinates)
            index = mouse_point.x()
            if index > self.LEFT_X and index <= self.RIGHT_X:
                timeBH = self.transForm(mouse_point.x())
                self.pw2.setTitle(
                    "<span style='font-size: 12pt'>时间: %s,   <span style='color: red'>价格: %0.1f</span>" % (
                        timeBH, mouse_point.y()))
                print("鼠标 -> ",timeBH, mouse_point.x() ,mouse_point.y())
            self.vertical_line.setPos(mouse_point.x())
            self.horizontal_line.setPos(mouse_point.y())


    def btn1_Fun(self):
        print("btn1_Fun")
        pass
    def update(self):
        # print("123")
        self.undateV1()
        self.undateV2()
        self.undateV3()

    def transForm(self,timeindex):
        # h = int(timeindex / 3600 ) + 8
        # fen = int((timeindex - (3600*h)) / 60)
        h = int(timeindex // 3600) + 8
        fen = int(timeindex % 3600 // 60)
        timeBH = str(h) + ":" + str(fen)
        return timeBH
if __name__ == '__main__':
    appexit = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGui(MainWindow)
    MainWindow.show()
    sys.exit(appexit.exec_())