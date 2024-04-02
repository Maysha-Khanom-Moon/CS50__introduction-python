# by convention: pascal case for class name
# class: like dict but we just use .key over ["key"]

# import sys

class Student:
    # __init__: instance method --> initialization of object
    def __init__(self, name, house, patronus):
        if not name:
            # 1. 
            # sys.exit("Missing name")
            
            # 2. 
            # return None
            # its not possible because already object created
            # so, its not okay to say there is no obejct
            
            # 3.
            raise ValueError("Missing name")
        
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        self.name = name
        self.house = house
        self.patronus = patronus
        
    # give a intro about each object
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    # own created mathod
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎" # windows + .
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"



def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    
    # print(student)
    # print(f"{student.name} from {student.house}")


def get_student():
    # student is a object from class Student
    # name, house: instance variable of object student
    
    # 1. no need __init__, just need '...'
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    
    
    # 2. via __init__
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)
    try:
        return student
    except Value:
        print(Value)




if __name__=="__main__":
    main()