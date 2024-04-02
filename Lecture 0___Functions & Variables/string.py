# str
name = "     moon    good"
print(name)

# remove whitespace from str
name = name.strip()
print(name)


# capitalize 1st letter of first word
name = name.capitalize() 
print(name)


# capitalize user's full name
# capitalize 1st letter of every word
name = name.title()
print(name)


# remove whitespace from str and capitalize user's name
name = "\n     moon      good\n"
print(name)
name = name.strip().title()
print(name)

# 
name = input("enter your name: ").strip().title()
print(name)


# split user's name into first name and last name
first, last = name.split(" ")
print("first name:", first)
print(f"last name: {last}")