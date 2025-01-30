import sqlite3
#user Admin password 'baza1podatek'

import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('DBQuestions.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()
def restart():
    # tworzenie tabel
    #cur.execute("DROP TABLE IF EXISTS questions;")

    cur.executescript("""
        DROP TABLE IF EXISTS questions;
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY ASC,
            number int(50) NOT NULL,
            question varchar(250) NOT NULL,
            type varchar(5) DEFAULT 'N'''
        )""")

    # B- binarna odpowiedź
    # D-
    ## tupla "record" zawiera tuple z danymi poszczególintnych zapytań
    ### na tuplę składa się klucz , numer pytania (najczęściej numer pola w deklaracji, pytania, typ zapytania)
    #### typ B oznacza wybór odpowiedzi z tak nie, typ N oznacza pola do uzupełnienia wartościami numerycznymi, typ W oznacz uzupełnienie 1 wartości nie zależnie czy rozliczenie z małżonkiem czy nie
    record = (
        (None,999,'Proszę wcisnoć przycisk Wprowadzone wartości','N'),

        (None,1,'Proszę zaznaczyć tak jeśli podatnik jest mężczyzną','B'),
        (None,2,'Czy rozliczenie wspólnie z Żoną/Mężem? ','B'),
        (None,3,'Podaj wiek','N'),
        (None,5,'Czy pracujesz na Etacie?','B'),
        (None,7,'Czy wykonujesz działalność wykonywaną osobiście?','B'),
        (None,9,'Czy uzyskujesz przychody z Praw Autorskich i innych praw?','B'),
        (None,11,'Czy posiadasz inne źródła przychodów w tym praktyki absolwenckie, staże uczniowskie i zasiłki macieżyńskie?','B'),
        (None,13,'Czy otrzymujesz świadczenia od państwa (emerytury,renty,zasiłki)?','B'),
        (None,15,'Czy są w rodzinie nieletnie(na wychowaniu) dzieci?','B'),
        (None,16,'Czy jesteś wdową/wdowcem?','B'),

        (None,34,'Czy zrezygnowałeś z ulgi dla młodych?','B'),
        (None,36,'Czy opłacane były podatki w innym kraju po 2021 roku?', 'B'),
        (None,38,'Czy w rodzinie są co najmniej 4 nieletnie(na wychowaniu) dzieci?','B'),
        (None,40,'Czy otrzymywana jest emerytura?','B'),
        (None,52,'Przychody z pracy na Etacie opodatkowanie zgodnie z kosztami','N'),
        (None,53,'Koszty z pracy na Etacie opodatkowanie zgodnie z kosztami','N'),
        (None,56,'Zaliczka pobrana przez płatnika z pracy na Etacie','N'),
        (None,57,'Przychody z pracy na Etacie do których stosowana jest stawka 50% maksymalnie 120000','N'),
        (None,58,'Kosszty pracy na Etacie do których stosowana jest stawka 50% maksymalnie 120000','N'),
        (None,59,'Przychody z Emerytury/renty/ inne krajowe świadczenia','N'),
        (None,61,'Zaliczka pobrana przez płatnika z Emerytury/renty/ inne krajowe świadczenia','N'),
        (None,62,'Przychody z działalności wykonywanej osobiście(art. 13 pkt 8 ustawy o podatku od osób fizycznych)','N'),
        (None,63,'Koszty z działalności wykonywanej osobiście','N'),
        (None,66,'Zaliczka pobrana przez płatnika z działalności wykonywanej osobiście','N'),
        (None,67,'Przychody z działalności wykonywanej osobiście (art. 13 pkt 8 - umowy zlecenia lub o dzieło)','N'),
        (None,68,'Koszty z działalności wykonywanej osobiście(art. 13)','N'),
        (None,69,'Przychody z Praw Autorskich i innych praw(art. 18)','N'),
        (None,70,'Koszty z Praw Autorskich i innych praw(art. 18)','N'),
        (None,73,'Zaliczka pobrana przez płatnika z Praw Autorskich i innych praw(art. 18)','N'),
        (None,74,'Przychody z Praw Autorskich i innych praw(art. 18)do których stosowana jest stawka 50% maksymalnie 120000','N'),
        (None,75,'Koszty z Praw Autorskich i innych praw(art. 18)do których stosowana jest stawka 50% maksymalnie 120000','N'),
        (None,76,'Przychody z innych źródeł bez praktyk, staży lub zasiłku macieżyńskiego','N'),
        (None,77,'koszty z innych źródeł','N'),
        (None,81,'Przychody z praktyk absolwenckich oraz staży uczniowskich','N'),
        (None,82,'Przychody z zasiłku macierzyńskiego','N'),
        (None,77,'koszty innych źródeł','N'),
        (None,80,'Zaliczki pobrane przez płatnika inne źródeła','N'),
        (None,122,'Składki na ubezpieczenia społeczne','N'),
        (None,124,'Odliczenia - część B załącznika PIT/O','N'),
        (None,126,'Odliczenia - część B.1 załącznika PIT/O','W'),
        (None,128,'Odliczenia - część B.3 załącznika PIT/O','W'),
        (None,132,'Doliczenia do podatku - kwota ','W'),
        (None,133,'Odliczenia - część C załącznika PIT/O','N'),
        (None,136,'Odliczenia - część C.2 załącznika PIT/D','W'),
        (None,140,'Składki na ubezpieczenia zdrowotne ','N'),
        (None,142,'Różnica między kwotą przysługującego odliczenia a odliczoną z PIT/O (poz.1 część E - część C ulga na dzieci)','N'),
        (None,146,'Dochody z budynków i działalności rolnej','N'),
        
        

     )

    # wstawiamy wiele rekordów
    cur.executemany('INSERT INTO questions VALUES(?,?,?,?)', record)

    # zatwierdzamy zmiany w bazie
    con.commit()
    # pobieranie danych z bazy
def read():
    """Funkcja pobiera i wyświetla dane z bazy."""

    cur.execute("""
        SELECT * FROM questions""")
    record = cur.fetchall()
    


restart()


