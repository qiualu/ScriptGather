
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
class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        # print("TimeAxisItem -> ",values,len(values), scale, spacing)
        return [datetime.fromtimestamp(value) for value in values]


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
    # 绘制 折线图
    def initV1(self):
        # pw = pg.PlotWidget(self.Dialog,title="绘图")  # 创建一个绘图控件
        self.pw1 = pg.PlotWidget(title="绘图")  # 创建一个绘图控件
        self.v1.addWidget(self.pw1) # 添加到容器中
        # self.pw.resize(600, 300) # 充满容器
        self.data = np.random.random(size=50)
        self.curve1 = self.pw1.plot(self.data)  # 在绘图控件中绘制图形

    # 绘制 点 时间x轴
    def initV2(self):
        list_x = [datetime(2018, 3, 1, 9, 36, 50, 136415),
                  datetime(2018, 3, 1, 9, 36, 51, 330912),
                  datetime(2018, 3, 1, 9, 36, 51, 382815),
                  datetime(2018, 3, 1, 9, 36, 52, 928818)]

        list_y = [10, 9, 12, 11]
        date_axis = TimeAxisItem(orientation='bottom')
        self.pw2 = pg.PlotWidget(axisItems={'bottom': date_axis})
        self.v2.addWidget(self.pw2)  # 添加到容器中
        self.pw2.plot(x=[x.timestamp() for x in list_x], y=list_y, pen=None, symbol='o')
        self.pw2.show()
    # 禁用鼠标滚轮，但保持鼠标的其他功能不变
    def initV3(self):
        self.pw3 = pg.PlotWidget(show=True)
        # self.p2 = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False,title="三金")
        # self.p2 = pg.PlotWidget( axisItems={'bottom': axis}, enableMenu=False, title="三金")
        # self.v2.addWidget(self.p2)
        self.v3.addWidget(self.pw3)

        # xshuchu = self.p2x[-5:]
        # yshuchu = self.p2y[-5:]
        # print("输出 -- > ", xshuchu, yshuchu)
        # self.pw3.plot(x=xshuchu, y=yshuchu, symbol='o')

        dates = np.arange(8) * (24 * 356)
        self.pw3.plot(x=dates, y=[1, 6, 2, 4, 3, 5, 6, 8], symbol='o')

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