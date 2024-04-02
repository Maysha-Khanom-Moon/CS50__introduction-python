# import all the functionality of random module
import random

# returns a random element from the given sequence or list
coin = random.choice(["heads", "tails"])
print(coin)


# Returns a random number between the given range
num = random.randint(1, 10)
print(num)


# suffle sequence in a random order
num = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(num)
print(num)