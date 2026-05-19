import sqlite3

DATABASE = 'book.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

# Insert book details into the data
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
# ---------------------------------------------------------------------------------------------------------------------------------------------------#

# Print all the books sorted by a specific genre
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

# --------------------------------------------------------------------------------------------------------------------- #

# Check the details on a specific book by its book ID
def check_book_id():
        while True:
            book_id = input("Book ID: ")
            try:
                int(book_id)
                break
            except ValueError:
                 print('Invalid input')
        sql = "SELECT * FROM book WHERE book_id = ?;"
        cursor.execute(sql, (book_id,))
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
# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Print all the books that were made by a specific author
def print_book_author():
     author = input('Author name: ').title()
     sql = "SELECT * FROM author WHERE author_name = ?;"
     cursor.execute(sql, (author,))
     result = cursor.fetchall()
     if result:
        for author_book in result:
            author_id = author_book[0]
            sql = "SELECT * FROM book WHERE author_id = ?;"
            cursor.execute(sql, (author_id,))
            result = cursor.fetchall()
            print(f"book_name                              genre_id        book_id  year_released  author_name")
            for book in result:
                print(f"{book[1]:<39}{book[2]:<16}{book[0]:<9}{book[3]:<15}{author_book[1]:<10}")
     else:
          print('author not found')
     db.close()

# ------------------------------------------------------------------------------------------------------------------------ #

# Print all the books sorted by the year they were published
def print_allbook_year():
     while True:
        year = input('Year: ')
        try:
          int(year)
          break
        except ValueError:
            print('Invalid input')
     sql = "SELECT * FROM book WHERE book_date >= ?;"
     cursor.execute(sql, (year,))
     result = cursor.fetchall()
     if result:
            print(f"book_name                              genre_id        book_id  year_released  author_id")
            for book in result:
                print(f"{book[1]:<39}{book[2]:<16}{book[0]:<9}{book[3]:<15}{book[4]:<10}")
     else:
          print('book not found')
     
     db.close()

# ----------------------------------------------------------------------------------------------------------------- #


# Insert book details into the data 
def insert_book_details():
     inst_book = input('Book title: ').title()
     numberG = 1
     sql = "SELECT genre_name FROM genre;"
     cursor.execute(sql,)
     result = cursor.fetchall()
     print("Genre Avalaible:")
     for genre_list in result:
          numberG += 1
          print(f"{numberG}. ".join(genre_list))
     

     



# FINISHED WITH THE QUESTIONS.

while True:
     user_input = input("What would you like to do?\n(1) Insert book details into the data\n(2) Check the details on a specific book by the name\n(3) Check the details on a specific book by its book ID\n(4) Print all the books sorted by a specific genre\n(5) Print all the books that were made by a specific author\n(6) Print all the books sorted by the year they were published\n(7) Exit\nEnter the number: ")
  
     #Insert book details into the data
     if user_input == 1:
          insert_book_details()
     #Check the details on a specific book by the name
     elif user_input == 2:
          check_book_details()
     #Check the details on a specific book by its book ID
     elif user_input == 3:
          check_book_id()
    #Print all the books sorted by a specific genre
     elif user_input == 4:
          print_book_genre()
     # Print all the books that were made by a specific author
     elif user_input == 5:
          print_book_author()
    #Print all the books sorted by the year they were published
     elif user_input == 6:
          print_allbook_year()
     
     elif user_input == 7:
          break
     
     else:
        print('Invalid input')

  





