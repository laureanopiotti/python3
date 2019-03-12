from database_connection import DatabaseConnection

db_file = 'data.db'

def create_book_table():
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        # connection = sqlite3.connect(db_file)

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

        # connection.commit()
        # connection.close()

def add_book(name,author):
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))


def get_all_books():
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')

        # books = cursor.fetchall() # List of tuples [(name,author,read),(name,author,read)]
        books = [{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()]

    return books

def mark_book_as_read(name):
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))


def delete_book(name):
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?',(name,))
