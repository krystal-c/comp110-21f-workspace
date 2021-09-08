"""Repeating a beat in a loop."""

__author__ = "730482618"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
number: int = int(input("How many times do you want to repeat it? "))
output: str = " " + " " + " "
i: int = 0
while i < number:
    output = output + beat
    i += 1

print(output) 