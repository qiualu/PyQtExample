#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

我们创建了一个切换按钮和一个QWidget，并把QWidget的背景设置为黑色。点击不同的切换按钮，
背景色会在红、绿、蓝之间切换（而且能看到颜色合成的效果，而不是单纯的颜色覆盖）。

作者：十羽
编辑时间：2018.9.22
"""

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QApplication
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        # 设置颜色为黑色。
        self.col = QColor(0,0,0)

        # 创建一个QPushButton，然后调用它的setCheckable()的方法就把这个按钮编程了切换按钮。
        redb = QPushButton('Red',self)
        redb.setCheckable(True)
        redb.move(10,10)

        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值。
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green',self)
        greenb.setCheckable(True)
        greenb.move(10,60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)

        blueb.clicked[bool].connect(self.setColor)


        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget { background-color: %s }' % self.col.name())

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        # 获取被点击的按钮。
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        # 如果是标签为“red”的按钮被点击，就把颜色更改为预设好的对应颜色。
        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        # 使用样式表（就是CSS的SS）改变背景色
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

