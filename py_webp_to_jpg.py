from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import sys
import os 


class Webp_to_Jpg(QtWidgets.QWidget):
	"""docstring for Png_to_Jpg"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.file_path = ""
		self.setWindowTitle("Webp to Jpg Converter")
		self.ui()
		self.show()

	def ui(self):

		self.label_1 = QLabel("Select the Webp file ")
		self.select_btn = QPushButton('Browse..',self)
		self.type_space = QLineEdit('')
		self.download_btn = QPushButton('Convert',self)

		
		hbox = QHBoxLayout()
		hbox.addWidget(self.type_space)
		hbox.addWidget(self.select_btn)
		hbox.addWidget(self.download_btn)
		
		vbox = QVBoxLayout()
		vbox.addWidget(self.label_1)
		vbox.addLayout(hbox)


		self.setLayout(vbox)
		self.select_btn.clicked.connect(lambda x : self.select_path() )
		self.download_btn.clicked.connect(lambda x : self.convert_png_to_jpg())

	def select_path(self):

		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.file_path, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "", options=options)
		self.type_space.setText(self.file_path)


	def convert_webp_to_jpg(self):
		try:
			im = Image.open(self.file_path)
			rgb_im = im.convert("RGB")
			save_path = self.download_path()
			rgb_im.save(save_path)
		except:
			pass

	def download_path(self):
		path, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","Untitled.jpg","All Files (*);;Text Files (*.txt)")
		return path


if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = Webp_to_Jpg()
	sys.exit(App.exec())
