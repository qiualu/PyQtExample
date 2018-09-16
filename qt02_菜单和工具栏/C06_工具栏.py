#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

作者：学沫
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Toolbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



