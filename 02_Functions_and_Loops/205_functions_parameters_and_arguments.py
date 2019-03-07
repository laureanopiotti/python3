"""
We’ve learned a whole bunch of Python already, from variables and types of data to loops, if statements, and dictionaries. Functions are an entirely new concept, but I’m sure you’ll grasp it very quickly.

A function is a name for a block of code.

Any piece of code you have, you can turn it into a function. For example, the following code which asks the user for their name and prints a greeting:
"""

name = input('Enter your name: ')
print(f'Hello, {name}!')

"""
If you type that code into a file and run the file, you’d immediately be asked to enter your name, and then a greeting would be printed as soon as you press ‘Enter’.

We can /extract/ the code into a function, which just means give the code a name:
"""

def greet():
  name = input('Enter your name: ')
  print(f'Hello, {name}!')

"""
The new line is the /function definition/, which is always made up of:

* `def`, the Python keyword to define a new function;
* The function name, which can include letters, numbers, and underscores;
* A pair of brackets. Things can go inside these brackets, as we’ll see shortly; and
* A colon (`:`), to signal the start of the block.
* The lines contained in the function (those you want to run when the function runs) need to be indented.

> Type that code to a file and run it. What happens?

If you type the function to a file and run the file, you’ll see nothing is printed out. That’s because defining a function does not run it. We need to run the function separately.

> In Python and indeed programming as a whole, you’ll frequently read that a function can be ran, executed, or called. They’re all the same thing!

To run the function, we could just do this:
"""

def greet1():
  name = input('Enter your name: ')
  print(f'Hello, {name}!')

greet1()

"""
Notice how we’ve defined our function; its contents are more indented; and then in less indentation we’ve called (or ran, or executed) the function by typing its name and the opening and closing brackets.
"""

## Function arguments

"""
Sometimes a function will need some data in order to do what it must. For example, recently we looked at some code that checked whether a number was prime or not:
"""

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')

"""
It’s a rather long piece of code, maybe a bit difficult to understand. If I didn’t tell you what it does, it may not be very clear. By creating functions, we can make the code more understandable:
"""

# for n in range(2, 10):
#   check_if_prime(n)

"""
Naturally we need to define the `check_if_prime` function:
"""

def check_if_prime(number):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')

for n in range(2, 10):
  check_if_prime(n)

"""
Now we have a function that, given a number, it checks whether it is a prime or not.

We could split it into more functions:
"""

def find_primes(limit):
  for n in range(2, limit):
    check_if_prime1(n)

def check_if_prime1(number):
  for x in range(2, number):
    if number % x == 0:
      print(number, 'equals', x, '*', number//x)
      break
  else:
    # loop fell through without finding a factor
    print(number, 'is a prime number')

find_primes(18)

"""
Now our program is more extensible because our `find_primes` function takes in a `limit` argument, which is the upper limit of the range in which to search for primes.

I think now the code is more readable, because we have two functions being defined and *the code we are running* is one called `find_primes`. That’s probably going to find prime numbers!
"""