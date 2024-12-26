# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import  QApplication
from recorder import RecordingAppInterface

class Aplicacion(QApplication):
	
	def __init__(self):
		QApplication.__init__(self, sys.argv)
		interface = RecordingAppInterface()

		sys.exit(self.exec_())

def main():
	app = Aplicacion()
	return 0


if __name__ == '__main__':
    main()