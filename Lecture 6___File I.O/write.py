# open: its allows us to what you want to read from or write to this file

name = input("What's your name? ")

# 1. open return a file handle
file = open("names.txt", "w")

# 2. write the name inside the file
file.write(name)

# 3. close means effectively save the file
file.close()


# after every execuition we got last input only and before that all disapear!