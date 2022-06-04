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
__set__ = x, y, name, is_cool = (1, 2.5, 'John', True)
# print(__set__)

# Casting
x = str(x)
y = int(y)
z = float(y)

print(x, y, z)
