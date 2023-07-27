from PyQt5.QtGui import QFont

from config import *
from qt_material import apply_stylesheet

class clock(QWidget):

    trigger = pyqtSignal()

    def __init__(self, time):
        super(clock, self).__init__()
        self.setMinimumSize(300,300)
        self.time = time    #所要记的时

        self.t = self.time

        self.setup_clock()

    def setup_clock(self):
        self.setFixedSize(200,200)

        #垂直布局类QVBoxLayout
        layout = QVBoxLayout()
        # 显示屏
        w = QWidget(self)
        w.setMinimumSize(100,100)
        layout_in = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        # self.lcdNumber.setStyleSheet('QLCDNumber { font-size: 24px; }')
        # self.lcdNumber.setProperty('class', 'mylcd')
        # self.lcdNumber.setStyleSheet('''
        #     QLCDNumber {
        #         font-size: 30px; /* 设置字体大小为30像素 */
        #     }
        # ''')
        # self.lcdNumber.setStyleSheet(
        #     "QLCDNumber {{\n"
        #     "font-size: 16px;\n"
        #     "}}"
        # )
        self.lcdNumber.setDigitCount(2)
        # self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        # font = self.lcdNumber.font()
        # font.setPointSize(20)
        # self.lcdNumber.setFont(font)
        layout_in.addWidget(self.lcdNumber)
        w.setLayout(layout_in)
        self.lcdNumber.display(self.time)
        layout.addWidget(w)

        self.label = QLabel(self)
        self.label.setText("时间")
        # 创建字体对象
        font = QFont()
        # 设置字体的点大小
        font.setPointSize(12)
        self.label.setFont(font)
        layout.addWidget(self.label)


        self.timer = QTimer()
        # 每次计时结束，触发 countTime
        self.timer.timeout.connect(self.countTime)

        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

    def work(self):
        # 计时器每秒计数
        # print("begin_clock")
        # self.timer.timeout.connect(self.countTime)
        self.timer.start(1000)
        # print("end_clock")

    def countTime(self):
        self.time -= 1
        # LED显示数字+1
        self.lcdNumber.display(self.time)
        print(self.time)
        if self.time == 0:
            self.timer.stop()
            self.time = self.t
            self.trigger.emit()
            print("end")

