#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

QColorDialog提供颜色的选择。

作者：学沫
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QColorDialog,QApplication
from PyQt5.QtGui import QColor

# 例子里有一个按钮和一个QFrame，默认的背景颜色为黑色，我们可以使用QColorDialog改变背景颜色。
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 初始化QtGui.QFrame的背景颜色。
        col = QColor(0,0,0)

        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('color dialog')
        self.show()





    def showDialog(self):

        # 弹出一个QColorDialog对话框。
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())













