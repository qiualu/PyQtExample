#!/usr/bin/python3
# -*- coding:  utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

作者：学沫
编辑时间：2018.9.13
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QMenu,QApplication

# 这个例子里，有两个子菜单，一个在file菜单下面，一个在file的import下面。
class Example(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        # 使用QMenu创建一个新菜单。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # 使用QMenu创建一个新菜单。 Import
        impMenu = QMenu('Import',self)

        # 创造菜单选项 Import mail
        impAct = QAction('Import mail',self)

        # 使用addAction添加一个动作。
        impMenu.addAction(impAct)

        # 创造菜单选项 New
        newAct = QAction('New',self)

        # 菜单file 中添加 New 和 Import
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Submenu')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


