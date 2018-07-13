from .ui_window import Ui_MainWindow
from PyQt5 import QtWidgets


class OPMainWindow(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButon(self.radioButton_add)
        self.button_group.addButon(self.radioButton_substract)
        self.button_group.addButon(self.radioButton_multiply)
        self.button_group.addButon(self.radioButton_divide)
        self.button_group.addButon(self.radioButton_comp)
        self.button_group.addButon(self.radioButton_subs)
        self.button_group.addButon(self.radioButton_cos)
        self.button_group.addButon(self.radioButton_sin)
        self.button_group.addButon(self.radioButton_tan)
        self.button_group.addButon(self.radioButton_pow)

