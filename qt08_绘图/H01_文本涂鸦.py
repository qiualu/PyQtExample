#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

PyQt5绘图系统能渲染矢量图像、位图图像和轮廓字体文本。一般会使用在修改或者提高现有组件的功能，或者创建自己的组件。使用PyQt5的绘图API进行操作。
绘图由paintEvent()方法完成，绘图的代码要放在QPainter对象的begin()和end()方法之间。是低级接口。
文本涂鸦
我们从画一些Unicode文本开始。

作者：十羽 拾雨
编辑时间：2018.9.23
"""

import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

# 写了一些文本上下居中对齐的俄罗斯Cylliric语言的文字。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Drawing text')
        self.show()

    # 在绘画事件内完成绘画动作。
    def paintEvent(self, event):

        # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()方法之间完成，绘画动作都封装在drawText()内部了。
        qp = QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end()

    def drawText(self,event,qp):

        # 为文字绘画定义了笔和字体。
        qp.setPen(QColor(168,34,3))
        qp.setFont(QFont('Decorative',10))

        # drawText() 方法在窗口里绘制文本，rect()方法返回要更新的矩形区域。
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())





