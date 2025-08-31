from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from DBUacces import update,readDBU,readall,resetuser,benefit


class WindowCalculate(QWidget):

	def __init__(self,user):
		super().__init__()
		self.user= user

		self.initUI()

	def initUI(self):	


		calculete(self.user)
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
		resetuser(self.user)
    
	def on_click_back(self):
		self.close()



	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()

def additions(user):
	if readDBU('20',user):
		sum=readDBU('518',user) + readDBU('519',user)
		update('520',sum,user)
		update('522',sum,user)
		update('128',sum,user)
		sum=readDBU('510',user) - readDBU('511',user)
		update('512',sum,user)
		sum=readDBU('515',user) + readDBU('512',user)
		update('126',sum,user)
		sum=readDBU('529',user) - readDBU('530',user)
		update('531',sum,user)
		sum=readDBU('534',user) + readDBU('531',user)
		update('136',sum,user)
	if readDBU('21',user):
		sum = readDBU('411',user) + readDBU('413',user) + readDBU('415',user) + readDBU('417',user) + readDBU('419',user) + readDBU('421',user) + readDBU('423',user) 
		sum += readDBU('425',user) + readDBU('427',user) + readDBU('429',user) + readDBU('431',user) + readDBU('433',user) + readDBU('435',user) + readDBU('437',user) + readDBU('440',user)
		update('442',sum,user)
		update('124',sum,user)
		sum = readDBU('412',user) + readDBU('414',user) + readDBU('416',user) + readDBU('418',user) + readDBU('420',user) + readDBU('422',user) + readDBU('424',user) 
		sum += readDBU('426',user) + readDBU('428',user) + readDBU('430',user) + readDBU('432',user) + readDBU('434',user) + readDBU('436',user) + readDBU('438',user) + readDBU('441',user)
		update('443',sum,user)
		update('125',sum,user)
		sum= readDBU('444',user) + readDBU('446',user) + readDBU('450',user) + readDBU('452',user) + readDBU('455',user)
		update('457',sum,user)
		update('142',sum,user)
		sum= readDBU('445',user) + readDBU('447',user) + readDBU('451',user) + readDBU('453',user) + readDBU('456',user)
		update('458',sum,user)
		update('143',sum,user)
		


