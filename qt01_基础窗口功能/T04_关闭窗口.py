#！/usr/bin/python3
# -*- coding: utf-8 -*-


# 关闭一个窗口最直观的方式就是点击标题栏的那个叉，这个例子里，我们展示的是如何用程序关闭一个窗口。
# 这里我们将接触到一点single和slots的知识。
# 本例使用的是QPushButton组件类。
# QPushButton(string text, QWidget parent = None)
# text参数是想要显示的按钮名称，parent参数是放在按钮上的组件，在我们的 例子里，这个参数是QWidget。
# 应用中的组件都是一层一层（继承而来的？）的，
# 在这个层里，大部分的组件都有自己的父级，没有父级的组件，是顶级的窗口。


"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5 显示一个提示文本

作者：学沫
编辑时间：2018.9
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

# 这里创建了一个点击之后就退出窗口的按钮。
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 创建一个继承自QPushButton的按钮。第一个参数是按钮的文本，第二个参数是按钮的父级组件，这个例子中，父级组件就是我们创建的继承自Qwidget的Example类。
    # def initUI(self):父级组件就是我们创建的继承自Qwidget的Example父级组件就是我们创建的继承自Qwidget的Example类。
    # def initUI(self):类。
    def initUI(self):

        # 程序需要QtCore对象。
        qbtn = QPushButton('Quit',self)

        # 创建一个继承自QPushButton的按钮。第一个参数是按钮的文本，第二个参数是按钮的父级组件，这个例子中，
        # 父级组件就是我们创建的继承自Qwidget的Example类。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

















