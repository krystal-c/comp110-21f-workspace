"""Repeating a beat in a loop."""

__author__ = "730482618"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
number: int = int(input("How many times do you want to repeat it? "))
output = beat
i: int = 0
while i < number - 1:
    output = output + " " + beat
    i += 1
if number < 1:
    print("No beat...")
else:
    print(output) 