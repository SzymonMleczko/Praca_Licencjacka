from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from DBUacces import update,readDBU,readall,restart,benefit


class WindowCalculate(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):	


		calculete()
		self.creatingTables()
		self.show()
		self.setGeometry(900, 950, 900, 950)
		self.setWindowTitle("Wyliczone wartości")
		self.show()

	def creatingTables(self):

		data=readall()
		n=0
		for rec in data:
			if rec['value'] != 0 and rec['name'] != 'current' :
				if int(rec['name']) > 20 :
					n += 1

		vbox = QVBoxLayout()
		label = QLabel()
		label.setText('Do pola na deklaracji PIT o numerze z kolumny numer, należy wpisać liczbę z kolumny wartość')
		vbox.addWidget(label)
		button_clear = QPushButton('Wyczyść dane', self)
		button_clear.clicked.connect(self.on_click_clear)
		vbox.addWidget(button_clear)

		button_back = QPushButton('Wróć', self)
		button_back.clicked.connect(self.on_click_back)
		vbox.addWidget(button_back)

		table = QTableWidget()
		table.setColumnCount(2)
		table.setRowCount(n)
		table.setColumnWidth(0,300)
		table.setColumnWidth(1,100)
		table.move(700,700)
		table.setHorizontalHeaderLabels(['pole','wartość'])
		n=0
		for rec in data:
			if rec['value'] != 0 and rec['name'] != 'current':
				if int(rec['name']) > 20 :
					table.setItem(n,0,QTableWidgetItem(str(rec['name'])))
					table.setItem(n,1,QTableWidgetItem(str(rec['value'])))
					n += 1
		vbox.addWidget(table)
		self.setLayout(vbox)

	def on_click_clear(self):
		restart()
    
	def on_click_back(self):
		self.close()



	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()


def calculete():
	benefit()
	if readDBU('34') or readDBU('36')  or readDBU('38') or readDBU('40'):
		sum = 0
		field = 42
		for x in [52,67,81,82]:
			sum += readDBU(str(x))
			update(str(field),readDBU(str(x)))
			if sum > 85528:
				sum -= 85528
				update(str(field),readDBU(str(x))-sum)
				update(str(x),sum)
				sum = 85528
			else:
				update(str(x),0)
			
			field += 2

		update('50',sum)

	if readDBU('35') or readDBU('37') or readDBU('39') or readDBU('41'):
		sum = 0
		field = 43
		for x in [87,102,116,117]:
			sum += readDBU(str(x))
			update(str(field),readDBU(str(x)))
			if sum > 85528:
				sum -= 85528
				update(str(field),readDBU(str(x))-sum)
				update(str(x),sum)
				sum = 85528
			else:
				update(str(x),0)
			
			field += 2

		update('51',sum)

	for x in [52,62,69,87,97,104]:
		sum = readDBU(str(x))+readDBU(str(x+5))-readDBU(str(x+1))-readDBU(str(x+6))
		if sum >= 0:
			update(str(x+2),sum)
		else:
			update(str(x+3),-sum)
	update('80',readDBU('59'))
	update('95',readDBU('94'))
	for x in [76,111]:
		sum = readDBU(str(x))+readDBU(str(x+5))+readDBU(str(x+6))-readDBU(str(x+1))
		if sum >= 0:
			update(str(x+2),sum)
		else:
			update(str(x+3),-sum)
	sum = readDBU('52')+readDBU('57')+readDBU('59')+readDBU('62')+readDBU('67')+readDBU('69')+readDBU('74')+readDBU('76')+readDBU('81')+readDBU('82')
	update('83',sum)
	sum = readDBU('53')+readDBU('58')+readDBU('63')+readDBU('68')+readDBU('70')+readDBU('75')+readDBU('77')
	update('84',sum)
	sum = readDBU('54')+readDBU('60')+readDBU('64')+readDBU('71')+readDBU('78')-readDBU('55')-readDBU('65')-readDBU('72')-readDBU('79')
	update('85',sum)
	sum = readDBU('56')+readDBU('61')+readDBU('66')+readDBU('73')+readDBU('80')
	update('86',sum)
	sum = readDBU('87')+readDBU('92')+readDBU('94')+readDBU('97')+readDBU('102')+readDBU('104')+readDBU('109')+readDBU('111')+readDBU('116')+readDBU('117')
	update('118',sum)
	sum = readDBU('88')+readDBU('93')+readDBU('98')+readDBU('103')+readDBU('105')+readDBU('110')+readDBU('112')
	update('119',sum)
	sum = readDBU('89')+readDBU('95')+readDBU('99')+readDBU('106')+readDBU('113')-readDBU('90')-readDBU('100')-readDBU('107')-readDBU('114')
	update('120',sum)
	sum = readDBU('91')+readDBU('96')+readDBU('101')+readDBU('108')+readDBU('115')
	update('121',sum)
	if readDBU('122') > readDBU('85'):
		update('122',readDBU('85'))
	if readDBU('123') > readDBU('120'):
		update('123',readDBU('120'))
	limit = readDBU('85')-readDBU('122')
	mlimit = readDBU('120')-readDBU('123')

	if readDBU('124') > limit:
		update('124',limit)
	if readDBU('125') > mlimit:
		update('125',mlimit) 
	if readDBU('126') > limit+mlimit:
		update('126',limit+mlimit)
	update('127',limit+mlimit-readDBU('124')-readDBU('125')-readDBU('126'))
	if readDBU('128') > readDBU('127'):
		update('128', readDBU('127'))
	if readDBU('2') or (readDBU('15') and not readDBU('2')) or readDBU('16'):
		update('129',round((readDBU('127')-readDBU('128'))/2))
	else:
		update('129',round(readDBU('127')-readDBU('128')))
	if readDBU('129') > 120000:
		tax = 10800+(readDBU('129')-120000)*0.32
		update('130',round(tax,2))
	else:
		tax = readDBU('129')*0.12-3600
		
		if tax < 0:
			tax = 0
		update('130',round(tax,2))
	if readDBU('2') or (readDBU('15') and not readDBU('2')) or readDBU('16'):
		update('130',readDBU('130')*2)
	
	tax = readDBU('130')+readDBU('132')
	deduct = readDBU('133')+readDBU('134')
	if deduct > tax:
		deduct -= tax
		if readDBU('133') > deduct:
			update('133',readDBU('133')-deduct)
		else:
			update('133',readDBU('134')-deduct)
		deduct = tax
	update('135',tax-deduct)
	if readDBU('136') > tax-deduct:
		update('136', tax-deduct)
	update('137',round(readDBU('135')-readDBU('136')))
	if readDBU('137')-readDBU('86')-readDBU('121') > 0:
		update('138',readDBU('137')-readDBU('86')-readDBU('121'))
	else:
		update('139',-(readDBU('137')-readDBU('86')-readDBU('121')))
	if readDBU('15'):
		update('140',readDBU('140')+readDBU('122'))
		update('141',readDBU('141')+readDBU('123'))
	if readDBU('142')+readDBU('143') > readDBU('140')+readDBU('141'):
		update('144',readDBU('140')+readDBU('141'))
	else:
		update('144',readDBU('142')+readDBU('143'))
	update('145',readDBU('139')+readDBU('144'))

	


