import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

stuff = input('What would you like to do?\nOption: Insert Book Details, Check Book Details, Check Genre Books\nUser: ').lower()

if 'check book details' in stuff:
        book_title = input("What book are you looking for?\nUser: ").title()
        sql = "SELECT * FROM book WHERE book_name = ?;"
        cursor.execute(sql, (book_title,))
        result = cursor.fetchall()
        if result:
            for book in result:
                    print(book)
        else:
            print('not found')

db.close()



