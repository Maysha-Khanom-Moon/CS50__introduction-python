# if there is multiple commas or extra comma inside of a part

import csv

students = []

with open("csv_list.csv") as file:
    # slipt at each of the comma
    # return a each line as a list
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


for student in sorted(students, key=lambda x: x['name']):
    print(f"{student['name']} is from {student['home']}")