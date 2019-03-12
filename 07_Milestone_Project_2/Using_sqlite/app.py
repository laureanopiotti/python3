from utils import database

USER_CHOICE = '''
Enter:

- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete book
- 'q' to quit

Your choice: '''

def menu():
    database.create_book_table()
    
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command. Please try again')

        user_input = input(USER_CHOICE)


def prompt_add_book():
    '''Prompts user to input book name and author'''
    name = input('Enter the book name: ')
    author = input('Enter the book author: ')

    database.add_book(name,author)

def list_books():
    books = database.get_all_books()
    for book in books:
        is_read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}. Read: {is_read}")

def prompt_read_book():
    name = input('Enter the name of the book you read: ')

    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input('Enter the name of the book you want to delete: ')

    database.delete_book(name)

if __name__ == '__main__':
    menu()