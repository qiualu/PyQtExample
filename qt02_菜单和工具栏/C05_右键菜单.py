#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程
在这个例子中, 我们用PyQt5 进行一个羞羞的操作
右键菜单也叫弹出框（！？），是在某些场合下显示的一组命令。例如，Opera浏览器里，网页上的右键菜单里会有刷新，返回或者查看页面源代码。
如果在工具栏上右键，会得到一个不同的用来管理工具栏的菜单。
作者：学沫
编辑时间：2018.9.15
"""

import sys
from PyQt5.QtWidgets import QMainWindow,qApp,QMenu,QApplication

class Example(QMainWindow):
    def __init__(self):

        super().__init__()
        self.initUI()
    def initUI(self):

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self,event):  # 事件函数，event

        cmenu = QMenu(self)

        # 创建3个右键菜单
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")

        # 使用exec_() 方法显示菜单。从鼠标右键事件对象中获得当前坐标。mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        # 如果右键菜单里触发了事件，也就触发了推出事件，我们就关闭菜单。
        if action == quitAct:
            qApp.quit()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
