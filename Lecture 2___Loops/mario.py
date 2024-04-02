# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")


def main():
    print_column(3)
    print_row(4)
    print_block(3, 4)
    print_square(2)
    

def print_column(height):
    print("#\n" * height, end="")

        
def print_row(width):
    print("?" * width)
    
    
def print_block(height, width):
    
    # for each row in block
    for i in range(height):
        
        # for each brick in row
        for j in range(width):
            
            # print brick
            print("#", end="")
        print()
        
        
def print_square(size):
    for i in range(size):
        print("#" * size)

        
main()