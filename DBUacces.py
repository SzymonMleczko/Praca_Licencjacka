import sqlite3
#user Admin password 'baza1podatek'





con = sqlite3.connect('DBUser.db')

con.row_factory = sqlite3.Row

cur = con.cursor()
list_available = [1,2,3,5,7,9,11,13,15]

def restart():

	cur.executescript("""
		DROP TABLE IF EXISTS data;
		CREATE TABLE IF NOT EXISTS data (
		id INTEGER PRIMARY KEY ASC,
		name varchar(50) NOT NULL,
		value float(250) NOT NULL,
		showname varchar(250) NOT Null
		)""")

	record = (
		(None,'current',1, 'Aktualna Pozycja w PIT'),
		(None,'1',0,'Płeć'),
		(None,'2',0, 'Rozliczenie z małżonkiem'),
		(None,'3',0,'Wiek'),
		(None,'4',0,'Wiek małżonka'),
		(None,'5',0,'Praca na Etacie'),
		(None,'6',0,'Praca na etacie małżonka'),
		(None,'7',0,'Praca wykonywana osobiście'),
		(None,'8',0,'Praca wykonywana osobiście małżonka'),
		(None,'9',0,'Przychody z Praw Autorskich i innych praw'),
		(None,'10',0,'Przychody z Praw Autorskich i innych praw małżonka'),
		(None,'11',0,'Inne źródła przychodów'),
		(None,'12',0,'Inne źródła przychodów małżonka'),
		(None,'13',0,'Świadczenia od państwa'),
		(None,'14',0,'Świadczenia od państwa małżonka'),

		(None,'15',0,'Dzici w rodzinie'),
		(None,'16',0,'Wdowiec/Wdowa'),

		(None,'34',0,'Ulga dla młodych'),
		(None,'35',0,'Ulga dla młodych małżonka'),	
		(None,'36',0, 'Powrót do kraju po 2021'),
		(None,'37',0, 'Powrót do kraju po 2021 małżonka'),
		(None,'38',0,'W rodzinie jest ponad trójka dzieci'),
		(None,'39',0,'W rodzinie jest ponad trójka dzieci małżonka'),	
		(None,'40',0,'Pracujący senior'),
		(None,'41',0,'Pracujący senior małżonka'),

		(None,'42',0,'Przychody na etacie'),
		(None,'43',0,'Przychody na etacie małżonka'),
		(None,'44',0,'Przychody z umów zlecenia lub o dzieło od firmy lub właściciela nieruchomości'),
		(None,'45',0,'Przychody z umów zlecenia lub o dzieło od firmy lub właściciela nieruchomości małżonka'),
		(None,'46',0,'Przychody praktyk absolwenckich lub staży uczniowskich'),
		(None,'47',0,'Przychody praktyk absolwenckich lub staży uczniowskich małżonka'),
		(None,'48',0,'Przychody z zasiłku macieżyńskiego'),
		(None,'49',0,'Przychody z zasiłku macieżyńskiego małżonka'),
		(None,'50',0,'Razem D.2'),
		(None,'51',0,'Razem D.2 małżonka'),

		(None,'52',0,'Przychody na etacie opodatkowanie zgodnie z kosztami'),
		(None,'53',0,'Koszty uzyskania przychodu na etacie opodatkowanie zgodnie z kosztami'),
		(None,'54',0,'Dochód na etacie'),
		(None,'55',0,'Strata na etacie'),
		(None,'56',0,'Zaliczki na podatek z pracyna etacie '),
		(None,'57',0,'Przychody na etacie opodatkowanie 50%'),
		(None,'58',0,'Koszty uzyskania przychodu na etacie 50%'),
		(None,'59',0,'Przychody emerytura, renta, inne krajowe świadczenia'),
		(None,'60',0,'Dochód emerytura, renta, inne krajowe świadczenia'),
		(None,'61',0,'Zaliczka emerytura, renta, inne krajowe świadczenia'),
		(None,'62',0,'Przychody działalność wykonywana osobiście opodatkowanie zgodnie z kosztami'),
		(None,'63',0,'Koszty uzyskania przychodu działalność wykonywana osobiście opodatkowanie zgodnie z kosztami'),
		(None,'64',0,'Dochód działalność wykonywana osobiście'),
		(None,'65',0,'Strata działalność wykonywana osobiście'),
		(None,'66',0,'Zaliczki na podatek z działalność wykonywana osobiście '),
		(None,'67',0,'Przychody działalność wykonywana osobiście na zlecenie lub umowe o dzieło'),
		(None,'68',0,'Koszty uzyskania przychodu działalność wykonywana osobiście na umowe zlecenie lub umowe o dzieło'),
		(None,'69',0,'Przychody z praw autorskich opodatkowanie zgodnie z kosztami'),
		(None,'70',0,'Koszty uzyskania przychodu z praw autorskich opodatkowanie zgodnie z kosztami'),
		(None,'71',0,'Dochód z praw autorskich'),
		(None,'72',0,'Strata z praw autorskich'),
		(None,'73',0,'Zaliczki na podatek z pracyz praw autorskich '),
		(None,'74',0,'Przychody z praw autorskich opodatkowanie 50%'),
		(None,'75',0,'Koszty uzyskania przychodu z praw autorskich 50%'),
		(None,'76',0,'Przychody inne żródła opodatkowanie zgodnie z kosztami'),
		(None,'77',0,'Koszty uzyskania przychodu inne żródła opodatkowanie zgodnie z kosztami'),
		(None,'78',0,'Dochód inne żródła'),
		(None,'79',0,'Strata inne żródła'),
		(None,'80',0,'Zaliczki na podatek z pracyinne żródła '),
		(None,'81',0,'Przychody inne żródła opodatkowanie = praktyki absolwenckie i staże uczniowskie'),
		(None,'82',0,'Przychody inne żródła opodatkowania - zasiłek macierzyński'),
		(None,'83',0,'Przychody razem'),
		(None,'84',0,'Koszty razem'),
		(None,'85',0,'Dochód razem'),
		(None,'86',0,'Zaliczka razem'),
		
		(None,'87',0,'Przychody na etacie opodatkowanie zgodnie z kosztami małżonka'),
		(None,'88',0,'Koszty uzyskania przychodu na etacie opodatkowanie zgodnie z kosztami małżonka'),
		(None,'89',0,'Dochód na etacie małżonka'),
		(None,'90',0,'Strata na etacie małżonka'),
		(None,'91',0,'Zaliczki na podatek z pracyna etacie  małżonka'),
		(None,'92',0,'Przychody na etacie opodatkowanie 50% małżonka'),
		(None,'93',0,'Koszty uzyskania przychodu na etacie 50% małżonka'),
		(None,'94',0,'Przychody emerytura, renta, inne krajowe świadczenia małżonka'),
		(None,'95',0,'Dochód emerytura, renta, inne krajowe świadczenia małżonka'),
		(None,'96',0,'Zaliczka emerytura, renta, inne krajowe świadczenia małżonka'),
		(None,'97',0,'Przychody działalność wykonywana osobiście opodatkowanie zgodnie z kosztami małżonka'),
		(None,'98',0,'Koszty uzyskania przychodu działalność wykonywana osobiście opodatkowanie zgodnie z kosztami małżonka'),
		(None,'99',0,'Dochód działalność wykonywana osobiście małżonka'),
		(None,'100',0,'Strata działalność wykonywana osobiście małżonka'),
		(None,'101',0,'Zaliczki na podatek z działalność wykonywana osobiście małżonka'),
		(None,'102',0,'Przychody działalność wykonywana osobiście opodatkowanie 50% małżonka'),
		(None,'103',0,'Koszty uzyskania przychodu działalność wykonywana osobiście 50% małżonka'),
		(None,'104',0,'Przychody z praw autorskich opodatkowanie zgodnie z kosztami małżonka'),
		(None,'105',0,'Koszty uzyskania przychodu z praw autorskich opodatkowanie zgodnie z kosztami małżonka'),
		(None,'106',0,'Dochód z praw autorskich małżonka'),
		(None,'107',0,'Strata z praw autorskich małżonka'),
		(None,'108',0,'Zaliczki na podatek z pracyz praw autorskich małżonka'),
		(None,'109',0,'Przychody z praw autorskich opodatkowanie 50% małżonka'),
		(None,'110',0,'Koszty uzyskania przychodu z praw autorskich 50% małżonka'),
		(None,'111',0,'Przychody inne żródła opodatkowanie zgodnie z kosztami małżonka'),
		(None,'112',0,'Koszty uzyskania przychodu inne żródła opodatkowanie zgodnie z kosztami małżonka'),
		(None,'113',0,'Dochód inne żródła małżonka'),
		(None,'114',0,'Strata inne żródła małżonka'),
		(None,'115',0,'Zaliczki na podatek z pracyinne żródła małżonka'),
		(None,'116',0,'Przychody inne żródła opodatkowanie = praktyki absolwenckie i staże uczniowskie małżonka'),
		(None,'117',0,'Przychody inne żródła opodatkowania - zasiłek macierzyński małżonka'),
		(None,'118',0,'Przychody razem małżonka'),
		(None,'119',0,'Koszty razem małżonka'),
		(None,'120',0,'Dochód razem małżonka'),
		(None,'121',0,'Zaliczka razem małżonka'),

		(None,'122',0,'Składki na ubezpieczenia społeczne'),
		(None,'123',0,'Składki na ubezpieczenia społeczne małżonka'),
		(None,'124',0,'Odliczenia od dochodu- wykazane w części B załącznika PIT/O'),
		(None,'125',0,'Odliczenia od dochodu- wykazane w części B załącznika PIT/O małżonka'),
		(None,'126',0,'Ulga odsetkowa - wykazane w części B.1 załącznika PIT/D'),
		(None,'127',0,'Dochód po odliczeniach'),
		(None,'128',0,'Odliczenia mieszkaniowe - wykazane w części B.3 . załącznika PIT/D'),
		(None,'129',0,'Podstawa obliczenia podatku'),
		(None,'130',0,'Obliczony podatek według skali'),
		(None,'132',0,'Doliczenia do podatku '),
		(None,'133',0,'Doliczenia do podatku - wykazane w części C załącznika PIT/O'),
		(None,'134',0,'Doliczenia do podatku - wykazane w części C załącznika PIT/O małżonka'),
		(None,'135',0,'Podatek po odliczeniach'),
		(None,'136',0,'Odliczenia mieszkaniowe - wykazane w części C.2 . załącznika PIT/D'),
		(None,'137',0,'Podatek należny'),
		(None,'138',0,'Podatek do zapłaty'),
		(None,'139',0,'Nadpłata podatku'),
		(None,'140',0,'Składki na ubezpieczenia społeczne i zdrowotne'),
		(None,'141',0,'Składki na ubezpieczenia społeczne i zdrowotne małżonka'),
		(None,'142',0,'Różnica między kwotami PIT/O ulga na dzieci'),
		(None,'143',0,'Różnica między kwotami PIT/O ulga na dzieci małżonka'),
		(None,'144',0,'Dodatkowy zwrot'),
		(None,'145',0,'Łączny zwrot'),
		(None,'146',0,'Dochody art. 45 ust 3c'),
		)


   	 # wstawiamy wiele rekordów
	cur.executemany('INSERT INTO data VALUES(?,?,?,?)', record)

   	 # zatwierdzamy zmiany w bazie
	con.commit()
	global list_available
	list_available = [1,2,3,5,7,9,11,13,15]


    # pobieranie danych z bazy
