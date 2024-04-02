import re

name = input("What's your name? ").strip()

# 1.
# if "," in name:
#     first, last = name.split(", ")
#     name = f"{first} {last}"
# split doesn't support regular expression



# 2.
# matches = re.search(r"^(.+), *(.+)$", name)

# to assign something at if statement use :=
# := assign a value and also ask a boolean question
if matches := re.search(r"^(.+), *(.+)$", name):
    # first, last = matches.groups()
    first = matches.group(1)
    last = matches.group(2)
    name = f"{first} {last}"


print(f"hello, {name}")