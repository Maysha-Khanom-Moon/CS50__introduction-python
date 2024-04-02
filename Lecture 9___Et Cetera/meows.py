# at administrator command prompt: pip install mypy

# def meow(n):
def meow(n: int) -> None:
    # for _ in range(n):
    #     print("meow")
    return "meow\n" * n

# number = int(input("Number: "))
number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meow)
# meow(number)
meows: str = meow(number)
print(meows, end="")


# mypy meows.py: check the type error of variable
# mypy found the issues in the source code


# docstring: just write the methodology and extra info about source code

# def meow(n: int) -> None:
"""
    Meow n times.
    
    param n: Number of times to meow
    type n: int
    raise TypeError: If n is not an int
    return: A string of n meows, one per line
    rtype: str
"""
#    return "meow\n" * n