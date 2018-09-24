#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

噩梦可以使用PyQt5的QPainterPath创建贝塞尔曲线。绘画路径是由许多构建图形的对象，具体表现就是一些线的形状，比如矩形，椭圆，线和曲线。

作者：十羽 拾雨
编辑时间：2018.9.24
"""

import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QPainterPath
from PyQt5.QtCore import Qt

# 这个示例中，我们画出了一个贝塞尔曲线。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,380,250)
        self.setWindowTitle('Bezier curve')
        self.show()

    def paintEvent(self, QPaintEvent):

        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self,qp):

        # 用QPainterPath路径创建贝塞尔曲线。使用cubicTo()方法生成，分别需要三个点：起始点，控制点和终止点。
        path = QPainterPath()
        path.moveTo(30,30)
        path.cubicTo(30,30,200,350,350,30)

        # drawPath() 绘制最后的图像。
        qp.drawPath(path)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







