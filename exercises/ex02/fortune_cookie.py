"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730482618"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

# Begin your solution here...
import random

print("Your fortune cookie says...")
random_int: int = random.randint(1, 4)
if random_int == 1:
    print("Don't pursue happiness--create it.")
elif random_int == 2:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
elif random_int == 3: 
    print("All things are difficult before they are easy.")
elif random_int == 4:
    print("The usefulness of a cup is in its emptiness")
else:  
    print("Now go and spread positive vibes!")