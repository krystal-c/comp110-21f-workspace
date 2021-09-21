"""Finding duplicate letters in a word."""

__author__ = "730482618"

word: str = (input("Enter a word: "))
dup: bool = False

i: int = 0

while i < len(word):
    r = i + 1
    while r < len(word):
        if word[i] == word[r]:
            dup = True
        r += 1
    i += 1

print("Found duplicate: " + str(dup))