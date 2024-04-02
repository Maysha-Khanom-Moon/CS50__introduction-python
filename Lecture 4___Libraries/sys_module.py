# sys: system

# sys.argv(): system argument vector --> an array for command line arguments in Python

import sys


# python sys_module.py
# print("program name is", sys.argv[0])


# python sys_module.py --> IndexError: list index out of range
# because we are try to get 2nd item
print("hello, my name is", sys.argv[1]) 
# python sys_module.py David

# sys.argv[0] = 1st element after python word

