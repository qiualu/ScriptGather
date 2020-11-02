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




class MainGui(Ui_MainWindow):
    def __init__(self,Dialog):
        super().setupUi(Dialog)
        self.updateTime = QTimer()
        self.updateTime.timeout.connect(self.update)
        self.updateTime.start(500)
        self.Dialog = Dialog
        self.initV1()

    # 绘制 折线图 时间轴 可刷新
    def initV1(self):
        pass


        # # Use for time.sleep (s)
        # self.FREQUENCY = .025
        # # Use for timer.timer (ms)
        # self.TIMER_FREQUENCY = self.FREQUENCY * 1000

        self.LEFT_X = -10
        self.RIGHT_X = 0
        # self.x_axis = np.arange(self.LEFT_X, self.RIGHT_X, self.FREQUENCY)
        # self.buffer = int((abs(self.LEFT_X) + abs(self.RIGHT_X)) / self.FREQUENCY)
        # self.data = []

        self.crosshair_plot_widget = pg.PlotWidget()
        self.crosshair_plot_widget.setXRange(self.LEFT_X, self.RIGHT_X)
        # self.crosshair_plot_widget.setLabel('left', 'Value')
        # self.crosshair_plot_widget.setLabel('bottom', 'Time (s)')
        self.crosshair_color = (196, 220, 255)

        self.crosshair_plot = self.crosshair_plot_widget.plot()

        # self.layout = QtGui.QGridLayout()
        # self.layout.addWidget(self.crosshair_plot_widget)
        self.v1.addWidget(self.crosshair_plot_widget)

        # self.crosshair_plot_widget.plotItem.setAutoVisible(y=True)
        self.vertical_line = pg.InfiniteLine(angle=90)
        self.horizontal_line = pg.InfiniteLine(angle=0, movable=False)

        self.vertical_line.setPen(self.crosshair_color)
        self.horizontal_line.setPen(self.crosshair_color)

        # self.crosshair_plot_widget.setAutoVisible(y=True)
        self.crosshair_plot_widget.addItem(self.vertical_line, ignoreBounds=True)
        self.crosshair_plot_widget.addItem(self.horizontal_line, ignoreBounds=True)

        self.crosshair_update = pg.SignalProxy(self.crosshair_plot_widget.scene().sigMouseMoved, rateLimit=60,
                                               slot=self.update_crosshair)

        #self.start()

    def undateV1(self):


        pass
        #self.curve1.setData(self.data)  #给图形对象设置数据---图形对象重新绘图
        # self.crosshair_plot


    def update_crosshair(self, event):
        """Paint crosshair on mouse"""

        coordinates = event[0]
        if self.crosshair_plot_widget.sceneBoundingRect().contains(coordinates):
            mouse_point = self.crosshair_plot_widget.plotItem.vb.mapSceneToView(coordinates)
            index = mouse_point.x()
            if index > self.LEFT_X and index <= self.RIGHT_X:
                self.crosshair_plot_widget.setTitle(
                    "<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y=%0.1f</span>" % (
                    mouse_point.x(), mouse_point.y()))
            self.vertical_line.setPos(mouse_point.x())
            self.horizontal_line.setPos(mouse_point.y())





    def update(self):
        # print("123")
        self.undateV1()


if __name__ == '__main__':
    appexit = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGui(MainWindow)
    MainWindow.show()
    sys.exit(appexit.exec_())