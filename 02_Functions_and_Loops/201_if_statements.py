programmer = True

if programmer is True:
  print('You are awesome!')
  
# Here we've created a variable which stores the value True.
# Then we've written an if statement which checks if `programmer is True`—if it is, then we're going to run the code below it.
# Notice how the code is indented. That means it has at least 1 more space in front of it than the if statement.
# Any code that is not indented will not be a part of the if statement.

# ----

is_programmer = False

if is_programmer is True:
  print('You are awesome!')
else:
  print('Learn some programming!')

# Here we have a print statement under the if.
# Then, separately and outside of the if statement, we have an else. This allows us to do something only if the `if` didn't run.

# ----

# Python allows us to omit `is True`, as that's the default check:

if is_programmer:
  print('You are awesome!')

# ----

# Instead of checking whether something is True, we can check whether something is False:

if is_programmer is False:
  print('Learn some programming!')
else:
  print('You are awesome!')
  
# And we can also check whether something is not True:

if is_programmer is not True:
  print('Learn some programming!')

# We can also omit the `is True` in this case, but then we have to place the `not` in a different place,
# as that makes more sense in English:

if not is_programmer:
  print('Learn some programming!')

# ----

"""
We can also do multiple checks in one:
"""

is_programmer = False
is_awesome = True

if is_programmer:
  print("You're the best!")
elif is_awesome:
  print("Not the best, but still awesome.")
else:
  print('Be awesome!')

# As a recap, here's what we can do:

# if is_programmer is True:
# if is_programmer:
# if is_programmer is False:
# if not is_programmer:
# else: