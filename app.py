import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

book_title = input("What book are you looking for?\nUser: ").title()
sql = "SELECT * FROM book WHERE book_name = ?;"
cursor.execute(sql, (book_name,))
result = cursor.fetchall()

if result:
    print(result)
else:
    print("Not found")

db.close()
