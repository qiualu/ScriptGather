

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

        app = pg.mkQApp()
        self.axis = pg.DateAxisItem(orientation='bottom')
        self.vb = CustomViewBox()
        self.pw = pg.PlotWidget(show=True,  axisItems={'bottom': self.axis}, enableMenu=False, title="三金")
        dates = np.arange(8) * (24 * 356)
        self.pw.plot(x=dates, y=[1, 6, 2, 4, 3, 5, 6, 8], symbol='o')
        # self.pw.show()
        # self.pw.setWindowTitle('pyqtgraph example: customPlot')

        self.axis1 = pg.DateAxisItem(orientation='bottom')
        self.vb1 = CustomViewBox()
        self.p1 = pg.PlotWidget(show=True,  axisItems={'bottom': self.axis1}, enableMenu=False, title="紧紧三金")
        self.v1.addWidget(self.p1)

        self.p2 = pg.PlotWidget(show=True)
        # self.p2 = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False,title="三金")
        #self.p2 = pg.PlotWidget( axisItems={'bottom': axis}, enableMenu=False, title="三金")
        #self.v2.addWidget(self.p2)
        self.v2.addWidget(self.pw)
        self.p3 = pg.PlotWidget()
        self.v3.addWidget(self.p3)
        # pw = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False, title="三金")
        # dates = np.arange(8) * (3600 * 24 * 356 * -1)
        # self.p2.plot(x=dates, y=[1, 6, 2, 4, 3, 5, 6, 8] , symbol='o')
        # self.p2.show()
        # self.p2.setWindowTitle('pyqtgraph example: customPlot')



        # self.p1.setDownsampling(mode='peak')
        # self.p1.setClipToView(True)
        # self.p1.setLimits(xMax=0)


        # self.data1 = np.empty(1,dtype=np.int32)
        # self.data1 = [0]
        # self.ptr1 = 0

        # print(self.curve1,self.data1,self.ptr1)

        self.pushButton.clicked.connect(self.btn1_def)

        self.data1 = np.random.normal(size=300)
        self.curve1 = self.p1.plot(self.data1)
        # self.curve2 = self.p2.plot(self.data1)
        self.ptr1 = 0

        self.p2.setDownsampling(mode='peak')
        self.p2.setClipToView(True)
        self.p2.setRange(xRange=[-100, 0])
        self.p2.setLimits(xMax=0)
        self.curve2 = self.p2.plot()
        self.data2 = np.empty(5)
        self.ptr2 = 0

        self.p1x = [0,0]
        self.p1y = [0,0]
        self.ptr1 = 0


        self.p2x = [0]
        self.p2y = [0]

        self.p3.setDownsampling(mode='peak')
        self.p3.setClipToView(True)
        self.p3.setRange(xRange=[-100, 0])
        self.p3.setLimits(xMax=0)
        self.curve3 = self.p3.plot()
        self.data3 = np.empty(5)
        self.ptr3 = 0

    def btn1_def(self):
        print(" -- > ")
        # 一区
        self.p1x[self.ptr1] = self.p1x[self.ptr1-1] + 600
        self.p1y[self.ptr1] = random.randint(-9,9)
        self.ptr1 += 1
        if self.ptr1 >= len(self.p2y):
            tmp = self.p1y
            self.p1y = self.p1y + [0] * 30
            self.p1y[:len(tmp)] = tmp
            tmp = self.p1x
            self.p1x = self.p1x + [0] * 30
            self.p1x[:len(tmp)] = tmp




        # 二区
        # self.data3[self.ptr3] = random.random()
        # self.ptr3 += 1
        self.p2x.append(self.p2x[-1]+600)
        self.p2y.append(random.randint(-9,9))

        # self.p2.plot(x=self.p2x, y=self.p2y, symbol='o')

        xshuchu = self.p2x[-5:]
        yshuchu = self.p2y[-5:]
        print("输出 -- > ",xshuchu, yshuchu)
        self.pw.plot(x=xshuchu, y=yshuchu, symbol='o')


        # self.curve3.setData(self.data3[:self.ptr3])
        # self.curve3.setPos(-self.ptr3, 0)

        # 三区
        self.data3[self.ptr3] = random.random()
        self.ptr3 += 1
        if self.ptr3 >= self.data3.shape[0]:
            tmp = self.data3
            self.data3 = np.empty(self.data3.shape[0] * 2)
            self.data3[:tmp.shape[0]] = tmp
        self.curve3.setData(self.data3[:self.ptr3])
        self.curve3.setPos(-self.ptr3, 0)
        print(self.data3.shape, self.ptr3, self.data3.shape[0], self.data3.dtype, np.random.normal())
        # print(np.random.normal(),type(np.random.normal()),np.random.normal().dtype)

        return

        # self.data1[:-1] = self.data1[1:]  # shift data in the array one sample left
        # # (see also: np.roll)
        # self.data1[-1] = np.random.normal()
        # self.curve1.setData(self.data1)
        # print(self.data1.shape)
        # print(" --  3  -- ")
        # self.data3[self.ptr3] = random.random()
        # self.ptr3 += 1
        # if self.ptr3 >= self.data3.shape[0]:
        #     tmp = self.data3
        #     self.data3 = np.empty(self.data3.shape[0] * 2)
        #     self.data3[:tmp.shape[0]] = tmp
        # self.curve3.setData(self.data3[:self.ptr3])
        # self.curve3.setPos(-self.ptr3, 0)
        # print(self.data3.shape,self.ptr3,self.data3.shape[0],self.data3.dtype,np.random.normal())
        # #print(np.random.normal(),type(np.random.normal()),np.random.normal().dtype)




if __name__ == '__main__':
    appexit = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGui(MainWindow)
    MainWindow.show()
    sys.exit(appexit.exec_())