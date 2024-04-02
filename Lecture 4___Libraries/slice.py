"""
1. slice define a subset of data type list
2. list[1: ] --> give me a subset from 1st index element to rest all of those
3. for list: slice via [] --> like access the items via index
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


# for arg in sys.argv:
for arg in sys.argv[1:]:
    print("hello, my name is", arg) # python slice.py moon khan maysha
print()


# [1: -1] --> negative index count from the last
# slice index 1 upto index (-1)
for arg in sys.argv[1: -1]:
    print("hello, my name is", arg)