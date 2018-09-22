#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

对话框是一个现代GUI应用不可或缺的一部分。对话是两个人之间的交流，对话框就是人与电脑之间的对话。对话框用来输入数据，修改数据，修改应用设置等等。
这个示例有一个按钮和一个输入框，点击按钮显示对话框，输入的文本会显示在输入框里。
作者：学沫
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QInputDialog,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input dialog')
        self.show()

    # 这是显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符。
    # 对话框返回输入内容和一个布尔值，如果点击的是OK按钮，布尔值就返回True。
    def showDialog(self):

        text,ok = QInputDialog.getText(self,'Input Dialog','Enter your name:')

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







