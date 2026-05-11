import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

book_title = input("What book are you looking for?\nUser: ").title()
sql = "SELECT * FROM book WHERE book_name = ?;"
cursor.execute(sql, (book_title,))
result = cursor.fetchall()


if result:
    for booj in result:
        print(book[1])
else:
    print('not found')

db.close()
