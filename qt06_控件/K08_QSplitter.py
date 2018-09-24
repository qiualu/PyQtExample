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
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QFrame,QSplitter,QStyleFactory,QApplication
from PyQt5.QtCore import Qt

# 三个窗口和两个分割线的布局创建完成了，但是要注意，有些主题下，分割线的显示效果不太好。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        # 为了更清楚的看到分割线，我们使用了设置好的子窗口样式。
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 创建一个QSplitter组件，并在里面添加了两个框架。
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        # 也可以在分割线里面再进行分割。
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChenged(self,text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

