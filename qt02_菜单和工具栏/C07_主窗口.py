#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作
创建了一个很经典的菜单框架，有右键菜单，工具栏和状态栏。

作者：学沫
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 这里创建了一个文本编辑区域
        textEdit = QTextEdit()
        # 并把它放在QMainWindow的中间区域。这个组件或占满所有剩余的区域。
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300,300,300,250)
        self.setWindowTitle('Main window')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







