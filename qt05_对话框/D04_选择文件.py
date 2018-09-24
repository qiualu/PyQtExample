#!/usr/bin/python3
#  -*- coding:utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作

QFileDialog给用户提供文件或者文件夹选择的功能。能打开和保存文件。

作者：十羽
编辑时间：2018.9.22
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QFileDialog,QApplication
from PyQt5.QtGui import QIcon

# 本例中有一个菜单栏，一个置中的文本编辑框，一个状态栏。点击菜单栏选项会弹出一个QtGui.QFileDialog对话框，
# 在这个对话框里，你能选择文件，然后文件的内容就会显示在文本编辑框里。

class Example(QMainWindow):

    # 这里设置了一个文本编辑框，文本编辑框是基于QMainWindow组件的。
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFlie = QAction(QIcon('open.png'),'Open',self)
        openFlie.setShortcut('Ctrl+O')
        openFlie.setStatusTip('Open new File')
        openFlie.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFlie)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        # 弹出QFileDialog窗口。getOpenFileName()
        # 方法的第一个参数是说明文字，第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件。
        fname = QFileDialog.getOpenFileName(self,'Open file','/home/wy/Desktop')

        if fname[0]:
            f = open(fname[0],'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())





