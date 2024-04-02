"""
# for sys module:
--> Mostly its hard to remember to give extra arguments after python name.py

--> here we can error handling
"""

import sys

# ------- 1. -------
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
# we can also use ValueError


# ------- 2. --------
# if we want to print full name: python name.py "Maysha Khanom Moon"
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])


# ------- 3 -------
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])