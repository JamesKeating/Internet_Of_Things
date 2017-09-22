import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="james",         # your username
                     passwd="1234",  # your password
                     db="us_states")

c = db.cursor()
c.execute("select * from states")

row1 = c.fetchone()

print(row1[2])

db.close()
