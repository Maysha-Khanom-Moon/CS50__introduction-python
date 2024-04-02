# properties is a class for maintaining the class attributes

# decorators:  modify the behavior of functions or classes without directly changing their source code


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    # to avoid python confussion: we use different name. 
    # name as property and _name as instance variable. 
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        self._house = house


def main():
    student = get_student()
    # it's possible for setter: @house.setter
    student._house = "Gryffindor"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student



if __name__=="__main__":
    main()