import sqlite3

# Připojte se k databázi
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Získejte seznam všech tabulek
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

if not tables:
    print("Žádné tabulky nebyly nalezeny.")
else:
    # Pro každou tabulku získejte seznam sloupců
    for table in tables:
        table_name = table[0]
        print(f"Tabulka: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        if not columns:
            print(f"  Tabulka {table_name} nemá žádné sloupce.")
        else:
            for column in columns:
                print(f"  Sloupec: {column[1]}, Typ: {column[2]}")
        print()

# Zavřete připojení k databázi
conn.close()
