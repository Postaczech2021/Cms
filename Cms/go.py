import sqlite3

# Připojení k databázi
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Získání informací o sloupcích tabulky food_food
cursor.execute("PRAGMA table_info(food_food);")
columns = cursor.fetchall()

# Výpis sloupců
for column in columns:
    print(f"Column: {column[1]}, Type: {column[2]}")

# Uzavření připojení
conn.close()
