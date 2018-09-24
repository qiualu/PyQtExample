#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

QFontDialog能做字体的选择。

作者：十羽
编辑时间：2018.9.22
"""

import sys
from PyQt5.QtWidgets import (QWidget,QVBoxLayout,QPushButton,
                             QSizePolicy,QLabel,QFontDialog,QApplication)

# 我们创建了一个有一个按钮和一个标签的QFontDialog的对话框，我们可以使用这个功能修改字体样式。

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #布局
        vbox = QVBoxLayout()

        btn = QPushButton('Dialong',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

        btn.move(20,20)
        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters',self)
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):

        # 弹出一个字体选择对话框。getFont()
        # 方法返回一个字体名称和状态信息。状态信息有OK和其他两种。

        font , ok = QFontDialog.getFont()

        # 如果点击OK，标签的字体就会随之更改。
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())





