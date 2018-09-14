#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5 显示一个提示文本

作者：学沫
编辑时间：2018.9.13
"""

import sys,PyQt5
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(1000,300,500,500)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes |
                                     QMessageBox.No,QMessageBox.No)
        # 我们创建了一个消息框，上面有俩按钮：Yes和No.第一个字符串显示在消息框的标题栏，
        # 第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，
        # 这个按钮是默认选中的。返回值在变量reply里。

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






