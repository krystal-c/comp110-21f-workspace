"""Examples of optional parameters and Union types."""

from typing import Union

# World is the default parameter or the default value. When we call the param. with no argument, it'll produce World. But when we call it with Sally, hopefully it will be Sally. 
# If you have multiple parameters, your default parameters must come at the end, after required parameters. "World" is an optional parameter.
# The ordering matters/is important when it comes to parameters. You can't have int = 1 and have it work after an optional parameter.


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else: 
        greeting += "Alien Life from Sector " + str(name)
    return greeting


# Single argument 

print(hello("Sally"))

# No arguments!
print(hello())

# int Argument works too!
print(hello(110))
print(hello(3.14))