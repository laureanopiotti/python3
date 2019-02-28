my_string = "Hello world!"
single_quote_string = 'Hello world!'

string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing!" yesterday.'

escaped_quotes = "He said \"You are amazing!\" yesterday."

# ---

# Concatenate
name = 'Jose'
greeting = 'Hello, ' + name
print(greeting)

# f strings
another_greeting = f'Hello, {name}'
print(another_greeting)

# .format
final_greeting = 'How are you, {}'
formatted_greeting = final_greeting.format(name)
print(formatted_greeting)