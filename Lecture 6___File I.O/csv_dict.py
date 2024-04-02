import csv

students = []

with open("csv_dict.csv") as file:
    # return a each line as a dict
    # here reader is a list of dicts
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# be careful: do not use space around comma at csv file

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is from {student['home']}")
    
    
# if we use dict:
    # if change the column position or
    # if we add more column but still my existing code will be same