'''
Concerned with storing and retrieving books from a json file.
Format of the csv file:
name,author,read
'''
import json

books_file = 'books.json'

def create_book_table():
    with open(books_file,'w') as json_file:
        json.dump([],json_file)

def add_book(name,author):
    books = get_all_books()
    books.append({'name':name,'author':author,'read':False})
    print(f'Book "{name} by: {author}" has been added.')

    _save_all_books(books)

def get_all_books():
    with open(books_file,'r') as json_file:
        return json.load(json_file)

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)

def _save_all_books(books):
    with open(books_file,'w') as json_file:
        json.dump(books,json_file)

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)