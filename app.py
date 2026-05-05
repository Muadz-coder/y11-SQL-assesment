import sqlite3

DATABASE = 'book.db'


db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM book;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
db.close()