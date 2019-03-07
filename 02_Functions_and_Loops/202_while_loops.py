  # The `while` loop

"""
The `while` loop allows us to repeat a block of code for as long as a condition is `True`.
"""

is_programmer = True
while is_programmer:  # is_programmer is True
  print('Hello, world!')
  is_programmer = False

"""
It can also be used to repeat something a number of times:
"""

i = 0
while i < 10:
  print(f'Repeated {i} times')
  i += 1

"""
A common use of the while loop is to do things like these:
"""

temperature = 15

while temperature < 20:
  print('Heating...')
  temperature += 1

"""
Only instead of the temperature increasing continuously, we would e.g. get it from a sensor.

Remember to always have a way of exiting the loop! Otherwise it will run endlessly!
"""