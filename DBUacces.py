import sqlite3
#user admin password 'baza1podatek'





con = sqlite3.connect('DBUser.db')

con.row_factory = sqlite3.Row

cur = con.cursor()
list_available = [0,1,2,3,5,7,9,11,13,15]
def restartusers():
	
	cur.executescript("""
		DROP TABLE IF EXISTS users;
		CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY ASC,
		name varchar(50) NOT NULL,
		password varchar(250) NOT NULL
		)""")

	record = (None,'admin','admin')

		


   	 # wstawiamy wiele rekordów
	cur.execute('INSERT INTO users VALUES(?,?,?)', (record))

   	 # zatwierdzamy zmiany w bazie
	con.commit()
	if check:
		if checkU('admin'):
			create('admin')

def createuser(name,password):
	cur.execute('INSERT INTO users VALUES(?,?,?)',(None,name,password))
	con.commit()
	create(name)

def confirmpassword(name, password):

	cur.execute('SELECT * FROM users WHERE users.name=?',[name])
	
	paswor = cur.fetchall()
	
	return password == paswor[0]['password']

def checkuser(name):
	
	table = cur.execute("""SELECT name FROM users WHERE users.name=?""",[name])
	if table == []:
		return False
	else:
		return True
def checkUexuist():
	table = cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='users'""").fetchall()
	
	if table == []:
		return False
	else:
		return True


def resetall():
	cur.executescript("""
		DROP TABLE IF EXISTS data;
		CREATE TABLE IF NOT EXISTS data (
		id INTEGER PRIMARY KEY ASC,
		name varchar(50) NOT NULL,
		value float(250) NOT NULL,
		showname varchar(250) NOT Null,
		user varchar(250) NOT NULL
		)""")
	create('admin')
def resetuser(user):

	cur.execute("""
		UPDATE data SET value=0 WHERE user=?
	""",user)

def create(name):

	

	record = (
		(None,'current',1, 'Aktualna Pozycja w PIT',name),
		(None, '0',0,'Gotowy',name),
		(None,'1',0,'Płeć',name),
		(None,'2',0, 'Rozliczenie z małżonkiem',name),
		(None,'3',0,'Wiek',name),
		(None,'4',0,'Wiek małżonka',name),
		(None,'5',0,'Praca na Etacie',name),
		(None,'6',0,'Praca na etacie małżonka',name),
		(None,'7',0,'Praca wykonywana osobiście',name),
		(None,'8',0,'Praca wykonywana osobiście małżonka',name),
		(None,'9',0,'Przychody z Praw Autorskich i innych praw',name),
		(None,'10',0,'Przychody z Praw Autorskich i innych praw małżonka',name),
		(None,'11',0,'Inne źródła przychodów',name),
		(None,'12',0,'Inne źródła przychodów małżonka',name),
		(None,'13',0,'Świadczenia od państwa',name),
		(None,'14',0,'Świadczenia od państwa małżonka',name),

		(None,'15',0,'Dzici w rodzinie',name),
		(None,'20',0,'PIT/D',name),
        	(None,'21',0,'PIT/O',name),
        	(None,'25',0,'PIT-11',name),


		(None,'26',0,'Wdowiec/Wdowa',name),

		(None,'34',0,'Ulga dla młodych',name),
		(None,'35',0,'Ulga dla młodych małżonka',name),	
		(None,'36',0, 'Powrót do kraju po 2021',name),
		(None,'37',0, 'Powrót do kraju po 2021 małżonka',name),
		(None,'38',0,'W rodzinie jest ponad trójka dzieci',name),
		(None,'39',0,'W rodzinie jest ponad trójka dzieci małżonka',name),	
		(None,'40',0,'Pracujący senior',name),
		(None,'41',0,'Pracujący senior małżonka',name),

		(None,'42',0,'Przychody na etacie',name),
		(None,'43',0,'Przychody na etacie małżonka',name),
		(None,'44',0,'Przychody z umów zlecenia lub o dzieło od firmy lub właściciela nieruchomości',name),
		(None,'45',0,'Przychody z umów zlecenia lub o dzieło od firmy lub właściciela nieruchomości małżonka',name),
		(None,'46',0,'Przychody praktyk absolwenckich lub staży uczniowskich',name),
		(None,'47',0,'Przychody praktyk absolwenckich lub staży uczniowskich małżonka',name),
		(None,'48',0,'Przychody z zasiłku macieżyńskiego',name),
		(None,'49',0,'Przychody z zasiłku macieżyńskiego małżonka',name),
		(None,'50',0,'Razem D.2',name),
		(None,'51',0,'Razem D.2 małżonka',name),

		(None,'52',0,'Przychody na etacie opodatkowanie zgodnie z kosztami',name),
		(None,'53',0,'Koszty uzyskania przychodu na etacie opodatkowanie zgodnie z kosztami',name),
		(None,'54',0,'Dochód na etacie',name),
		(None,'55',0,'Strata na etacie',name),
		(None,'56',0,'Zaliczki na podatek z pracyna etacie ',name),
		(None,'57',0,'Przychody na etacie opodatkowanie 50%',name),
		(None,'58',0,'Koszty uzyskania przychodu na etacie 50%',name),
		(None,'59',0,'Przychody emerytura, renta, inne krajowe świadczenia',name),
		(None,'60',0,'Dochód emerytura, renta, inne krajowe świadczenia',name),
		(None,'61',0,'Zaliczka emerytura, renta, inne krajowe świadczenia',name),
		(None,'62',0,'Przychody działalność wykonywana osobiście opodatkowanie zgodnie z kosztami',name),
		(None,'63',0,'Koszty uzyskania przychodu działalność wykonywana osobiście opodatkowanie zgodnie z kosztami',name),
		(None,'64',0,'Dochód działalność wykonywana osobiście',name),
		(None,'65',0,'Strata działalność wykonywana osobiście',name),
		(None,'66',0,'Zaliczki na podatek z działalność wykonywana osobiście ',name),
		(None,'67',0,'Przychody działalność wykonywana osobiście na zlecenie lub umowe o dzieło',name),
		(None,'68',0,'Koszty uzyskania przychodu działalność wykonywana osobiście na umowe zlecenie lub umowe o dzieło',name),
		(None,'69',0,'Przychody z praw autorskich opodatkowanie zgodnie z kosztami',name),
		(None,'70',0,'Koszty uzyskania przychodu z praw autorskich opodatkowanie zgodnie z kosztami',name),
		(None,'71',0,'Dochód z praw autorskich',name),
		(None,'72',0,'Strata z praw autorskich',name),
		(None,'73',0,'Zaliczki na podatek z pracyz praw autorskich ',name),
		(None,'74',0,'Przychody z praw autorskich opodatkowanie 50%',name),
		(None,'75',0,'Koszty uzyskania przychodu z praw autorskich 50%',name),
		(None,'76',0,'Przychody inne żródła opodatkowanie zgodnie z kosztami',name),
		(None,'77',0,'Koszty uzyskania przychodu inne żródła opodatkowanie zgodnie z kosztami',name),
		(None,'78',0,'Dochód inne żródła',name),
		(None,'79',0,'Strata inne żródła',name),
		(None,'80',0,'Zaliczki na podatek z pracyinne żródła ',name),
		(None,'81',0,'Przychody inne żródła opodatkowanie = praktyki absolwenckie i staże uczniowskie',name),
		(None,'82',0,'Przychody inne żródła opodatkowania - zasiłek macierzyński',name),
		(None,'83',0,'Przychody razem',name),
		(None,'84',0,'Koszty razem',name),
		(None,'85',0,'Dochód razem',name),
		(None,'86',0,'Zaliczka razem',name),
		
		(None,'87',0,'Przychody na etacie opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'88',0,'Koszty uzyskania przychodu na etacie opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'89',0,'Dochód na etacie małżonka',name),
		(None,'90',0,'Strata na etacie małżonka',name),
		(None,'91',0,'Zaliczki na podatek z pracyna etacie  małżonka',name),
		(None,'92',0,'Przychody na etacie opodatkowanie 50% małżonka',name),
		(None,'93',0,'Koszty uzyskania przychodu na etacie 50% małżonka',name),
		(None,'94',0,'Przychody emerytura, renta, inne krajowe świadczenia małżonka',name),
		(None,'95',0,'Dochód emerytura, renta, inne krajowe świadczenia małżonka',name),
		(None,'96',0,'Zaliczka emerytura, renta, inne krajowe świadczenia małżonka',name),
		(None,'97',0,'Przychody działalność wykonywana osobiście opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'98',0,'Koszty uzyskania przychodu działalność wykonywana osobiście opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'99',0,'Dochód działalność wykonywana osobiście małżonka',name),
		(None,'100',0,'Strata działalność wykonywana osobiście małżonka',name),
		(None,'101',0,'Zaliczki na podatek z działalność wykonywana osobiście małżonka',name),
		(None,'102',0,'Przychody działalność wykonywana osobiście opodatkowanie 50% małżonka',name),
		(None,'103',0,'Koszty uzyskania przychodu działalność wykonywana osobiście 50% małżonka',name),
		(None,'104',0,'Przychody z praw autorskich opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'105',0,'Koszty uzyskania przychodu z praw autorskich opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'106',0,'Dochód z praw autorskich małżonka',name),
		(None,'107',0,'Strata z praw autorskich małżonka',name),
		(None,'108',0,'Zaliczki na podatek z pracyz praw autorskich małżonka',name),
		(None,'109',0,'Przychody z praw autorskich opodatkowanie 50% małżonka',name),
		(None,'110',0,'Koszty uzyskania przychodu z praw autorskich 50% małżonka',name),
		(None,'111',0,'Przychody inne żródła opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'112',0,'Koszty uzyskania przychodu inne żródła opodatkowanie zgodnie z kosztami małżonka',name),
		(None,'113',0,'Dochód inne żródła małżonka',name),
		(None,'114',0,'Strata inne żródła małżonka',name),
		(None,'115',0,'Zaliczki na podatek z pracyinne żródła małżonka',name),
		(None,'116',0,'Przychody inne żródła opodatkowanie = praktyki absolwenckie i staże uczniowskie małżonka',name),
		(None,'117',0,'Przychody inne żródła opodatkowania - zasiłek macierzyński małżonka',name),
		(None,'118',0,'Przychody razem małżonka',name),
		(None,'119',0,'Koszty razem małżonka',name),
		(None,'120',0,'Dochód razem małżonka',name),
		(None,'121',0,'Zaliczka razem małżonka',name),

		(None,'122',0,'Składki na ubezpieczenia społeczne',name),
		(None,'123',0,'Składki na ubezpieczenia społeczne małżonka',name),
		(None,'124',0,'Odliczenia od dochodu- wykazane w części B załącznika PIT/O',name),
		(None,'125',0,'Odliczenia od dochodu- wykazane w części B załącznika PIT/O małżonka',name),
		(None,'126',0,'Ulga odsetkowa - wykazane w części B.1 załącznika PIT/D',name),
		(None,'127',0,'Dochód po odliczeniach',name),
		(None,'128',0,'Odliczenia mieszkaniowe - wykazane w części B.3 . załącznika PIT/D',name),
		(None,'129',0,'Podstawa obliczenia podatku',name),
		(None,'130',0,'Obliczony podatek według skali',name),
		(None,'132',0,'Doliczenia do podatku ',name),
		(None,'133',0,'Doliczenia do podatku - wykazane w części C załącznika PIT/O',name),
		(None,'134',0,'Doliczenia do podatku - wykazane w części C załącznika PIT/O małżonka',name),
		(None,'135',0,'Podatek po odliczeniach',name),
		(None,'136',0,'Odliczenia mieszkaniowe - wykazane w części C.2 . załącznika PIT/D',name),
		(None,'137',0,'Podatek należny',name),
		(None,'138',0,'Podatek do zapłaty',name),
		(None,'139',0,'Nadpłata podatku',name),
		(None,'140',0,'Składki na ubezpieczenia społeczne i zdrowotne',name),
		(None,'141',0,'Składki na ubezpieczenia społeczne i zdrowotne małżonka',name),
		(None,'142',0,'Różnica między kwotami PIT/O ulga na dzieci',name),
		(None,'143',0,'Różnica między kwotami PIT/O ulga na dzieci małżonka',name),
		(None,'144',0,'Dodatkowy zwrot',name),
		(None,'145',0,'Łączny zwrot',name),
		(None,'146',0,'Dochody art. 45 ust 3c',name),


		(None,'411',0,'Dar organizajom poż. publicznego',name),
		(None,'412',0,'Dar organizajom poż. publicznego małżonka',name),
        	(None,'413',0,'Darowizny przekazane na cele kultu religijnego',name),
		(None,'414',0,'Darowizny przekazane na cele kultu religijnego małżonka',name),
		(None,'415',0,'Darowizny przekazane na cele krwiodastwa',name),
		(None,'416',0,'Darowizny przekazane na cele krwiodastwa małżonka',name),
		(None,'417',0,'Darowizny przekazane na cele kształcenia zawodowego',name),
		(None,'418',0,'Darowizny przekazane na cele kształcenia zawodowego małżonka',name),
		(None,'419',0,'Darowizny przekazane na odbudowe',name),
		(None,'420',0,'Darowizny przekazane na odbudowe małżonka',name),
		(None,'421',0,'Darowizny wynikające z odrębnych ustaw',name),
		(None,'422',0,'Darowizny wynikające z odrębnych ustaw małżonka',name),
		(None,'423',0,'Ulga rehabilitacyjna',name),
		(None,'424',0,'Ulga rehabilitacyjna małżonka',name),
		(None,'425',0,'Zwrot nienależnie pobranych świadczeń',name),
		(None,'426',0,'Zwrot nienależnie pobranych świadczeń małżonka',name),
		(None,'427',0,'Ulga internetowa',name),
		(None,'428',0,'Ulga internetowa małżonka',name),
		(None,'429',0,'Ulga termomodernizacyjna',name),
		(None,'430',0,'Ulga termomodernizacyjna małżonka',name),
		(None,'431',0,'Wplłaty na IKZE',name),
		(None,'432',0,'Wplłaty na IKZE małżonka',name),
		(None,'433',0,'Składki członkowskie na rzecz związków zawodowych',name),
		(None,'434',0,'Składki członkowskie na rzecz związków zawodowych małżonka',name),
		(None,'435',0,'Ulga na zabytki',name),
		(None,'436',0,'Ulga na zabytki małżonka',name),
		(None,'437',0,'Wydatki na nabycie lub objęcie udziałów/akcji',name),
		(None,'438',0,'Wydatki na nabycie lub objęcie udziałów/akcji małżonka',name),
		(None,'440',0,'Inne ulgi podaj Wartość',name),
		(None,'441',0,'Inne ulgi podaj Wartość małżonka',name),

		(None,'442',0,'Rozem odliczenia od dochodu',name),
		(None,'443',0,'Razem odliczenia od dochodu małżonka',name),

		(None,'444',0,'Ulga uczniowska na podstawie decyzji',name),
		(None,'445',0,'Ulga uczniowska na podstawie decyzji małżonka',name),
		(None,'446',0,'składki ubezpieczenia społecznego opłacone z tytułu umowy aktywacyjnej z osobą bezrobotną',name),
		(None,'447',0,'składki ubezpieczenia społecznego opłacone z tytułu umowy aktywacyjnej z osobą bezrobotną małżonka',name),
		(None,'448',0,'Ulga na dzieci - Liczba dzieci',name),
		(None,'449',0,'Jeśli wpisałęś jedno dziecko ale ma ono orzeczenie niepełnosprawności wpisz 1',name),
		(None,'450',0,'Ulga na dzieci wartość',name),
		(None,'451',0,'Ulga na dzieci wartość małżonka',name),
		(None,'452',0,'Ulga abolicyjna',name),
		(None,'453',0,'Ulga abolicyjna małżonka',name),
		(None,'455',0,'Inne Ulgi wartość',name),
		(None,'456',0,'Inne Ulgi wartość małżonka',name),

		(None,'455',0,'Razem Odliczenia od podatku',name),
		(None,'456',0,'Razem Odliczenia od podatku małżonka',name),

		(None,'510',0,'Wydatki poniesione na spłatę kredytu do odliczenia',name),
		(None,'511',0,'Wydatki do odliczenia od przychodu w zeznaniu PIT-28',name),
		(None,'512',0,'Wydatki do odliczenia od przychodu w zeznaniu PIT-28 małżonka',name),
		(None,'513',0,'Ulgi mieszkaniowe do odliczenia w PIT-28,',name),
		(None,'514',0,'Ulgi mieszkaniowe do odliczenia w PIT-28, małżonka',name),
		(None,'515',0,'Ulgi mieszkaniowe do odliczenia w PIT-36 lub 37',name),
		(None,'516',0,'Ulgi mieszkaniowe do odliczenia w PIT-36 lub 37,małżonka',name),
		(None,'518',0,'Ulgi mieszkaniowe poniesione w roku podaj wartość',name),
		(None,'519',0,'Odliczenia które nie były  pokryte w latach ubiegłych',name),

		(None,'520',0,'Razem odliczenia w roku',name),
		(None,'521',0,'Odliczenia w PIT-28',name),
		(None,'522',0,'Odliczenia w pit 36|37',name),
		(None,'523',0,'Odliczenia od dochodu mieszkaniowe do odliczenia w PIT-28,',name),
		(None,'524',0,'Odliczenia od dochodu mieszkaniowe do odliczenia w PIT-28, małżonka',name),
		(None,'525',0,'Odliczenia od dochodu mieszkaniowe do odliczenia w PIT-36 lub 37',name),
		(None,'526',0,'Odliczenia od dochodu mieszkaniowe do odliczenia w PIT-36 lub 37,małżonka',name),
		
		

		(None,'527',0,'Odliczenia z tytułu kumulacji niewykożystanych ulg (30% nie więcje niż 11 340)',name),
		(None,'528',0,'Wyskość pozostałych do wykożystania odliczeń',name),
		(None,'532',0,'Odliczenia od podatku mieszkaniowe do odliczenia w PIT-28,',name),
		(None,'533',0,'Odliczenia od podatku mieszkaniowe do odliczenia w PIT-28, małżonka',name),
		(None,'534',0,'Odliczenia od podatku mieszkaniowe do odliczenia w PIT-36 lub 37',name),
		(None,'535',0,'Odliczenia od podatku mieszkaniowe do odliczenia w PIT-36 lub 37,małżonka',name),
		
		(None,'201',0,'Jeden stosunek pracy',name),
		(None,'202',0,'Więcej niż jeden stosunek pracy',name),
		(None,'203',0,'Jeden stosunke pracy poz miejscem',name),
		(None,'204',0,'Więcje niż jeden poza miejscem pracy',name),

		(None,'229',0,'Wpisz wartość pola 29 w PIT-11 druga strona',name),
		(None,'230',0,'Wpisz wartość pola 30 w PIT-11 druga strona',name),
		(None,'231',0,'Wpisz wartość pola 31 w PIT-11 druga strona',name),
		(None,'232',0,'Wpisz wartość pola 32 w PIT-11 druga strona',name),
		(None,'233',0,'Wpisz wartość pola 33 w PIT-11 druga strona',name),
		(None,'234',0,'Wpisz wartość pola 34 w PIT-11 druga strona',name),
		(None,'235',0,'Wpisz wartość pola 35 w PIT-11 druga strona',name),
		(None,'236',0,'Wpisz wartość pola 36 w PIT-11 druga strona',name),
		(None,'237',0,'Wpisz wartość pola 37 w PIT-11 druga strona',name),
		(None,'238',0,'Wpisz wartość pola 38 w PIT-11 druga strona',name),
		(None,'239',0,'Wpisz wartość pola 39 w PIT-11 druga strona',name),
		(None,'240',0,'Wpisz wartość pola 40 w PIT-11 druga strona',name),
		(None,'241',0,'Wpisz wartość pola 41 w PIT-11 druga strona',name),
		(None,'242',0,'Wpisz wartość pola 42 w PIT-11 druga strona',name),
		(None,'243',0,'Wpisz wartość pola 43 w PIT-11 druga strona',name),
		(None,'244',0,'Wpisz wartość pola 44 w PIT-11 druga strona',name),
		(None,'245',0,'Wpisz wartość pola 45 w PIT-11 druga strona',name),
		(None,'246',0,'Wpisz wartość pola 46 w PIT-11 druga strona',name),
		(None,'247',0,'Wpisz wartość pola 47 w PIT-11 druga strona',name),
		(None,'248',0,'Wpisz wartość pola 48 w PIT-11 druga strona',name),
		(None,'249',0,'Wpisz wartość pola 49 w PIT-11 druga strona',name),
		(None,'250',0,'Wpisz wartość pola 50 w PIT-11 druga strona',name),
		(None,'251',0,'Wpisz wartość pola 51 w PIT-11 druga strona',name),
		(None,'252',0,'Wpisz wartość pola 52 w PIT-11 druga strona',name),
		(None,'253',0,'Wpisz wartość pola 53 w PIT-11 druga strona',name),
		(None,'254',0,'Wpisz wartość pola 54 w PIT-11 druga strona',name),
		(None,'255',0,'Wpisz wartość pola 55 w PIT-11 druga strona',name),
		(None,'256',0,'Wpisz wartość pola 56 w PIT-11 druga strona',name),
		(None,'257',0,'Wpisz wartość pola 57 w PIT-11 druga strona',name),
		(None,'258',0,'Wpisz wartość pola 58 w PIT-11 druga strona',name),
		(None,'259',0,'Wpisz wartość pola 59 w PIT-11 druga strona',name),
		(None,'260',0,'Wpisz wartość pola 60 w PIT-11 druga strona',name),
		(None,'261',0,'Wpisz wartość pola 61 w PIT-11 druga strona',name),
		(None,'262',0,'Wpisz wartość pola 62 w PIT-11 druga strona',name),
		(None,'263',0,'Wpisz wartość pola 63 w PIT-11 druga strona',name),
		(None,'264',0,'Wpisz wartość pola 64 w PIT-11 druga strona',name),
		(None,'265',0,'Wpisz wartość pola 65 w PIT-11 druga strona',name),
		(None,'266',0,'Wpisz wartość pola 66 w PIT-11 druga strona',name),
		(None,'267',0,'Wpisz wartość pola 67 w PIT-11 druga strona',name),
		(None,'268',0,'Wpisz wartość pola 68 w PIT-11 druga strona',name),
		(None,'269',0,'Wpisz wartość pola 69 w PIT-11 druga strona',name),
		(None,'270',0,'Wpisz wartość pola 70 w PIT-11 druga strona',name),
		(None,'271',0,'Wpisz wartość pola 71 w PIT-11 druga strona',name),
		(None,'272',0,'Wpisz wartość pola 72 w PIT-11 druga strona',name),
		(None,'273',0,'Wpisz wartość pola 73 w PIT-11 druga strona',name),
		(None,'274',0,'Wpisz wartość pola 74 w PIT-11 druga strona',name),
		(None,'275',0,'Wpisz wartość pola 75 w PIT-11 druga strona',name),
		(None,'276',0,'Wpisz wartość pola 76 w PIT-11 druga strona',name),
		(None,'277',0,'Wpisz wartość pola 77 w PIT-11 druga strona',name),
		(None,'278',0,'Wpisz wartość pola 78 w PIT-11 druga strona',name),
		(None,'279',0,'Wpisz wartość pola 79 w PIT-11 druga strona',name),
		(None,'280',0,'Wpisz wartość pola 80 w PIT-11 druga strona',name),
		(None,'281',0,'Wpisz wartość pola 81 w PIT-11 druga strona',name),
		(None,'282',0,'Wpisz wartość pola 82 w PIT-11 druga strona',name),
		(None,'283',0,'Wpisz wartość pola 83 w PIT-11 druga strona',name),
		(None,'284',0,'Wpisz wartość pola 84 w PIT-11 druga strona',name),
		(None,'285',0,'Wpisz wartość pola 85 w PIT-11 druga strona',name),
		(None,'286',0,'Wpisz wartość pola 86 w PIT-11 druga strona',name),
		(None,'287',0,'Wpisz wartość pola 87 w PIT-11 druga strona',name),
		(None,'288',0,'Wpisz wartość pola 88 w PIT-11 druga strona',name),
		(None,'289',0,'Wpisz wartość pola 89 w PIT-11 druga strona',name),
		(None,'290',0,'Wpisz wartość pola 90 w PIT-11 druga strona',name),
		(None,'291',0,'Wpisz wartość pola 91 w PIT-11 druga strona',name),
		(None,'292',0,'Wpisz wartość pola 92 w PIT-11 druga strona',name),
		(None,'293',0,'Wpisz wartość pola 93 w PIT-11 druga strona',name),
		(None,'294',0,'Wpisz wartość pola 94 w PIT-11 druga strona',name),
		(None,'295',0,'Wpisz wartość pola 95 w PIT-11 druga strona',name),
		(None,'296',0,'Wpisz wartość pola 96 w PIT-11 druga strona',name),
		(None,'297',0,'Wpisz wartość pola 97 w PIT-11 druga strona',name),
		(None,'298',0,'Wpisz wartość pola 98 w PIT-11 trzecia strona',name),
		(None,'299',0,'Wpisz wartość pola 99 w PIT-11 trzecia strona',name),
		(None,'300',0,'Wpisz wartość pola 100 w PIT-11 trzecia strona',name),
		(None,'301',0,'Wpisz wartość pola 101 w PIT-11 trzecia strona',name),
		(None,'302',0,'Wpisz wartość pola 102 w PIT-11 trzecia strona',name),
		(None,'303',0,'Wpisz wartość pola 103 w PIT-11 trzecia strona',name),
		(None,'304',0,'Wpisz wartość pola 104 w PIT-11 trzecia strona',name),
		(None,'305',0,'Wpisz wartość pola 105 w PIT-11 trzecia strona',name),
		(None,'306',0,'Wpisz wartość pola 106 w PIT-11 trzecia strona',name),
		(None,'307',0,'Wpisz wartość pola 107 w PIT-11 trzecia strona',name),
		(None,'308',0,'Wpisz wartość pola 108 w PIT-11 trzecia strona',name),
		(None,'309',0,'Wpisz wartość pola 109 w PIT-11 trzecia strona',name),
		(None,'310',0,'Wpisz wartość pola 110 w PIT-11 trzecia strona',name),
		(None,'311',0,'Wpisz wartość pola 111 w PIT-11 trzecia strona',name),
		(None,'312',0,'Wpisz wartość pola 112 w PIT-11 trzecia strona',name),
		(None,'313',0,'Wpisz wartość pola 113 w PIT-11 trzecia strona',name),
		(None,'314',0,'Wpisz wartość pola 114 w PIT-11 trzecia strona',name),
		(None,'315',0,'Wpisz wartość pola 115 w PIT-11 trzecia strona',name),
		(None,'316',0,'Wpisz wartość pola 116 w PIT-11 trzecia strona',name),
		(None,'317',0,'Wpisz wartość pola 117 w PIT-11 trzecia strona',name),
		(None,'318',0,'Wpisz 1 jeśli kwadrat jest zaznaczony  118 w PIT-11 trzecia strona',name),
		(None,'319',0,'Wpisz wartość pola 119 w PIT-11 trzecia strona',name),
		(None,'320',0,'Wpisz wartość pola 120 w PIT-11 trzecia strona',name),
		(None,'321',0,'Wpisz wartość pola 121 w PIT-11 trzecia strona',name),
		(None,'322',0,'Wpisz wartość pola 122 w PIT-11 trzecia strona',name),
		(None,'323',0,'Wpisz wartość pola 123 w PIT-11 trzecia strona',name),
		
		
		)


   	 # wstawiamy wiele rekordów
	cur.executemany('INSERT INTO data VALUES(?,?,?,?,?)', record)

   	 # zatwierdzamy zmiany w bazie
	con.commit()
	global list_available
	list_available = [0,1,2,3,5,7,9,11,13,15,20,21,25]


    # pobieranie danych z bazy
def readall(user):
	cur.execute("""
		SELECT * FROM data WHERE user=?""",(user))
	record = cur.fetchall()
	return record
	

def update(name,val,user):
	cur.execute("""
		UPDATE data SET value=? WHERE name=? AND user=?""", (val, name,user))
	con.commit()

def readDBU(name,user):
	cur.execute("SELECT * FROM data WHERE data.name=? AND data.user=?",[name,user])
	record = cur.fetchall()
	return record[0]['value']

def current(user):
	cur.execute("SELECT * FROM data WHERE data.name=? AND data.user=?",['current',user])
	record=cur.fetchall()
	return record[0]['value']

def next(curr):
	if curr == 999:
		return 999
	elif curr < 25:
		a = list_available.index(curr)
		return list_available[a+1]
	else:
		if len(list_available) < 14:
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



def create_list(user):
	global list_available
	gender = readDBU('1',user)
	age = readDBU('3',user)
	mage = readDBU('4',user)
	if readDBU('20',user):
		list_available += [510,511,513,518,519,523,527,528,532]
	if readDBU('21',user):
		list_available += [411,413,415,417,419,421,423,425,427,429,431,433,435,437,440,444,446,448,449,450,452,455]
	if readDBU('25',user):
		list_available += [201,202,203,204]
		num=229
		while num < 324:
			list_available.append(num)
			num += 1
	if not readDBU('1',user):
		list_available.append(26)

	if age < 27 or (mage < 27 and mage != 0):
		list_available.append(34)
	if readDBU('15',user) and not readDBU('2',user):  # jeśli wrodzinie są dzieci i osoba rozlicza się samotnie
		list_available.append(35)
	list_available.append(36)
	if gender:
		if age > 64 or mage > 59:
			list_available.append(40)
	else:
		if age > 59 or mage > 64:
			list_available.append(40)
	if readDBU('5',user) > 0 or readDBU('6',user) > 0:  # praca na etacie
		list_available += [52,53,56,57,58]
	if readDBU('13',user) > 0 or readDBU('14',user) > 0: # świadczenia państwowe
		list_available += [59,61]
	if readDBU('7',user) > 0 or readDBU('8',user) > 0: # praca wykonana osobiście
		list_available += [62,63,66,67,68]
	if readDBU('9',user) > 0 or readDBU('10',user) > 0: # Prawa autorskie
		list_available += [69,70,73,74,75]
	if readDBU('11',user) > 0 or readDBU('12',user) > 0: # inne źródła
		list_available += [76,77,80,81,82]
	list_available += [122,132,133,146]
	if readDBU('15',user):
		list_available += [140]
	list_available.append(999)


def benefit(user):
	gender = readDBU('2',user)
	age = readDBU('3',user)
	mage = readDBU('4',user)
	if age < 27 or (mage < 27 and mage != 0):
		if readDBU('34',user):
			update('34',0,user)
		elif age < 27:
			update('34',1,user)
		if readDBU('35'):
			update('35',0,user)
		elif (mage < 27 and mage != 0):
			update('35',1,user)
	if gender:
		if age > 64:
			if readDBU('40',user):
				update('40',0,user)
			else:
				update('40',1,user)
		if mage > 59 :
			if readDBU('41',user):
				update('41',0,user)
			else:
				update('41',1,user)
			
	else:
		if age > 59:
			if readDBU('40',user):
				update('40',0,user)
			else:
				update('40',1,user)
		if mage > 64:
			if readDBU('41',user):
				update('41',0,user)
			else:
				update('41',1,user)
def check():
	table = cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='data'""").fetchall()
	
	if table == []:
		return True
	else:
		return False

def checkU(name):
	table = cur.execute("""SELECT name FROM users WHERE name=?""",[name]).fetchall()
	
	if table == []:
		return True
	else:
		return False