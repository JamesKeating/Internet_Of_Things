import MySQLdb

db = MySQLdb.connect("localhost", "root", "1234", "world")

c = db.cursor()
c.execute("select * from country")

row1 = c.fetchone()

print(row1[3])

db.close()
