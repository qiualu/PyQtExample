#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

作者：学沫
编辑时间：2018.9.13
"""

# QMainWindow提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏。

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication


# 状态栏是由QMainWindow创建的。
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
        # 第一次调用创建一个状态栏，返回一个状态栏对象。
        self.statusBar().showMessage('Ready') #showMessage()方法在状态栏上显示一条信息。

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






