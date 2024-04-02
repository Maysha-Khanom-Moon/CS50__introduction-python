name = input("What's your name? ")

# 1. return a file handle which append the inputs
file = open("append.txt", "a")

# 2. append the input inside the file
file.write(f"{name}\n")

# 3. save the file
file.close()


# to see the txt file using CLI: code append.txt


# after appends all the inputs that's not readable enough
# so we can add '\n' after each of the name