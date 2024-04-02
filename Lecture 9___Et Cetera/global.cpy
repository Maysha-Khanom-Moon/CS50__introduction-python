balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n
    
def withdraw(n):
    global balance
    balance -= n



if __name__=="__main__":
    main()
    
    
# global variable we can use in local scope but can't modify the value of it
# to modify that's value: firstly we have to declare as global variable