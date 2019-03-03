"""
Now that we’ve covered functions in some of their forms, we can look at functions with no names.

> Wait… Didn’t I say functions are names for blocks of code?

I did say that… Sorry! I lied. Kinda.

We can also have anonymous functions, which are useful in a small but important number of places. In this section I just want to tell you about anonymous functions: how to create them and how to use them. In a future section (soon!) we’ll look into places where they can be very useful.

Here’s a function, and its equivalent lambda function:
"""

def add_two(x, y):
    return x + y

lambda x, y: x+y

"""
But… how do you call them?
"""

add_two(10, 5)  # 15

# ???
(lambda x, y: x+y)(10, 5)  # 15

"""
Wait, that’s extremely unreadable! Yes, it is. Let’s talk more about how to use them in a moment…

The structure of the lambda function is:

* The `lambda` keyword;
* The arguments, separated by commas;
* A colon (`:`);
* And what the function should return.

> Lambda functions only take some inputs and return something—they cannot have multiple lines like normal functions.

Something to remember: in any place where you can use a function, you can use a lambda function. And vice versa.
"""

## First class functions
"""
Functions in Python can be “first class functions”. That means functions themselves can be arguments to other functions! Take this example:
"""

def who(data, identify):
    return identify(data)

def my_identifier_function(data):
    return data['name']

user = { 'name': 'Jose', 'surname': 'Salvatierra' }

print(who(user, my_identifier_function))

"""
This is a very common way of using first class functions in Python.

You have a function that does something, but it is extended by the functionality of another function you pass in. That way, you can decide what the `who` function is going to retrieve from the data.

For this to make sense, assume you don’t have access to modifying the `who` function, because it is part of Python or it was written by someone else.

Now, we could re-write that example more concisely using lambda functions:
"""

def identifier(data, identify):
    return identify(data)

user = { 'name': 'Jose', 'surname': 'Salvatierra' }

print(identifier(user, lambda x: x['name']))

"""
Instead of defining a function that needs a name and so forth, we can just create one right where it is used, that does exactly the same thing with less verbosity.

Lambda functions are very useful when using first class functions.
"""

## Higher order functions

"""
The `identify` function above was a first class function, because it was passed as an argument.

The `who` function, which accepted and used a function as an argument, is called a *higher order function*. That’s just some lingo for you to know!

Some programming languages don’t support first class and higher order functions, but as we’ll see throughout the course they may end up being quite handy!
"""