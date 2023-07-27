from PyQt5.QtGui import QFont

from config import *
from qt_material import apply_stylesheet

class MyQComboBox(QWidget):
    def __init__(self):
        super(MyQComboBox, self).__init__()
        # self.setMinimumSize(200,200)
        self.init_UI()

    def init_UI(self):

        layout = QVBoxLayout()

        self.label = QLabel('Please choose the experience')
        # 创建字体对象
        font = QFont()
        # 设置字体的点大小
        font.setPointSize(12)
        self.label.setFont(font)


        self.cb = QComboBox()
        self.cb.addItem('experience_1')
        self.cb.addItem('experience_2')
        self.cb.addItem('experience_3')
        self.cb.addItem('experience_4')
        # self.cb.addItem('experience_5')

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        layout.setAlignment(Qt.AlignVCenter)

        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))

        print('current index', i, 'selection changed', self.cb.currentText())

class Main_Ui_Form(QWidget):

    switch = pyqtSignal()

    def __init__(self):

        super(Main_Ui_Form, self).__init__()

        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("EMG 肌电采集")
        self.setFixedSize(1000, 500)

        self.pushButton = QPushButton("begin")
        font = QFont()
        # 设置字体的点大小
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.start_collect)
        self.pushButton.setFixedSize(200, 100)

        self.combobox = MyQComboBox()

        self.label_name = QLabel('Name:')
        # 创建字体对象
        font = QFont()
        # 设置字体的点大小
        font.setPointSize(20)
        self.label_name.setFont(font)
        self.edit_name = QLineEdit('Please input the name')
        self.label_name.setFixedSize(200,30)
        self.edit_name.setFixedSize(200,30)
        self.label_name.setBuddy(self.edit_name)

        layout = QVBoxLayout()

        w = QWidget(self)
        w.setFixedSize(500, 100)

        layout_name = QHBoxLayout()
        layout_name.addWidget(self.label_name)
        layout_name.addWidget(self.edit_name)
        layout_name.setAlignment(Qt.AlignLeft)

        w.setLayout(layout_name)

        layout.addWidget(w)

        layout.addWidget(self.combobox)

        w2 = QWidget(self)
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.pushButton)
        w2.setLayout(layout_button)

        layout.addWidget(w2)

        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

    def start_collect(self):
        self.switch.emit()

    def imform_text(self):
        imformation = []
        imformation.append(self.combobox.cb.currentText())
        imformation.append(self.edit_name.text())
        print(imformation)
        return imformation
