#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

在PyQt5中，事件处理器经常被重写（也就是用自己的覆盖库自带的）。

作者：十羽
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event handler')
        self.show()

    # 这个例子中，我们替换了事件处理器函数keyPressEvent()。
    # 此时如果按下ESC键程序就会退出。
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







