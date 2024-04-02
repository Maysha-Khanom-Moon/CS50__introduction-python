# Can I go and 'try' to do something 'except' something goes wrong
# except ValueError: when try code crash

# try statement:
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
    
except ValueError:
    print("x is not an integer")
    
    

"""
try:
    // block of codes

except TypeOfError:
    // if try block crash

else:
    // if try block works
"""