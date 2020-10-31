
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import random
from .sanb import Ui_MainWindow


class MainGui(Ui_MainWindow):
    def __init__(self,Dialog):
        super().setupUi(Dialog)
        self.updateTime = QTimer()
        self.updateTime.timeout.connect(self.update)
        self.updateTime.start(500)

        self.initV1()
        self.initV2()
        self.initV3()

    def initV1(self):
        pass

    def initV2(self):
        pass

    def initV3(self):
        pass

    def undateV1(self):
        pass
    def undateV2(self):
        pass
    def undateV3(self):
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