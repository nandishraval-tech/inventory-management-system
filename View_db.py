import sqlite3

connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()