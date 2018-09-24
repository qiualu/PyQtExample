#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

我们继续介绍PyQt5控件。这次的有QPixmap，QLineEdit，QSplitter，和QComboBox。
QPixmap是处理图片的组件。本例中，我们使用QPixmap在窗口里显示一张图片。

作者：十羽 拾雨
编辑时间：2018.9.23
"""

import sys
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QLabel,QApplication
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        # 创建一个QPixmap对象，接收一个文件作为参数。
        pixmap = QPixmap('mute.png')
        
        # 把QPixmap实例放到QLabel组件里。
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300,200)
        self.setWindowTitle('Red Rock')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
