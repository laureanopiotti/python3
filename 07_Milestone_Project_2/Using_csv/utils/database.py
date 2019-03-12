'''
Concerned with storing and retrieving books from a csv file.
Format of the csv file:
name,author,read
'''

books_file = 'books.csv'

def create_book_table():
    with open(books_file,'a'):
        pass

def add_book(name,author):
    with open(books_file,'a') as csv_file:
        csv_file.write(f'{name},{author},0\n')
    print(f'Book "{name} by: {author}" has been added.')

def get_all_books():
    with open(books_file,'r') as csv_file:
        books = [book.strip().split(',') for book in csv_file.readlines()]
    return [{'name':book[0],'author':book[1],'read':book[2]} for book in books]

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)

def _save_all_books(books):
    with open(books_file,'w') as csv_file:
        for book in books:
            csv_file.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)