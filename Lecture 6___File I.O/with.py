name = input("What's your name? ")

# all 3 steps within in a block
with open("with.txt", "a") as file:
    file.write(f"{name}\n")
    

# for with: we do not have to close(save) the file