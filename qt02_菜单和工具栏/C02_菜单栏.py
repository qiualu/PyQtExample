#!/usr/bin/python3
# -*- coding : utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

作者：学沫
编辑时间：2018.9.13
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        # 我们创建了只有一个命令的菜单栏，这个命令就是终止应用。
        # 同时也创建了一个状态栏。而且还能使用快捷键Ctrl+Q退出应用。
        # QAction是菜单栏、工具栏或者快捷键的动作的组合。

        # 我们创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作。
        exitAct = QAction(QIcon('exit.png'),'&Exit',self) #前面两行，我们创建了一个图标

        # 快捷键的动作
        exitAct.setShortcut('Ctrl+Q')

        # 创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct.setStatusTip('Exit application')

        # 当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()
        # 行为相关联，所以这个动作就能终止这个应用。
        exitAct.triggered.connect(qApp.quit)

        # 第一次调用创建一个状态栏，返回一个状态栏对象。
        self.statusBar() # .showMessage('Ready')

        # 创建菜单栏。
        menubar = self.menuBar()

        # 这里创建了一个菜单，并在上面添加了一个file菜单
        fileMenu =  menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Simple menu')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

