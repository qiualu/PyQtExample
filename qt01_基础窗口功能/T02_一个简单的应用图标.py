#！/usr/bin/python3
# -*- coding: utf-8 -*-
"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5 一个简单的应用图标

作者：学沫
编辑时间：2018.9.13
"""
import sys,os
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    # 在面向对象编程中有三个重要的东西，分别是类，数据和方法。这里我们创建了一个新类叫做Example。
    # Example类继承自QWidget类。这意味着我们调用了两个构造方法：第一个是Example类的构造方法，
    # 第二个是被继承类的构造方法。super()
    # 方法返回了Example类的父类对象，并且我们调用了父类的构造方法。__init__()方法是Python语言中的构造方法。
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # GUI的创建授予initUI()方法完成。
        # 三个方法都继承自QWidgets类。
        # setGeometry()做了两件事：将窗口在屏幕上显示，并设置了它的尺寸。
        self.setGeometry(300,300,300,220) #setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。
        # 第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。事实上，这是将resize()和move()
        # 方法融合在一个方法内。为了做好这个例子，我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。

        # path = os.path.join(os.getcwd(), 'web.png')
        self.setWindowTitle('Tcon')

        # self.setWindowIcon(QIcon(path))

        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  # 应用和example对象被创建。主循环被启动。



