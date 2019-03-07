"""
A Boolean is a true/false, yes/no, one/zero value.
We can use it to make decisions.
In Python, True and False are keywords to represent these values.
"""

truthy = True
falsy = False

# ----

age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

"""
Other symbols are > and <=.

We can of course compare two variables, as below. We ask the user for a number, and check that it matches our 'secret number'.
"""

my_number = 5
user_number = int(input("Enter a number: "))

print(my_number == user_number)
print(my_number != user_number)


# Logical comparison of Booleans.

## AND

"""
`and` is used to get two Booleans and check whether they are both True. If either or both are not True, then the resultant expression is also False.
"""

yes = True and True
no = True and False

print(no)

## OR

"""
`or` is used to get the second value if the first one is False. If the first one is True, it gets the first one.
"""

which_one_is_it = True or False
second_one = False or True
first_one = True or True
neither = False or False

## NOT

"""
`not` is used to invert the Boolean. Gets the opposite value!
"""

absolutely = not False
another_no = not True

# ----

# These can be used with variables as well, of course!

is_programmer = True
is_learning = False

awesome = is_programmer and is_learning
less_awesome = is_programmer and not is_learning

"""
They can also be used together in any way you can imagine
Just like in maths equations, brackets give part of the expression precedence, so it runs first
It's also a bit nicer to read.
"""

is_designer = False

great_guy = (is_programmer or is_designer) and is_learning