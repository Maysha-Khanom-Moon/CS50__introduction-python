# def main():
def moon():
    hello("world")
    goodbye("world")
    
    
def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")
    


# main()
# when we import this file then before import specific function it execute main() function automatically. which we do not want!

# if we want to solve this problem:
if __name__ == "__main__":
    # main()
    moon()
# now when we call directly sayings.py then it will works otherwise it didn't call or execute the moon() function


# if we want to use my own created module?
