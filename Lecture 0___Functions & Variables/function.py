# def: define a function
def hello(to = "world"):
  print("hello,", to)

hello()

def hello():
  print("hello")

name = input("enter you name: ")
hello()
print(name)


def hello(n):
  print(f"hello, {n}")
  print("hello,", n)

hello(name)

# please always maintain scope