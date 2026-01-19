import sqlite3

conn = sqlite3.connect("tuckshop.db")
cursor = conn.cursor()

sweet = input("Enter sweet name: ")
price = int(input("Enter price in pence: "))

cursor.execute(
    "INSERT INTO tuckshop (sweet, price) VALUES (?, ?)",
    (sweet, price)
)

conn.commit()
conn.close()

print("Sweet added")