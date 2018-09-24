#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

QObject实例能发送事件信号。下面的例子是发送自定义的信号。
我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定。

作者：十羽
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow,QApplication

# Communicate类创建了一个pyqtSignal()属性的信号。
class Communicate(QObject):

    closeApp = pyqtSignal()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # closeApp信号QMainWindow的close()方法绑定。
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit signal')
        self.show()

    # 点击窗口的时候，发送closeApp信号，程序终止。
    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
