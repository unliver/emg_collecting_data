# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from controller import Controller
from config import *
import os
from qt_material import apply_stylesheet

from main_ui import Main_Ui_Form

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.

extra = {
    'font_size': '20px'
}

if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    apply_stylesheet(app, theme='light_blue.xml', extra = extra)
    my_controller = Controller()
    my_controller.show_main_ui()
    # main_ui = Main_Ui_Form()
    # main_ui.show()
    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
