#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

控件就像是应用这座房子的一块块砖。PyQt5有很多的控件，比如按钮，单选框，滑动条，复选框等等。
在本章，我们将介绍一些很有用的控件：QCheckBox，ToggleButton，QSlider，QProgressBar和QCalendarWidget。

QCheckBox组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景。

作者：十羽
编辑时间：2018.9.22
"""

import sys
from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt

# 这个例子中，有一个能切换窗口标题的单选框。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 这个是QCheckBox的构造器。
        cb = QCheckBox('Show title',self)
        cb.move(20,20)

        # 要设置窗口标题，我们就要检查单选框的状态。默认情况下，窗口没有标题，单选框未选中。
        cb.toggle()

        # 把changeTitle()方法和stateChanged信号关联起来。这样，changeTitle()就能切换窗口标题了。
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    # 控件的状态是由changeTitle()方法控制的，如果空间被选中，我们就给窗口添加一个标题，如果没被选中，就清空标题。
    def changeTitle(self,state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')

        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




