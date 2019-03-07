# List comprehension

"""
A list comprehension is a Pythonic way of constructing a list.
"""

#for my_number in range(10):
#    print(my_number)

numbers = list(range(10))
doubled = [n*2 for n in numbers]

phrases = [f'I am {age} years old' for age in doubled]

names_list = ["John", "Rolf", "Anne"]
lowercase_names = [name.lower() for name in names_list]

## With conditional

numbers = list(range(10))
evens = [n for n in numbers if n % 2 == 0]

friends = ['rolf', 'anna', 'charlie']
guests = ['Jose', 'Rolf', 'ruth', 'Charlie', 'michael']

present_friends = [name.capitalize() for name in guests if name.lower() in friends]

# present_friends = [name.capitalize() for name in guests if name.lower() in [f.lower() for f in friends]]

# Set and dictionary comprehension

"""
In the same way that we do list comprehension, we can do set comprehension
"""

friends = {'rolf', 'anna', 'charlie'}
guests = {'jose', 'rolf', 'ruth', 'charlie', 'michael'}

present_friends = friends & guests

"""
We could capitalize them using set comprehension.
"""

present_friends = {name.capitalize() for name in present_friends}

"""
Dictionary comprehension is also possible! All we have to do is create key-value pairs in the for loop.
"""

names = ['Rolf', 'Anna', 'Charlie']
time_last_seen = [10, 15, 8]

friends_last_seen = {names[i]: time_last_seen[i] for i in range(len(names))}

## EXTRA

"""
This is so popular, that there's a built-in function for it!
"""

friends_last_seen = dict(zip(names, time_last_seen))
print(friends_last_seen)