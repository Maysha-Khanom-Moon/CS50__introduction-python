# rstrip(): removes any trailing characters (characters at the end a string)
# space is the default trailing character to remove.

with open("with.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

        
# here we just got the content of each line, we do not carried '\n'
# because '\n' not the content of line, that one '\n' just used to create a new line