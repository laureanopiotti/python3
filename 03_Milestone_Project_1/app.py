'''
- Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find movie
- Stop running program

Tasks:
[X]: Decide where to store movies
[X]: What is the format of a movie?
[X]: Show the user the main interface and get their input
[X]: Allow users to add movies
[X]: Allow users to show all their movies
[X]: Find a movie
[X]: Allow users to stop the program when 'q' is typed
'''

movies = []

'''
movie = {
    'name': ...(str),
    'director': ...(str),
    'year': ...(int)
}
'''

def menu():

    user_input = input('''\na. Add movie\nl. Show all movies\nf. Find movie\nq. Quit\n\nPlease enter an option: ''')

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('\nUnknown command. Please try again.\n')
        
        user_input = input('''\na. Add movie\nl. Show all movies\nf. Find movie\nq. Quit\n\nPlease enter an option: ''')

    if user_input == 'q':
        print('\nExiting program...\n')

def add_movie():
    movie_name = input('Enter movie name: ')
    movie_director = input('Enter movie director: ')
    movie_year = input('Enter movie release year: ')

    movies.append({
        'name': movie_name,
        'director': movie_director,
        'year': movie_year
    })

def show_movies(items):
    for i in items:
        print(f'''Movie: {i['name']} - Director: {i['director']} - Year:{i['year']}''')


def find_movie():
    find_by = input('What property of the movie are you looking for?: ')
    looking_for = input('What are you searching for?: ')

    found_movies = find_by_attribute(movies,looking_for, lambda x: x[find_by])

    show_movies(found_movies)

def find_by_attribute(items,expected,finder):

    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found

menu()