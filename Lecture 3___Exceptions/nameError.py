try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
    
print(f"x is {x}")

# if we input x is cat or float then we got NameError
# NameError: name 'x' is not defined
# Because before assign the value of x, try section crashed


try:
    y = input("what's y? ")
    y = int(y)
except ValueError:
    print("y is not an integer")

# before crash try section we assign the value to y
# NameError will not occur anymore    
print(f"y is {y}")