def calculete(user):
	benefit(user)
	additions(user)
	if readDBU('34',user) or readDBU('36',user)  or readDBU('38',user) or readDBU('40',user):
		sum = 0
		field = 42
		for x in [52,67,81,82]:
			sum += readDBU(str(x),user)
			update(str(field),readDBU(str(x),user),user)
			if sum > 85528:
				sum -= 85528
				update(str(field),readDBU(str(x),user)-sum,user)
				update(str(x),sum,user)
				sum = 85528
			else:
				update(str(x),0,user)
			
			field += 2

		update('50',sum,user)

	if readDBU('35',user) or readDBU('37',user) or readDBU('39',user) or readDBU('41',user):
		sum = 0
		field = 43
		for x in [87,102,116,117]:
			sum += readDBU(str(x),user)
			update(str(field),readDBU(str(x),user),user)
			if sum > 85528:
				sum -= 85528
				update(str(field),readDBU(str(x),user)-sum,user)
				update(str(x),sum,user)
				sum = 85528
			else:
				update(str(x),0,user)
			
			field += 2

		update('51',sum,user)

	for x in [52,62,69,87,97,104]:
		sum = readDBU(str(x),user)+readDBU(str(x+5),user)-readDBU(str(x+1),user)-readDBU(str(x+6),user)
		if sum >= 0:
			update(str(x+2),sum,user)
		else:
			update(str(x+3),-sum,user)
	update('80',readDBU('59',user),user)
	update('95',readDBU('94',user),user)
	for x in [76,111]:
		sum = readDBU(str(x),user)+readDBU(str(x+5),user)+readDBU(str(x+6),user)-readDBU(str(x+1),user)
		if sum >= 0:
			update(str(x+2),sum,user)
		else:
			update(str(x+3),-sum,user)
	sum = readDBU('52',user)+readDBU('57',user)+readDBU('59',user)+readDBU('62',user)+readDBU('67',user)+readDBU('69',user)+readDBU('74',user)+readDBU('76',user)+readDBU('81',user)+readDBU('82',user)
	update('83',sum,user)
	sum = readDBU('53',user)+readDBU('58',user)+readDBU('63',user)+readDBU('68',user)+readDBU('70',user)+readDBU('75',user)+readDBU('77',user)
	update('84',sum,user)
	sum = readDBU('54',user)+readDBU('60',user)+readDBU('64',user)+readDBU('71',user)+readDBU('78',user)-readDBU('55',user)-readDBU('65',user)-readDBU('72',user)-readDBU('79',user)
	update('85',sum,user)
	sum = readDBU('56',user)+readDBU('61',user)+readDBU('66',user)+readDBU('73',user)+readDBU('80',user)
	update('86',sum,user)
	sum = readDBU('87',user)+readDBU('92',user)+readDBU('94',user)+readDBU('97',user)+readDBU('102',user)+readDBU('104',user)+readDBU('109',user)+readDBU('111',user)+readDBU('116',user)+readDBU('117',user)
	update('118',sum,user)
	sum = readDBU('88',user)+readDBU('93',user)+readDBU('98',user)+readDBU('103',user)+readDBU('105',user)+readDBU('110',user)+readDBU('112',user)
	update('119',sum,user)
	sum = readDBU('89',user)+readDBU('95',user)+readDBU('99',user)+readDBU('106',user)+readDBU('113',user)-readDBU('90',user)-readDBU('100',user)-readDBU('107',user)-readDBU('114',user)
	update('120',sum,user)
	sum = readDBU('91',user)+readDBU('96',user)+readDBU('101',user)+readDBU('108',user)+readDBU('115',user)
	update('121',sum,user)
	if readDBU('122',user) > readDBU('85',user):
		update('122',readDBU('85',user),user)
	if readDBU('123',user) > readDBU('120',user):
		update('123',readDBU('120',user),user)
	limit = readDBU('85',user)-readDBU('122',user)
	mlimit = readDBU('120',user)-readDBU('123',user)

	if readDBU('124',user) > limit:
		update('124',limit,user)
	if readDBU('125',user) > mlimit:
		update('125',mlimit,user) 
	if readDBU('126',user) > limit+mlimit:
		update('126',limit+mlimit,user)
	update('127',limit+mlimit-readDBU('124',user)-readDBU('125',user)-readDBU('126',user),user)
	if readDBU('128',user) > readDBU('127',user):
		update('128', readDBU('127',user),user)
	if readDBU('2',user) or (readDBU('15',user) and not readDBU('2',user)) or readDBU('16',user):
		update('129',round((readDBU('127',user)-readDBU('128',user))/2),user)
	else:
		update('129',round(readDBU('127',user)-readDBU('128',user)),user)
	if readDBU('129',user) > 120000:
		tax = 10800+(readDBU('129',user)-120000)*0.32
		update('130',round(tax,2),user)
	else:
		tax = readDBU('129',user)*0.12-3600
		
		if tax < 0:
			tax = 0
		update('130',round(tax,2),user)
	if readDBU('2',user) or (readDBU('15',user) and not readDBU('2',user)) or readDBU('16',user):
		update('130',readDBU('130',user)*2,user)
	
	tax = readDBU('130',user)+readDBU('132',user)
	deduct = readDBU('133',user)+readDBU('134',user)
	if deduct > tax:
		deduct -= tax
		if readDBU('133',user) > deduct:
			update('133',readDBU('133',user)-deduct,user)
		else:
			update('133',readDBU('134',user)-deduct,user)
		deduct = tax
	update('135',tax-deduct,user)
	if readDBU('136',user) > tax-deduct:
		update('136', tax-deduct,user)
	update('137',round(readDBU('135',user)-readDBU('136',user)),user)
	if readDBU('137',user)-readDBU('86',user)-readDBU('121',user) > 0:
		update('138',readDBU('137',user)-readDBU('86',user)-readDBU('121',user),user)
	else:
		update('139',-(readDBU('137',user)-readDBU('86',user)-readDBU('121',user)),user)
	if readDBU('15',user):
		update('140',readDBU('140',user)+readDBU('122',user),user)
		update('141',readDBU('141',user)+readDBU('123',user),user)
	if readDBU('142',user)+readDBU('143',user) > readDBU('140',user)+readDBU('141',user):
		update('144',readDBU('140',user)+readDBU('141',user),user)
	else:
		update('144',readDBU('142',user)+readDBU('143',user),user)
	update('145',readDBU('139',user)+readDBU('144',user),user)

	


