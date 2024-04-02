from calculator import square


def main():
    test_square()

# 1.
# def test_square():
    # this code can be pertially break
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")


# 2.
# def test_square():
#     # assert means if any of these wrong then intier code will break
#     assert square(2) == 4
#     assert square(3) == 9
        

# 3.
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")    
        
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")  
    
# but there are lots of lines code for some testing
# to solve this problem we use 'pytest' package library
# pytest check all the case automatically



if __name__ == "__main__":
    main()
    
    
# unit test: typically tests for functions