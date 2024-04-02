while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
    
print(f"x is {x}")


# or
while True:
    try:
        y = int(input("What's y? "))
        break
    except ValueError:
        print("y is not an integer")

print(f"y is {y}")