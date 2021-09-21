"""Drawing forests in a loop."""

__author__ = "730482618"

# The string constant for the pine tree emoji
from typing import List

TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

i: int = 0
my_list: List[int] = [1, 2, 3, 4, 5, 6]

while i < len(my_list):
    print(my_list[i])
    i += 1
if depth < 1:
    print("0")

for item in my_list:
    print(TREE)