from PyQt5.QtWidgets import *
from DBUacces import checkuser,confirmpassword,createuser,check,resetall,checkUexuist,restartusers
from PyQt5.QtCore import pyqtSignal

class WindowUser(QDialog):
	

	def __init__(self):
		super(WindowUser, self).__init__()

		self.initUI()



	def initUI(self):

		self.label = QLabel(self)
		self.label.setText('Login:')
		self.label.resize(800,20)
		self.label.move(20,80)

		self.textbox = QLineEdit(self)
		self.textbox.move(20, 100)
		self.textbox.resize(280,40)



		self.label1 = QLabel(self)
		self.label1.setText("Hasło:")
		self.label1.move(20,160)

		self.textbox1 = QLineEdit(self)
		self.textbox1.move(20, 180)
		self.textbox1.resize(280,40) 

		self.button_log = QPushButton('Zaloguj', self)
		self.button_log.move(300,400)
		self.button_log.clicked.connect(self.on_click_log)

		self.button_new = QPushButton('Nowy', self)
		self.button_new.move(400,400)
		self.button_new.clicked.connect(self.on_click_new)

		self.button_return = QPushButton('Wróć', self)
		self.button_return.move(500,400)
		self.button_return.clicked.connect(self.on_click_return)
	
		if checkUexuist():
			restartusers()

		if check():
			resetall()

		self.show()
		self.setGeometry(500, 550, 800, 550)
		self.setWindowTitle("Login ")
		self.show()    
	
	def on_click_new(self):
		login = self.textbox.text()
		password = self.textbox1.text()
		if not checkuser(login):
			QMessageBox.question(self, 'Message ', "Login już istnieje: " + login, QMessageBox.Ok, QMessageBox.Ok)
		else:
			createuser(login, password)
			self.user = login
			self.accept()

		
	
	def on_click_log(self):
		login = self.textbox.text()
		password = self.textbox1.text()
		if checkuser(login):
			if confirmpassword(login, password):
				self.user = login
				self.accept()

			else:
				QMessageBox.question(self, 'Message ', "Nie poprawne hasło: " + password, QMessageBox.Ok, QMessageBox.Ok)
		else:
			QMessageBox.question(self, 'Message ', "Nie poprawny login: " + login, QMessageBox.Ok, QMessageBox.Ok)

	
	def on_click_return(self):
       		self.reject()



