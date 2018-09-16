#!/usr/bin/python3
# -*- coding:  utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作
本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏。

作者：学沫
编辑时间：2018.9.15
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 创建状态栏
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menuber = self.menuBar()
        viewMenu = menuber.addMenu('View')

        # 用checkable选项创建一个能选中的菜单。
        viewStatAct = QAction('View statusbar',self,checkable=True)
        viewStatAct.setStatusTip('view statusbar 左下角状态栏')

        # 默认设置为选中状态。
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu) # triggered 触发的；起动的；有扳机的

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Check menu')
        self.show()

    # 依据选中状态切换状态栏的显示与否。程序预览：
    def toggleMenu(self,statr):
        if statr:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




