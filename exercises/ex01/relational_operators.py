"""In this program, you input your name and sentences come out!""" 

__author__ = "730482618" 

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

less: bool = int(left) < int(right)
great_equal: bool = int(left) >= int(right)
equal: bool = int(left) == int(right)
not_equal: bool = int(left) != int(right)

print(left + " < " + right + " is " + str(less))
print(left + " >= " + right + " is " + str(great_equal))
print(left + " == " + right + " is " + str(equal)) 
print(left + " != " + right + " is " + str(not_equal))