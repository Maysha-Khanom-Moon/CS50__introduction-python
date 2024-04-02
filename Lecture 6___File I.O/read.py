# read an existing file

with open("with.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    print(f"hello, {line}")


# file.readlines(): reads all the line of entire file


# we got extra line gap: because we give a '\n' after each line

# "r" is default. So, if we can want then we can skip it