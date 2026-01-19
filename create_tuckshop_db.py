import sqlite3

conn = sqlite3.connect("tuckshop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE tuckshop (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               sweet TEXT,
               price INTEGER
)
""")

conn.commit()
conn.close()

print("Tuckshop database created")