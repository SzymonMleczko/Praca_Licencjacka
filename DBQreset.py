import sqlite3
#user admin password 'baza1podatek'

import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
con = sqlite3.connect('DBQuestions.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()
def restart():
    # tworzenie tabel
   

    cur.executescript("""
        DROP TABLE IF EXISTS questions;
        DROP TABLE IF EXISTS q2024;
        CREATE TABLE IF NOT EXISTS q2024 (
            id INTEGER PRIMARY KEY ASC,
            number int(50) NOT NULL,
            question varchar(250) NOT NULL,
            type varchar(5) DEFAULT 'N',
            pit varchar(10) NOT NULL''
        )""")

    # B- binarna odpowiedź
    # D-
    ## tupla "record" zawiera tuple z danymi poszczególintnych zapytań
    ### na tuplę składa się klucz , numer pytania (najczęściej numer pola w deklaracji, pytania, typ zapytania)
    #### typ B oznacza wybór odpowiedzi z tak nie, typ N oznacza pola do uzupełnienia wartościami numerycznymi, typ W oznacz uzupełnienie 1 wartości nie zależnie czy rozliczenie z małżonkiem czy nie
    record = (
        (None,999,'Proszę wcisnoć przycisk Wprowadzone wartości','N','PIT-37'),
        (None,0, 'Rozpoczynij, naciśnij Gotowy','B','PIT-37'),
        (None,1,'Proszę zaznaczyć tak jeśli podatnik jest mężczyzną','B','PIT-37'),
        (None,2,'Czy rozliczenie wspólnie z Żoną/Mężem? ','B','PIT-37'),
        (None,3,'Podaj wiek','N','PIT-37'),
        (None,5,'Czy pracujesz na Etacie?','B','PIT-37'),
        (None,7,'Czy wykonujesz działalność wykonywaną osobiście?','B','PIT-37'),
        (None,9,'Czy uzyskujesz przychody z Praw Autorskich i innych praw?','B','PIT-37'),
        (None,11,'Czy posiadasz inne źródła przychodów w tym praktyki absolwenckie, staże uczniowskie i zasiłki macieżyńskie?','B','PIT-37'),
        (None,13,'Czy otrzymujesz świadczenia od państwa (emerytury,renty,zasiłki)?','B','PIT-37'),
        (None,15,'Czy są w rodzinie nieletnie(na wychowaniu) dzieci?','B','PIT-37'),
        

        (None,20,'Czy zaciągnołeś ktedyt na mieszkanie,remont w latach 2002-2006 wpisz 1 jeśli tak','W','PIT-11'),
        (None,21,'Czy przekazałeś darowiznę, kożystasz z ulgi rehabilitacyjnej, internetowej, na zabytki na dzieci, abolicyjnej, wpłaciłeś na IKZE, składki członkowskie w związku zawodowym, wpisz 1 jeśli tak','W','PIT-11'),
        (None,25,'Czy otrzymałeś formularz PIT-11?','B','PIT-11'),
        (None,26,'Czy jesteś wdową/wdowcem?','B','PIT-37'),


        (None,34,'Czy zrezygnowałeś z ulgi dla młodych?','B','PIT-37'),
        (None,36,'Czy opłacane były podatki w innym kraju po 2021 roku?', 'B','PIT-37'),
        (None,38,'Czy w rodzinie są co najmniej 4 nieletnie(na wychowaniu) dzieci?','B','PIT-37'),
        (None,40,'Czy otrzymywana jest emerytura?','B','PIT-37'),
        (None,52,'Przychody z pracy na Etacie opodatkowanie zgodnie z kosztami','N','PIT-37'),
        (None,53,'Koszty z pracy na Etacie opodatkowanie zgodnie z kosztami','N','PIT-37'),
        (None,56,'Zaliczka pobrana przez płatnika z pracy na Etacie','N','PIT-37'),
        (None,57,'Przychody z pracy na Etacie do których stosowana jest stawka 50% maksymalnie 120000','N','PIT-37'),
        (None,58,'Kosszty pracy na Etacie do których stosowana jest stawka 50% maksymalnie 120000','N','PIT-37'),
        (None,59,'Przychody z Emerytury/renty/ inne krajowe świadczenia','N','PIT-37'),
        (None,61,'Zaliczka pobrana przez płatnika z Emerytury/renty/ inne krajowe świadczenia','N','PIT-37'),
        (None,62,'Przychody z działalności wykonywanej osobiście(art. 13 pkt 8 ustawy o podatku od osób fizycznych)','N','PIT-37'),
        (None,63,'Koszty z działalności wykonywanej osobiście','N','PIT-37'),
        (None,66,'Zaliczka pobrana przez płatnika z działalności wykonywanej osobiście','N','PIT-37'),
        (None,67,'Przychody z działalności wykonywanej osobiście (art. 13 pkt 8 - umowy zlecenia lub o dzieło)','N','PIT-37'),
        (None,68,'Koszty z działalności wykonywanej osobiście(art. 13)','N','PIT-37'),
        (None,69,'Przychody z Praw Autorskich i innych praw(art. 18)','N','PIT-37'),
        (None,70,'Koszty z Praw Autorskich i innych praw(art. 18)','N','PIT-37'),
        (None,73,'Zaliczka pobrana przez płatnika z Praw Autorskich i innych praw(art. 18)','N','PIT-37'),
        (None,74,'Przychody z Praw Autorskich i innych praw(art. 18)do których stosowana jest stawka 50% maksymalnie 120000','N','PIT-37'),
        (None,75,'Koszty z Praw Autorskich i innych praw(art. 18)do których stosowana jest stawka 50% maksymalnie 120000','N','PIT-37'),
        (None,76,'Przychody z innych źródeł bez praktyk, staży lub zasiłku macieżyńskiego','N','PIT-37'),
        (None,77,'koszty z innych źródeł','N','PIT-37'),
        (None,81,'Przychody z praktyk absolwenckich oraz staży uczniowskich','N','PIT-37'),
        (None,82,'Przychody z zasiłku macierzyńskiego','N','PIT-37'),
        (None,77,'koszty innych źródeł','N','PIT-37'),
        (None,80,'Zaliczki pobrane przez płatnika inne źródeła','N','PIT-37'),
        (None,122,'Składki na ubezpieczenia społeczne','N','PIT-37'),
        (None,124,'Odliczenia - część B załącznika PIT/O','N','PIT-37'),
        (None,132,'Doliczenia do podatku - kwota ','W','PIT-37'),
        (None,133,'Odliczenia - część C załącznika PIT/O','N','PIT-37'),
        (None,136,'Odliczenia - część C.2 załącznika PIT/D','W','PIT-37'),
        (None,140,'Składki na ubezpieczenia zdrowotne ','N','PIT-37'),
        (None,142,'Różnica między kwotą przysługującego odliczenia a odliczoną z PIT/O (poz.1 część E - część C ulga na dzieci)','N','PIT-37'),
        (None,146,'Dochody z budynków i działalności rolnej','N','PIT-37'),
    

        
        (None,201,'Jeśli pole 28.1 jest zaznaczone wpisz 1 w PIT-11 pierwsza strona','W','PIT-11'),
        (None,202,'Jeśli pole 28.2 jest zaznaczone wpisz 1 w PIT-11 pierwsza strona','W','PIT-11'),
        (None,203,'Jeśli pole 28.3 jest zaznaczone wpisz 1 w PIT-11 pierwsza strona','W','PIT-11'),
        (None,204,'Jeśli pole 28.4 jest zaznaczone wpisz 1 w PIT-11 pierwsza strona','W','PIT-11'),

        (None,229,'Wpisz wartość pola 29 w PIT-11 druga strona','W','PIT-11'),
        (None,230,'Wpisz wartość pola 30 w PIT-11 druga strona','W','PIT-11'),
        (None,231,'Wpisz wartość pola 31 w PIT-11 druga strona','W','PIT-11'),
        (None,232,'Wpisz wartość pola 32 w PIT-11 druga strona','W','PIT-11'),
        (None,233,'Wpisz wartość pola 33 w PIT-11 druga strona','W','PIT-11'),
        (None,234,'Wpisz wartość pola 34 w PIT-11 druga strona','W','PIT-11'),
        (None,235,'Wpisz wartość pola 35 w PIT-11 druga strona','W','PIT-11'),
        (None,236,'Wpisz wartość pola 36 w PIT-11 druga strona','W','PIT-11'),
        (None,237,'Wpisz wartość pola 37 w PIT-11 druga strona','W','PIT-11'),
        (None,238,'Wpisz wartość pola 38 w PIT-11 druga strona','W','PIT-11'),
        (None,239,'Wpisz wartość pola 39 w PIT-11 druga strona','W','PIT-11'),
        (None,240,'Wpisz wartość pola 40 w PIT-11 druga strona','W','PIT-11'),
        (None,241,'Wpisz wartość pola 41 w PIT-11 druga strona','W','PIT-11'),
        (None,242,'Wpisz wartość pola 42 w PIT-11 druga strona','W','PIT-11'),
        (None,243,'Wpisz wartość pola 43 w PIT-11 druga strona','W','PIT-11'),
        (None,244,'Wpisz wartość pola 44 w PIT-11 druga strona','W','PIT-11'),
        (None,245,'Wpisz wartość pola 45 w PIT-11 druga strona','W','PIT-11'),
        (None,246,'Wpisz wartość pola 46 w PIT-11 druga strona','W','PIT-11'),
        (None,247,'Wpisz wartość pola 47 w PIT-11 druga strona','W','PIT-11'),
        (None,248,'Wpisz wartość pola 48 w PIT-11 druga strona','W','PIT-11'),
        (None,249,'Wpisz wartość pola 49 w PIT-11 druga strona','W','PIT-11'),
        (None,250,'Wpisz wartość pola 50 w PIT-11 druga strona','W','PIT-11'),
        (None,251,'Wpisz wartość pola 51 w PIT-11 druga strona','W','PIT-11'),
        (None,252,'Wpisz wartość pola 52 w PIT-11 druga strona','W','PIT-11'),
        (None,253,'Wpisz wartość pola 53 w PIT-11 druga strona','W','PIT-11'),
        (None,254,'Wpisz wartość pola 54 w PIT-11 druga strona','W','PIT-11'),
        (None,255,'Wpisz wartość pola 55 w PIT-11 druga strona','W','PIT-11'),
        (None,256,'Wpisz wartość pola 56 w PIT-11 druga strona','W','PIT-11'),
        (None,257,'Wpisz wartość pola 57 w PIT-11 druga strona','W','PIT-11'),
        (None,258,'Wpisz wartość pola 58 w PIT-11 druga strona','W','PIT-11'),
        (None,259,'Wpisz wartość pola 59 w PIT-11 druga strona','W','PIT-11'),
        (None,260,'Wpisz wartość pola 60 w PIT-11 druga strona','W','PIT-11'),
        (None,261,'Wpisz wartość pola 61 w PIT-11 druga strona','W','PIT-11'),
        (None,262,'Wpisz wartość pola 62 w PIT-11 druga strona','W','PIT-11'),
        (None,263,'Wpisz wartość pola 63 w PIT-11 druga strona','W','PIT-11'),
        (None,264,'Wpisz wartość pola 64 w PIT-11 druga strona','W','PIT-11'),
        (None,265,'Wpisz wartość pola 65 w PIT-11 druga strona','W','PIT-11'),
        (None,266,'Wpisz wartość pola 66 w PIT-11 druga strona','W','PIT-11'),
        (None,267,'Wpisz wartość pola 67 w PIT-11 druga strona','W','PIT-11'),
        (None,268,'Wpisz wartość pola 68 w PIT-11 druga strona','W','PIT-11'),
        (None,269,'Wpisz wartość pola 69 w PIT-11 druga strona','W','PIT-11'),
        (None,270,'Wpisz wartość pola 70 w PIT-11 druga strona','W','PIT-11'),
        (None,271,'Wpisz wartość pola 71 w PIT-11 druga strona','W','PIT-11'),
        (None,272,'Wpisz wartość pola 72 w PIT-11 druga strona','W','PIT-11'),
        (None,273,'Wpisz wartość pola 73 w PIT-11 druga strona','W','PIT-11'),
        (None,274,'Wpisz wartość pola 74 w PIT-11 druga strona','W','PIT-11'),
        (None,275,'Wpisz wartość pola 75 w PIT-11 druga strona','W','PIT-11'),
        (None,276,'Wpisz wartość pola 76 w PIT-11 druga strona','W','PIT-11'),
        (None,277,'Wpisz wartość pola 77 w PIT-11 druga strona','W','PIT-11'),
        (None,278,'Wpisz wartość pola 78 w PIT-11 druga strona','W','PIT-11'),
        (None,279,'Wpisz wartość pola 79 w PIT-11 druga strona','W','PIT-11'),
        (None,280,'Wpisz wartość pola 80 w PIT-11 druga strona','W','PIT-11'),
        (None,281,'Wpisz wartość pola 81 w PIT-11 druga strona','W','PIT-11'),
        (None,282,'Wpisz wartość pola 82 w PIT-11 druga strona','W','PIT-11'),
        (None,283,'Wpisz wartość pola 83 w PIT-11 druga strona','W','PIT-11'),
        (None,284,'Wpisz wartość pola 84 w PIT-11 druga strona','W','PIT-11'),
        (None,285,'Wpisz wartość pola 85 w PIT-11 druga strona','W','PIT-11'),
        (None,286,'Wpisz wartość pola 86 w PIT-11 druga strona','W','PIT-11'),
        (None,287,'Wpisz wartość pola 87 w PIT-11 druga strona','W','PIT-11'),
        (None,288,'Wpisz wartość pola 88 w PIT-11 druga strona','W','PIT-11'),
        (None,289,'Wpisz wartość pola 89 w PIT-11 druga strona','W','PIT-11'),
        (None,290,'Wpisz wartość pola 90 w PIT-11 druga strona','W','PIT-11'),
        (None,291,'Wpisz wartość pola 91 w PIT-11 druga strona','W','PIT-11'),
        (None,292,'Wpisz wartość pola 92 w PIT-11 druga strona','W','PIT-11'),
        (None,293,'Wpisz wartość pola 93 w PIT-11 druga strona','W','PIT-11'),
        (None,294,'Wpisz wartość pola 94 w PIT-11 druga strona','W','PIT-11'),
        (None,295,'Wpisz wartość pola 95 w PIT-11 druga strona','W','PIT-11'),
        (None,296,'Wpisz wartość pola 96 w PIT-11 druga strona','W','PIT-11'),
        (None,297,'Wpisz wartość pola 97 w PIT-11 druga strona','W','PIT-11'),
        (None,298,'Wpisz wartość pola 98 w PIT-11 trzecia strona','W','PIT-11'),
        (None,299,'Wpisz wartość pola 99 w PIT-11 trzecia strona','W','PIT-11'),
        (None,300,'Wpisz wartość pola 100 w PIT-11 trzecia strona','W','PIT-11'),
        (None,301,'Wpisz wartość pola 101 w PIT-11 trzecia strona','W','PIT-11'),
        (None,302,'Wpisz wartość pola 102 w PIT-11 trzecia strona','W','PIT-11'),
        (None,303,'Wpisz wartość pola 103 w PIT-11 trzecia strona','W','PIT-11'),
        (None,304,'Wpisz wartość pola 104 w PIT-11 trzecia strona','W','PIT-11'),
        (None,305,'Wpisz wartość pola 105 w PIT-11 trzecia strona','W','PIT-11'),
        (None,306,'Wpisz wartość pola 106 w PIT-11 trzecia strona','W','PIT-11'),
        (None,307,'Wpisz wartość pola 107 w PIT-11 trzecia strona','W','PIT-11'),
        (None,308,'Wpisz wartość pola 108 w PIT-11 trzecia strona','W','PIT-11'),
        (None,309,'Wpisz wartość pola 109 w PIT-11 trzecia strona','W','PIT-11'),
        (None,310,'Wpisz wartość pola 110 w PIT-11 trzecia strona','W','PIT-11'),
        (None,311,'Wpisz wartość pola 111 w PIT-11 trzecia strona','W','PIT-11'),
        (None,312,'Wpisz wartość pola 112 w PIT-11 trzecia strona','W','PIT-11'),
        (None,313,'Wpisz wartość pola 113 w PIT-11 trzecia strona','W','PIT-11'),
        (None,314,'Wpisz wartość pola 114 w PIT-11 trzecia strona','W','PIT-11'),
        (None,315,'Wpisz wartość pola 115 w PIT-11 trzecia strona','W','PIT-11'),
        (None,316,'Wpisz wartość pola 116 w PIT-11 trzecia strona','W','PIT-11'),
        (None,317,'Wpisz wartość pola 117 w PIT-11 trzecia strona','W','PIT-11'),
        (None,318,'Wpisz 1 jeśli kwadrat jest zaznaczony  118 w PIT-11 trzecia strona','W','PIT-11'),
        (None,319,'Wpisz wartość pola 119 w PIT-11 trzecia strona','W','PIT-11'),
        (None,320,'Wpisz wartość pola 120 w PIT-11 trzecia strona','W','PIT-11'),
        (None,321,'Wpisz wartość pola 121 w PIT-11 trzecia strona','W','PIT-11'),
        (None,322,'Wpisz wartość pola 122 w PIT-11 trzecia strona','W','PIT-11'),
        (None,323,'Wpisz wartość pola 123 w PIT-11 trzecia strona','W','PIT-11'),



        (None,411,'Darowizny przekazane organizajom pożytku publicznego','N','PIT/O'),
        (None,413,'Darowizny przekazane na cele kultu religijnego','N','PIT/O'),
        (None,415,'Darowizny przekazane na cele krwiodastwa','N','PIT/O'),
        (None,417,'Darowizny przekazane na cele kształcenia zawodowego','N','PIT/O'),
        (None,419,'Darowizny przekazane na odbudowe Pałacu Saskiego, Bruhia oraz kamienic przy ulicy królewskiej','N','PIT/O'),
        (None,421,'Darowizny wynikające z odrębnych ustaw','N','PIT/O'),
        (None,423,'Ulga rehabilitacyjna','N','PIT/O'),
        (None,425,'Zwrot nienależnie pobranych świadczeń','N','PIT/O'),
        (None,427,'Ulga internetowa','N','PIT/O'),
        (None,429,'Ulga termomodernizacyjna','N','PIT/O'),
        (None,431,'Wplłaty na IKZE','N','PIT/O'),
        (None,433,'Składki członkowskie na rzecz związków zawodowych','N','PIT/O'),
        (None,435,'Ulga na zabytki','N','PIT/O'),
        (None,437,'Wydatki na nabycie lub objęcie udziałów/akcji','N','PIT/O'),
        (None,440,'Inne ulgi podaj Wartość','N','PIT/O'),
        (None,444,'Ulga uczniowska na podstawie decyzji','N','PIT/O'),
        (None,446,'składki ubezpieczenia społecznego opłacone z tytułu umowy aktywacyjnej z osobą bezrobotną','N','PIT/O'),
        (None,448,'Ulga na dzieci - Liczba dzieci','W','PIT/O'),
        (None,449,'Jeśli wpisałęś jedno dziecko ale ma ono orzeczenie niepełnosprawności wpisz 1','W','PIT/O'),
        (None,450,'Ulga na dzieci wartość','N','PIT/O'),
        (None,452,'Ulga abolicyjna','N','PIT/O'),
        (None,455,'Inne Ulgi wartość','N','PIT/O'),


        (None,510,'Wydatki poniesione na spłatę kredytu do odliczenia','W','PIT/D'),
        (None,511,'Wydatki do odliczenia od przychodu w zeznaniu PIT-28','W','PIT/D'),
        (None,513,'Ulga odsetkowa - Wydatki mieszkaniowe do odliczenia w PIT-28, Uzupełnij jeśli rozliczenie z kilku źródeł przychodu, ryczałtowo lub małżonkowie rozliczją się osobno','N','PIT/D'),
        (None,518,'Wydatki mieszkaniowe poniesione w roku podaj wartość','W','PIT/D'),
        (None,519,'Odliczenia które nie były  pokryte w latach ubiegłych','W','PIT/D'),
        (None,523,'Odliczenia dochodu- Wydatki mieszkaniowe do odliczenia w PIT-28, Uzupełnij jeśli rozliczenie z kilku źródeł przychodu, ryczałtowo lub małżonkowie rozliczją się osobno','N','PIT/D'),
       
        (None,527,'Odliczenia z tytułu kumulacji niewykożystanych ulg (30% nie więcje niż 11 340)','W','PIT/D'),
        (None,528,'Wyskość pozostałych do wykożystania odliczeń','W','PIT/D'),
        (None,532,'Odliczenia podatku- Wydatki mieszkaniowe do odliczenia w PIT-28, Uzupełnij jeśli rozliczenie z kilku źródeł przychodu, ryczałtowo lub małżonkowie rozliczją się osobno','N','PIT/D'),
       
        

        
    
     )

    # wstawiamy wiele rekordów
    cur.executemany('INSERT INTO q2024 VALUES(?,?,?,?,?)', record)

    # zatwierdzamy zmiany w bazie
    con.commit()
    # pobieranie danych z bazy
def read():
    """Funkcja pobiera i wyświetla dane z bazy."""

    cur.execute("""
        SELECT * FROM questions""")
    record = cur.fetchall()
    


restart()


