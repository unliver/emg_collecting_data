from PyQt5.QtGui import QPalette, QBrush

from config import *

class direct_img(QWidget):
    def __init__(self, flag):
        super(direct_img, self).__init__()
        self.flag = flag
        self.setMinimumSize(500,380)
        self.setMaximumSize(500,380)
        self._background = None

        if flag == 1:
            self.innerWidget_1= QWidget(self)
            self.innerWidget_1.setGeometry(60,100,40,40)
            self.innerWidget_1.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('1')
            print('1')
            layout.addWidget(label)
            self.innerWidget_1.setLayout(layout)

            self.innerWidget_2 = QWidget(self)
            self.innerWidget_2.setGeometry(250,140,40,40)
            self.innerWidget_2.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('2')
            layout.addWidget(label)
            self.innerWidget_2.setLayout(layout)

            self.innerWidget_3 = QWidget(self)
            self.innerWidget_3.setGeometry(100,220,40,40)
            self.innerWidget_3.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('8')
            layout.addWidget(label)
            self.innerWidget_3.setLayout(layout)

            self.innerWidget_4 = QWidget(self)
            self.innerWidget_4.setGeometry(300,200,40,40)
            self.innerWidget_4.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('4')
            layout.addWidget(label)
            self.innerWidget_4.setLayout(layout)
        else:
            self.innerWidget_1 = QWidget(self)
            self.innerWidget_1.setGeometry(200, 160, 40,40)
            self.innerWidget_1.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('5')
            layout.addWidget(label)
            self.innerWidget_1.setLayout(layout)

            self.innerWidget_2 = QWidget(self)
            self.innerWidget_2.setGeometry(150, 180, 40,40)
            self.innerWidget_2.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('6')
            layout.addWidget(label)
            self.innerWidget_2.setLayout(layout)

            self.innerWidget_3 = QWidget(self)
            self.innerWidget_3.setGeometry(400, 220, 40,40)
            self.innerWidget_3.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('7')
            layout.addWidget(label)
            self.innerWidget_3.setLayout(layout)

            self.innerWidget_4 = QWidget(self)
            self.innerWidget_4.setGeometry(300, 160, 40,40)
            self.innerWidget_4.setStyleSheet("background-color: green;border-radius: 20px")

            layout = QHBoxLayout()
            label = QLabel('3')
            layout.addWidget(label)
            self.innerWidget_4.setLayout(layout)

        # self.innerWidget_b = QWidget(self)
        # self.innerWidget_b.setStyleSheet("background-color: red;")
        # self.inner_button = QPushButton("push")
        # # self.inner_button.clicked.connect(self.change_color())
        # layout = QHBoxLayout()
        # layout.addWidget(self.inner_button)
        # self.innerWidget_b.setLayout(layout)

    def change_color(self, n, power):
        # 根据参数值计算颜色，这里假设参数范围在0到255之间
        # print("change:{}".format(power))
        if power > 1:
            red = int(1/power*255)
            green = int((1-1/power)*255)
            blue = 0
        else:
            red = 255
            green = 0
            blue = 0
        color = QColor(red,green,blue)
        if n == 1:
            self.innerWidget_1.setStyleSheet("background-color: {};border-radius: 20px".format(color.name()))
        elif n == 2:
            # print(red)
            self.innerWidget_2.setStyleSheet("background-color: {};border-radius: 20px".format(color.name()))
        elif n == 3:
            self.innerWidget_3.setStyleSheet("background-color: {};border-radius: 20px".format(color.name()))
        elif n == 4:
            self.innerWidget_4.setStyleSheet("background-color: {};border-radius: 20px".format(color.name()))

    def reset_color(self):
        self.innerWidget_1.setStyleSheet("background-color: green;border-radius: 20px")
        self.innerWidget_2.setStyleSheet("background-color: green;border-radius: 20px")
        self.innerWidget_3.setStyleSheet("background-color: green;border-radius: 20px")
        self.innerWidget_4.setStyleSheet("background-color: green;border-radius: 20px")


    def setBackground(self):
        if self.flag == 1:
            self._background = QPixmap("后.png")
        else:
            self._background = QPixmap("前.png")
        self.update()

    def paintEvent(self, event):
        if self._background:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self._background)