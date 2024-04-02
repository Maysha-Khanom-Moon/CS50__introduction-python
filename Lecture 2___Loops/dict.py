# dict: dictionary
# something with something
# keys and values

"""
dict:
-----
1. use carly braces
2. key-value pairs
3. kind of map in c++
4. we used keys as an index, and key can be a string
5. we will get keys in for loop as index

"""

students = {
    "Hermione": "Gryffinder",
    "Harry": "Gryffinder",
    "Ron": "Gryffinder",
    "Draco": "Slytherin"
}

print(students["Hermione"])

for student in students:
    print(f"{student}: {students[student]}") # keys