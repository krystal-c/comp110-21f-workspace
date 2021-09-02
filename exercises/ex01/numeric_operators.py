"""In this program, you input your name and sentences come out!""" 

__author__ = "730482618" 

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
 
power: int = int(left) ** int(right)
divide: float = float(left) / float(right)
total: int = int(left) // int(right)
remainder: int = int(left) % int(right)

print(left + " ** " + right + " is " + str(power))
print(left + " / " + right + " is " + str(divide))
print(left + " // " + right + " is " + str(total))
print(left + " % " + right + " is " + str(remainder))