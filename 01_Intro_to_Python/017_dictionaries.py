"""
A dictionary is very similar to a set, except instead of storing single values like numbers or strings, it associates those values to something else. This is normally a key-value pair.

For example, we could create a dictionary that associates each of our friends' names with a number describing how long ago we last saw them:
"""

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

"""
The same constraints as sets apply, but only on the keys. You cannot have duplicate keys, and the keys are not ordered. The values can be duplicated as many times as you want.

However, you cannot add or subtract dictionaries like you can do with sets.
"""

## Nested dictionaries

"""
You can have anything as the value for a key.

That includes a using a dictionary as a value!
"""

my_friends = {
    'Jose': { 'last_seen': 6 },
    'Rolf': { 'surname': 'Smith' },
    'Anne': 6
}

"""
Notice how the values are each independent objects. They don't need to have the same keys (although they can).
They don't even all have to be dictionaries! They can be anything you want them to be.
"""

## Lists and dictionaries

players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]

# How could we select one of these?

player = players[0]

# How could we add all the numbers of a player?

sum(player['numbers'])

# We have a function that takes in a list—it does not have to be a list of numbers
# of a player. Indeed, we could do something like this:

sum([1, 2, 3, 4, 5])
