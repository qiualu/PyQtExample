#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

使用盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。QHBoxLayout和QVBoxLayout是基本的布局类，分别是水平布局和垂直布局。

如果我们需要把两个按钮放在程序的右下角，创建这样的布局，我们只需要一个水平布局加一个垂直布局的盒子就可以了。再用弹性布局增加一点间隙。

作者：学沫
编辑时间：2018.9.16
"""

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication


# 上面的例子完成了在应用的右下角放了两个按钮的需求。当改变窗口大小的时候，它们能依然保持在相对的位置。我们同时使用了QHBoxLayout和QVBoxLayout。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 这是创建了两个按钮。
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 创建一个水平布局，增加两个按钮和弹性空间。stretch函数在两个按钮前面增加了一些弹性空间。下一步我们把这些元素放在应用的右下角。
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面。弹性元素会把所有的元素一起都放置在应用的右下角。
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 最后，我们就得到了我们想要的布局。
        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



