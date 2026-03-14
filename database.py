import sqlite3

connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
category TEXT,
stock INTEGER,
warehouse TEXT
)
""")

cursor.execute("INSERT INTO products (name, category, stock, warehouse) VALUES ('Chair','Furniture',3,'A')")
cursor.execute("INSERT INTO products (name, category, stock, warehouse) VALUES ('Table','Furniture',10,'A')")
cursor.execute("INSERT INTO products (name, category, stock, warehouse) VALUES ('Steel Rod','Raw Material',120,'B')")

connection.commit()

connection.close()

print("Database created successfully")