import sqlite3
#user Admin password 'baza1podatek'

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('DBQuestions.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

def read(number):
    """Funkcja pobiera i wyświetla dane z bazy."""
    
    cur.execute("""
        SELECT * FROM q2024 WHERE number=? """,[number])
    record = cur.fetchall()
    return record[0]

