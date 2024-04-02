# input
print("what's your origin? ")
input()

print("hello, world \n")

# ask user for their name
name = input("what's your name? ")

# say hello to user (one argument)
# at first do concatenation then print. so, one argument
print("hello, " + name)

# by default create a space to run multiple argument
# two argument
print("hello,", name)


# another way
print("hello, ", end="???\n")
# by default end = '\n' and here we are just overwriting. 
print("hello,", name, name, sep="??", end='\n\n')

# format string
# without f it will show just {name}, not the value of name
print(f"hello, {name}")
# f: format and "": string

# using of citation
print('hello, "friend"')
print("hello, \"friend\"")

"""
multiline code
comment

# print function:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
=> sep works when those are separated by comma(,)s


# function called via values: arguments
# function created via varibales: parameters


# '\n': go to new line
"""