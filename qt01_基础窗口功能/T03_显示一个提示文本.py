#！/usr/bin/python3
# -*- coding: utf-8 -*-
"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5 显示一个提示文本

作者：学沫
编辑时间：2018.9
"""

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # 在这个例子中，我们为应用创建了一个提示框。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 调用setTooltip()创建提示框可以使用富文本格式的内容。
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 创建一个按钮，并且为按钮添加了一个提示框。
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







