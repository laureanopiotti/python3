import sqlite3

db_file = 'data.db'

def create_book_table():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()

def add_book(name,author):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))

    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')

    # books = cursor.fetchall() # List of tuples [(name,author,read),(name,author,read)]
    books = [{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()]

    connection.close()

    return books
