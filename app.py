import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

stuff = input('What would you like to do?\nOption: Insert Book Details, Check Book Details, Check Genre Books\nUser: ').lower()


if 'check' and 'details' in stuff:
        book_title = input("What book are you looking for?\nUser: ").title()
        sql = "SELECT * FROM book WHERE book_name = ?;"
        cursor.execute(sql, (book_title,))
        result = cursor.fetchall()
        if result:
            for book in result:
                    genre_id = book[2]
                    sql = "SELECT * FROM genre WHERE genre_id = ?;"
                    cursor.execute(sql, (genre_id,))
                    result = cursor.fetchall()
                    for genre_name in result:
                        author_id = book[4]
                        sql = "SELECT * FROM author WHERE author_id = ?;"
                        cursor.execute(sql, (author_id,))
                        result = cursor.fetchall()
                        for author in result:
                            print(f'Book ID: {book[0]}  - Book Title:  {book[1]}  - Genre: {genre_name[1]}  - Date: {book[3]}  - Author:  {author[1]}')
                      
        else:
            print('not found')

db.close()