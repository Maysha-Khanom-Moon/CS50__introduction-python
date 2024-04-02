# if we want to store names and home simultaniously then .txt file it's not a good option
# to solve it we will use .csv file
# csv: Comma-separated values 
# A text file format that uses commas to separate values, and newlines to separate records


# row-by-row: students
# comma represent a column


# 1.
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")



# split the line(str) via specific char and return a list



# 2.
# with open("students.csv") as file:
#     for line in sorted(file):
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")





# make a list of dicts
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)


def get_name(student):
    return student["name"]        

# we are sorting our list based on the function specified in the key. And we choose the name-key
# 1.
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

# we can also use reverse=True


# 2.
# we can use lamda function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
    
    
    
# lambda funtion is a small anonymous function
# lambda arguments: expression