def readall():
	cur.execute("""
		SELECT * FROM data""")
	record = cur.fetchall()
	return record
	

def update(name,val):
	cur.execute("""
		UPDATE data SET value=? WHERE name=?""", (val, name))
	con.commit()

def readDBU(nazwa):
	cur.execute("SELECT * FROM data WHERE data.name=?",[nazwa])
	record = cur.fetchall()
	return record[0]['value']

def current():
	cur.execute("SELECT * FROM data WHERE data.name=?",['current'])
	record=cur.fetchall()
	return record[0]['value']

def next(curr):
	if curr == 999:
		return 999
	elif curr < 15:
		a = list_available.index(curr)
		return list_available[a+1]
	else:
		if len(list_available) < 10:
			create_list()
		a = list_available.index(curr)
		return list_available[a+1]
def prev(curr):
	if curr == 1:
		return 1

	elif curr == 999:
		return list_available[len(list_available)-2]

	else:
		if len(list_available) < 10:
			create_list()
		a = list_available.index(curr)
		return list_available[a-1]
def create_list():
	global list_available
	gender = readDBU('1')
	age = readDBU('3')
	mage = readDBU('4')
	if not readDBU('1'):
		list_available.append(16)

	if age < 27 or (mage < 27 and mage != 0):
		list_available.append(34)
	if readDBU('15') and not readDBU('2'):  # jeśli wrodzinie są dzieci i osoba rozlicza się samotnie
		list_available.append(35)
	list_available.append(36)
	if gender:
		if age > 64 or mage > 59:
			list_available.append(40)
	else:
		if age > 59 or mage > 64:
			list_available.append(40)
	if readDBU('5') > 0 or readDBU('6') > 0:  # praca na etacie
		list_available += [52,53,56,57,58]
	if readDBU('13') > 0 or readDBU('14') > 0: # świadczenia państwowe
		list_available += [59,61]
	if readDBU('7') > 0 or readDBU('8') > 0: # praca wykonana osobiście
		list_available += [62,63,66,67,68]
	if readDBU('9') > 0 or readDBU('10') > 0: # Prawa autorskie
		list_available += [69,70,73,74,75]
	if readDBU('11') > 0 or readDBU('12') > 0: # inne źródła
		list_available += [76,77,80,81,82]
	list_available += [122,124,126,128,132,133,136,146]
	if readDBU('15'):
		list_available += [140,142]
	list_available.append(999)


def benefit():
	gender = readDBU('2')
	age = readDBU('3')
	mage = readDBU('4')
	if age < 27 or (mage < 27 and mage != 0):
		if readDBU('34'):
			update('34',0)
		elif age < 27:
			update('34',1)
		if readDBU('35'):
			update('35',0)
		elif (mage < 27 and mage != 0):
			update('35',1)
	if gender:
		if age > 64:
			if readDBU('40'):
				update('40',0)
			else:
				update('40',1)
		if mage > 59 :
			if readDBU('41'):
				update('41',0)
			else:
				update('41',1)
			
	else:
		if age > 59:
			if readDBU('40'):
				update('40',0)
			else:
				update('40',1)
		if mage > 64:
			if readDBU('41'):
				update('41',0)
			else:
				update('41',1)
def check():
	table = cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='data'""").fetchall()
	
	if table == []:
		return True
	else:
		return False