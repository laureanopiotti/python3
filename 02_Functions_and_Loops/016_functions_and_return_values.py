"""
Let me tell you about another thing functions can do which is extremely useful: return values.

Returning values can be a bit confusing at first—just code along with me and play around with your code to see what the changes do. That’ll help you understand things better as we go along!

The following functions calculate `5 + 5` (let’s start simple!). One of them returns the value, the other one prints it:
"""

def i_return():
  return 5 + 5

def i_print():
  print(5 + 5)

result = i_return()
# another1 = i_print()

print(result)
# print(another1)

"""
What do you think are the values of the variables `result` and `another` when you run that code?

Go ahead, type it into a file and run the file!

Many students are initially confused, because printing a value tells it to the user (sends the data to the text interface), but the function actually returns `None`! That’s the default return value for all functions in Python.

When we `return`, the function sends back the value of whatever it is we return. In this case, it sends back `10`.

If you wanted to both have the value in a variable *and* tell it to the user, you’d have to do both:
"""

def fives():
  addition = 5 + 5
  print(addition)
  return addition

result = fives()
print(result)

"""
*Important*: when we reach a `return`, the function finishes and sends that value back. We cannot have the `print` after the `return`, as the function would’ve already exited.

In the function `fives()`, we define a variable `addition`, and return that. But also important, we don’t return a variable. We return the variable’s value!

If you try to use the variable `addition`, you’ll get an error because it doesn’t exist. For example, the following code would give you an error:
"""

def error_fives():
  addition = 5 + 5
  print(addition)
  return addition

error_fives()
# print(addition)

"""
Because our variable was created inside the function, it does not exist outside of it. *Variables only exist in the block in which they are defined*. That is the concept of *scope* in Python.

> Remember a block is any piece of code that is indented more than the previous code and follows a colon!
"""