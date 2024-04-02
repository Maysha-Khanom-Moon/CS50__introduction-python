def main():
    # 1.
    # name, house = get_student()
    # print(f"{name} from {house}")
    
    # 2. tuple
    # student = get_student()
    # print(f"{student[0]} from {student[1]}")
    # what happend, if we try to change the data
    # so, we have to skip tuple because tuple is immutable
    
    
    # 3. list
        student = get_student()
        if student[0] == "Padma":
            student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # 1.
    # return name, house
    
    # 2.
    # tuple
    # return (name, house)
    
    # 3.
    # list
    return [name, house]



"""
# when we will use tuple over list
--> when we sure that our data immutable
"""


    
if __name__=="__main__":
    main()
