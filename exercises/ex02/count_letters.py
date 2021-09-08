"""Counting letters in a string."""

__author__ = "730482618"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for?: "))
sentence: str = str(input("Enter a word: "))
count = 0

for i in sentence:
    if i == "A":
        count = count + 1
    elif i == "a":
        count = count + 1
    elif i == "B": 
        count = count + 1

print(count)