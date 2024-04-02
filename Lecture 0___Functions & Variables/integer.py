# int: +, -, *, /, %
x = 2
y = 3
print(x+y)


# input function by default take string

x = input("enter x: ")
y = input("enter y: ")
print("without type casting, x+y: "+x+y)


# x = float(x)
w = int(input("enter w: "))
z = int(x) + int(y) + w
print(f"x+y+w: {z}")
print("x+y+w: " + str(z))


# one line code(not readable)
print(int(input("x: ")) + int(input("y: ")))


# int() not able to do type cast from float type string
# but can do on actual float values or integer type string