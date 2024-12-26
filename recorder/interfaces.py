# -*- Coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
#from .plugins.pyqt5_custom import MessageCustom, InputCustom, ButtonCustom, BoxInfoCustom, TableWidgetCustom, MultipleLayoutWidgetCustom
#from config import Settings, Routes

class RecordingAppInterface(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Censura Audio'
        self.left = 0
        self.top = 0
        self.width = 450
        self.height = 550
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.show()

    