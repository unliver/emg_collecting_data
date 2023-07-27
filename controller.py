from ui import Ui_Form
from main_ui import Main_Ui_Form

class Controller():

    def __init__(self):
        self.ui = None
        self.main_ui = None

    def show_main_ui(self):
        self.main_ui = Main_Ui_Form()
        if self.ui != None:
            self.ui.close()
        self.main_ui.switch.connect(self.show_ui)
        self.main_ui.show()

    def show_ui(self):
        if self.main_ui != None:
            self.ui = Ui_Form(self.main_ui.imform_text())
            self.main_ui.close()
        self.ui.switch.connect(self.show_main_ui)
        self.ui.show()