#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

PyQt5有丰富的组件，但是肯定满足不了所有开发者的所有需求，PyQt5只提供了基本的组件，像按钮，文本，滑块等。如果你还需要其他的模块，应该尝试自己去自定义一些。
自定义组件使用绘画工具创建，有两个基本方式：根据已有的创建或改进；通过自己绘图创建。
Burning widget
这个组件我们会在Nero，K3B，或者其他CD/DVD烧录软件中见到。

作者：十羽 拾雨
编辑时间：2018.9.24
"""

import sys
from PyQt5.QtWidgets import QWidget,QSlider,QApplication,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import QObject,Qt,pyqtSignal
from PyQt5.QtGui import QPainter,QFont,QColor,QPen

class Communicate(QObject):

    updateBW = pyqtSignal(int)

class BurningWidget(QWidget):

    def __init__(self):
        super(BurningWidget, self).__init__()
        self.initUI()

    def initUI(self):

        self.setMinimumSize(1,30)
        self.value = 75
        self.num = [75,150,225,300,375,450,525,600,675]

    def setValue(self , value):

        self.value = value

    def paintEvent(self, QPaintEvent):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self,qp):

        MAX_CAPACITY = 700
        OVER_CAPACITY = 750

        font = QFont('Serif',7,QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w/10))

        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

