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
from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QApplication

# 例子中展示了一个编辑组件和一个标签，我们在输入框里键入的文本，会立即在标签里显示出来。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)
        # 创建一个QLineEdit对象。
        qle = QLineEdit(self)

        qle.move(60,100)
        self.lbl.move(60,40)

        # 如果输入框的值有变化，就调用onChanged()方法。
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 在onChanged()方法内部，我们把文本框里的值赋值给了标签组件，
    # 然后调用adjustSize()方法让标签自适应文本内容。
    def onChanged(self,text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



