# A variable is a container for a value, which can be of various types

'''
This is a
multiline comment or docstring(use to define a functions purpose)
It can be in single or double quotes
'''

"""
Pep8 - Triple should be used for docstring

VARIABLE RULES:
    - Variables names are case sensitive(name and NAME are different variables)
    - Must start with a letter or an underscore
    - Can have numbers in the variable but cannot start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str (strings can have single or double quotes
# is_cool = True  # bool

# Multiple Assignments
# __set__ = x, y, name, is_cool = (1, 2.5, 'John', True)
# # print(__set__)
#
# # Casting
# x = str(x)
# y = int(y)
# z = float(y)
#
# print(x, y, z)

# -- Strings --

#Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'J'
age = 39

# Concatenate
# print('Hello, my name is ' + name +  ' and I am ' + str(age))

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))
#
# # F-Strings (Python 3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# # String Methods
#
# s = 'hello world'
#
# # Capitalize string
# print(s.capitalize())
#
# # Make all uppercase
# print(s.upper())
#
# # Make all lower
# print(s.lower())
#
# # Swap case
# print(s.swapcase())
#
# # Get length -- Important and can be utilized for any data type
# print(len(s))
#
# # Replace
# print(s.replace('world', 'everyone'))
#
# # Count
# sub = 'h'
# print(s.count(sub))
#
# # Starts with
# print(s.startswith('hello'))
#
# # Ends with
# print(s.endswith('d'))
#
# # Split into a list
# print(s.split())
#
# # Find position
# print(s.find('r'))
#
# # Is all alphanumeric
# print(s.isalnum())
#
# # Is all alphabetic
# print(s.isalpha())
#
# # Is all numeric
# print(s.isnumeric())

# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
# numbers = [1, 2, 3, 4, 5]
# fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
#
# # Use a Constructor
# # numbers2 = list((1, 2, 3, 4, 5))
#
# # Get a value
# print(fruits[1])
#
# # Get length
# print(len(fruits))
#
# # Append to list
# fruits.append('Mangos')
#
# # Remove from list
# fruits.remove('Grapes')
#
# # Insert into position
# fruits.insert(2, 'Strawberries')
#
# # Change value
# fruits[0] = 'Blueberries'
#
# # Remove with Pop
# fruits.pop(2)
#
# # reverse list
# fruits.reverse()
#
# # Sort list
# fruits.sort()
#
# # Reverse sort
# fruits.sort(reverse=True)
#
# print(fruits)

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# # Create tuple
# fruits = ('Apples', 'Oranges', 'Grapes')
# #fruits2 = tuple(('Apples', 'Oranges', 'Grapes')
#
# # Single value needs trailing comma
# fruits2 = ('Apples',)
#
# # Get value
# print(fruits[1])
#
# # Can't change value
# # fruits[0] = 'Pears'
#
# # Delete tuple
# del fruits2
#
# print(len(fruits))
#
# # A set is a collections which is unordered and unindexed. No duplicate members.
#
# # Create set
# fruits_set = {'Apples', 'Oranges', 'Mango'}
#
# # Check if in set
# print('Apples' in fruits_set)
#
# # Add to set
# fruits_set.add('Grape')
#
# # Clear set
# fruits_set.clear()
#
# # Delete Set
# del fruits_set
#
# print(fruits_set)

# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
# person = {
#     'first_name': 'John',
#     'last_name': ' Doe',
#     'age': 30
# }
#
# # Use constructor
# # person2 = dict(first_name='Sara', last_name='Williams')
#
# # Get value
# print(person['first_name'])
# print(person.get('last_name'))
#
# # Add key/value
# person['phone'] = '555-555-5555'
#
# # Get dict keys
# print(person.keys())
#
# # Get dict items
# print(person.items())
#
# # Copy dict
# person2 = person.copy()
# person2['city'] = 'Florida'
#
# # Remove item
# del(person['age'])
# person.pop('phone')
#
# # Clear
# person.clear()
#
# # Get length
# print(len(person2))
#
# # List of dict
# people = [
#     {'name': 'Martha', 'age': 30},
#     {'name': 'Kevin', 'age': 25}
# ]
# print(people[1]['name'])

# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

# create function


def say_hello(name):
    print(f'Hello {name}')


say_hello('John Doe')

# Return value


def get_sum(num1, num2):
    total = num1 + num2
    return total


num = get_sum(3, 5)
print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
# add_sum = lambda num1, num2: num1 + num2
def add_sum(num1, num2): return num1 + num2


print(add_sum(10, 3))

