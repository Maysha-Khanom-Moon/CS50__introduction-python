# placeholder: ...
import random

class Hat:
    # 1. 
    # def __init__(self):
    #     self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # 2.
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    
    # 1.
    # def sort(self, name):
    
    # 2.
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# 1.
# hat = Hat()
# hat.sort("Harry")

# 2.
Hat.sort("Harry")