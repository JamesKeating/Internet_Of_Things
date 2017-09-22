
import sqlite3

db = sqlite3.connect("chinook.db")

c = db.cursor()
c.execute('select * from customers')

row1 = c.fetchone()

print(row1)
print(row1[3])

db.close()