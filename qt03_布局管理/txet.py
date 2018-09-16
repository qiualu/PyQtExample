import sys
from PyQt5.QtWidgets import QWidget,QGridLayout,QPushButton,QApplication

# 这个例子里，我们创建了栅格化的按钮。
class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        print('开始')

    def initUI(self):

        # 创建一个QGridLayout实例，并把它放到程序窗口里。
        grid = QGridLayout()
        self.setLayout(grid)

        # 这是我们将要使用的按钮的名称。
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        # 创建按钮位置列表。
        positions = [(i,j) for i in range(5) for j in range(4)]
        # print(positions)[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1),
        # (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
        for position,name in zip(positions,names):

            if name == '':
                continue
            # 创建按钮，并使用addWidget()方法把按钮放到布局里面。
            button = QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    print('结束')
    sys.exit(app.exec_())