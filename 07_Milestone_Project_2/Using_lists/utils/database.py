'''
Concerned with storing and retrieving books from a list.
'''

books = []

def add_book(name,author):
    books.append({'name':name,'author':author,'read':False})
    print(f'Book "{name} by: {author}" has been added.')

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]