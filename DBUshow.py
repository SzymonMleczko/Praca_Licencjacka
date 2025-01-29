
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from DBUacces import readall
from Calculete import WindowCalculate



class WindowDBshow(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):		

		self.cratingTables()
		self.show()
		self.setGeometry(900, 950, 900, 950)
		self.setWindowTitle("Wprowadzone_Wartości")

		self.show()

	def cratingTables(self):

		data=readall()
		n=1
		for rec in data:
			if rec['value'] != 0:
				n += 1

		vbox = QVBoxLayout()

		
		table = QTableWidget()
		table.setColumnCount(2)
		table.setRowCount(n)
		table.setColumnWidth(0,300)
		table.setColumnWidth(1,100)
		table.move(700,700)

		button_calculate= QPushButton('wylicz', self)
		button_calculate.clicked.connect(self.on_click_calculate)
		table.setCellWidget(0,1,button_calculate)

		button_back = QPushButton('Wróć', self)
		button_back.clicked.connect(self.on_click_back)
		table.setCellWidget(0,0,button_back)

		n=1
		for rec in data:
			if rec['value'] != 0:
				table.setItem(n,0,QTableWidgetItem(str(rec['showname'])))
				table.setItem(n,1,QTableWidgetItem(str(rec['value'])))
				n += 1
		vbox.addWidget(table)
		self.setLayout(vbox)
		

	def on_click_calculate(self):
		self.w = WindowCalculate()
		self.w.show()

    
	def on_click_back(self):
		self.close()



	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
