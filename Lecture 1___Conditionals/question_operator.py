# >, >=, <, <=, ==, !=
# Indentation(the spaces at the beginning of a code line) is must. 


x = int(input("what's x: "))
y = int(input("what's y: "))

if x < y:
  print("x is less than y")

# elif: else + if
elif y < x:
  print("x is greater than y")

else:
  print("x and y are equal")


if x < y or x > y:
  print("x is not equal to y")

else:
  print("x is equal to y")


if x == y:
  print("x is equal to y")

else:
  print("x is not equal to y")


