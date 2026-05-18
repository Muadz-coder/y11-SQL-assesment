import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

def check_book_details():
        book_title = input("Book Title: ").title()
        sql = "SELECT * FROM book WHERE book_name = ?;"
        cursor.execute(sql, (book_title,))
        result = cursor.fetchall()
        if result:
            for book in result:
                    genre_id = book[2]
                    sql = "SELECT * FROM genre WHERE genre_id = ?;"
                    cursor.execute(sql, (genre_id,))
                    result = cursor.fetchall()
                    for genre in result:
                        author_id = book[4]
                        sql = "SELECT * FROM author WHERE author_id = ?;"
                        cursor.execute(sql, (author_id,))
                        result = cursor.fetchall()
                        for author in result:
                            print(f'Book ID: {book[0]}  - Book Title:  {book[1]}  - Genre: {genre[1]}  - Date: {book[3]}  - Author:  {author[1]}')
                      
        else:
            print('book not found')
        
        db.close()

def print_book_genre():
     genre = input('Genre name: ')
     sql = "SELECT * FROM genre WHERE genre_name = ?;"
     cursor.execute(sql, (genre,))
     result = cursor.fetchall()
     if result:
        for genre_book in result:
            genre_id = genre_book[0]
            sql = "SELECT * FROM book WHERE genre_id = ?;"
            cursor.execute(sql, (genre_id,))
            result = cursor.fetchall()
            print(f"book_name                              genre_name        book_id  year_released  author_id")
            for book in result:
                print(f"{book[1]:<39}{genre_book[1]:<18}{book[0]:<9}{book[3]:<15}{book[4]:<10}")
     else:
          print('genre not found')
     db.close()

     









def insert_book_details():
     inst_book = input('Book title: ')
     sql = "SELECT * FROM genre;"
     cursor.execute(sql,)
     result = cursor.fetchall()

     






print_book_genre()

