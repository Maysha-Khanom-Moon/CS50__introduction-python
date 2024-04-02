# book: list of dict

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffinder", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
    # None: represent absence of the value
]

for student in students:
    print(f"{student["name"]}'s house is {student["house"]} and patronus is {student["patronus"]}")