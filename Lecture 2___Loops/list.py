# list like an array
students = ["Hermione", "Harry", "Ron"]

# print the list
print(students)


# print the specific item
print(students[0]) # 1st item


# print using loop
for student in students:
    print(student) # items not the index
    
    

# len: length of list
for i in range(len(students)):
    print(i+1, students[i])