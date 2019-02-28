# The variables below are all integers (whole numbers).

a = 1
b = 2
c = 3

my_sum = a + b
another_sum = 5 + 10

# Variables can be called anything you like, although there are a few reserved keywords
# and a few other names you should avoid.
# Reserved keywords are those that are part of the language.
# Words you should avoid are those which they themselves are variables.

# In Python we normally use "snake_case" for names. Other languages use "camelCase".
# If you want your code to look more like Python code, use "snake_case"!

# We'll look into this much more throughout the course!

maths_operators = 1 + 3 * 4 / 2 - 2
print(maths_operators)

# A float is a "floating point number"; one with a decimal point.
# Normally division results in a floating point number.

float_division = 12 / 3
print(float_division)

# However, sometimes we want to end up with an integer instead.

integer_division = 12 // 3  # drops anything after the decimal (no rounding!)
print(integer_division)

division_with_reminder = 12 // 5  # should be 2.4
print(division_with_reminder)  # prints 2

# 5 goes into 12 two times. (5 * 2 is 10). The reminder is 2.
# Getting the reminder of a division is such a popular operation, that Python gives us a way to do it really easily.

reminder = 12 % 5
print(reminder)  # prints 2

# Why is it so popular?
# What would the reminder be in these divisions?
#
# 10 / 2
# 14 / 2
# 6 / 2
# 340 / 2
#
# What about these?
#
# 11 / 2
# 27 / 2
# 3 / 2

# For every even number, the reminder when divided by 2 is always 0.
# For every odd number, the reminder when divided by 2 is always 1.

# We can check whether a number is odd or even just by checking the reminder!

x = 37
reminder = x % 2
print(reminder)  # should print 1, therefore it is odd

# We'll look at doing things depending on whether a number is odd or even soon in the course!