# The for loop

"""
The for loop lets us go over each element out of a series of elements. For example, each element of a list.
"""

primes = [2, 3, 5, 7, 11]
for prime in primes:
  print(f'{prime} is  a prime number.')


kid_ages = (3, 7, 12)
for age in kid_ages:
  print(f'I have a {age} year old kid.')

# The range function

"""
Instead of iterating over a pre-existing list, we can use the range() function to iterate over a specific range.
"""

for i in range(20):
  print(i)

"""
Notice that range() doesn't produce a list. We'll talk about what exactly range() is later on in th course!
"""

print(range(10))

# Iteration of dictionaries

"""
Sometimes you need to be able to iterate over a dictionary. It's not too common, but it can be useful!

In the example below, we have a dictionary of friends and how long ago we last saw them.
"""

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

for name, days in my_friends.items():
    print(f'I last saw {name} {days} days ago.')


"""
Notice what .items() gives us:
"""

print(my_friends.items())

"""
So this would be exactly the same as the initial for loop, by using tuple destructuring.
"""
friend_info = [('Jose', 6), ('Rolf', 12), ('Anne', 6)]
for name, days in friend_info:
    print(f'{name}, {days}')

# Extra!

"""
If you want to check whether you have a particular friend you can do so quite easily in Python, without the need to iterate over the dictionary.

Instead of this:
"""

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}
do_i_know = 'Anne'

for name, days in my_friends.items():
    if name == do_i_know:
      print(f'I know {do_i_know}')

"""
You can do this:
"""
my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}
do_i_know = 'Anne'

if do_i_know in my_friends:
  print(f'I know {do_i_know}')

