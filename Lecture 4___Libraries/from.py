# specifically import the choice attribute only
from random import choice

# we only import the choice, so do not have to use the reference of random.
coin = choice(["heads", "tails"])
print(coin)