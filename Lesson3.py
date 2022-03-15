# All about strings

# What is a string
# A string is a sequence of characters. It can be defined with either single
# or double quotes
# Single quotes
alpha = 'Hello'

# double quotes
beta = "Python"

# print results
print(alpha)
print(beta)

# A multi-line string uses three single or three double quotes and allows
# a string to be created on multiple lines.
multi = '''This string can be seen
on multiple lines so you could do
paragraphs if you wanted'''
print(multi)

# getting a specific index using the square bracket []
charlie = 'Happy'
print(charlie[2])

# if you put in a value of the index that is higher than the number of
# characters -1 you will generate an error
# print(charlie[5])

# slicing and range of characters
# using the same square brackets, you can output a range of characters
# from a string, this is called slicing. you use a colon to separate
# the start and end of the slice
delta = 'Enjoy Python'
print(delta[2:5])
# output should be joy

# negative slicing we use negative numbers, instead of starting at zero,
# it starts at the end of the string
print(delta[-5:-2])
# the output should be yth

# What is check string
# This technique is the ability to compare a set of characters with the string
# variable. This result will be either true or false. We use in or not in
# keywords for check string
# using the in keyword
txt = 'This is a test sentence'
result =  'is' in txt

# using the not in keyword
txt2 = 'This other phrase is also a test'
result2 = 'th' not in txt2

print(result)
print(result2)

# string concatenation in Python is the ability to join 2 or more strings
# using the + operator.
# basic concatenation
cat1 = "happy"
cat2 = "Friday"
combine = cat1 + cat2
print(combine)
combine2 = cat1 + " "+ cat2
print(combine2)

cat3 = 'Sample'
combine3 = cat3 + ' Code'
print(combine3)

# longer concatenation with more than 2 values
combine4 = cat1 + ' ' + cat2 + ' ' + combine3
print(combine4)

# What about strings and a number
# combine5 = cat3 + 5
# print(combine5)

# basic string format method using only a curly brace
age = 4
msg1 = 'my dog is {} years old'
print(msg1.format(age))

# string format using indexing
msg2 = 'My dog {1} is {0} years old'
print(msg2.format(age, 'spot'))

# Optional format
name = 'John'
total = 34.9856
msg3 = 'Hello {0}, your order comes to {1:6.2f}'
print(msg3.format(name, total))

# octal escape sequence '\110\145\154\154\157'
value_0 = '\110\145\154\154\157'
print(value_0)

# Escape Sequences allows you to use characters that are reserved using
# a backslash
value_more = 'That\'s a cool toy. \tCan I\n play with it?'
print(value_more)

# String methods are methods built into python
value_string = ' Hello, World '

print(value_string.strip())

# lower()
print(value_string.lower())

# upper()
print(value_string.upper())

# replace()
print(value_string.replace('e', 'a'))

# split()
print(value_string.split(','))


value_more = 'hello python'

# capitlize()
print(value_more.capitalize())

value_upper = 'PYTHON'

# casefold()
print(value_upper.casefold())

# centered()
print(value_more.center(40))
