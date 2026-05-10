import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

book_title = input("What book are you looking for?\nUser: ").title()
sql = "SELECT * FROM book WHERE book_name = ?;"
cursor.execute(sql, (book_title,))
result = cursor.fetchall()

if result:
    for book in result:
        print(f'Book: {book[1]}\nDate: {book[3]}')
else:
    print("Not found")

db.close()