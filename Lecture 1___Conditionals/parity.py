def main():
  x = int(input("what's x: "))

  if is_odd(x):
    print ("Odd")

  else:
    print("Even")

  
  if is_even(x):
    print("even")

  else:
    print("odd")


  if is_zero(x):
    print("zero")

  else:
    print("not zero")


def is_odd(n):
  return n % 2

def is_even(n):
  return True if n % 2 == 0 else False
  # if(n%2==0):
  #   return True
  # else:
  #   return False

def is_zero(n):
  return n == 0


main()