"""List utility functions."""

__author__ = "730482618"


# TODO: Implement your functions here.

def all(all_in: list[int], number: int) -> bool:
    """Indicating whether or not all the ints in the list are the same."""
    i: int = 0 
    while i < len(all_in): 
        if all_in[i] != number:
            return False
        i += 1
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Indicate if every element at every index is equal in both lists."""
    i: int = 0 
    while i < len(list_one) and len(list_two):
        if list_one == list_two:
            return True
        i += 1
    if len(list_one) and len(list_two) == 0:
        return False
    return False


def max(input_list: list[int]) -> int:
    """Return the largest in the list."""
    maximum = input_list[0]
    for i in input_list:
        if i > maximum:
            maximum = i
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    return maximum


def main() -> None:
    """Print the outputs here."""
    print(all([1, 2, 3], 1))
    print(all([1, 1, 1], 2))
    print(all([1, 1, 1], 1))
    print(all([], 0))
    print(is_equal([1, 0, 1], [1, 0, 1]))
    print(is_equal([1, 1, 0], [1, 0, 1]))
    print(is_equal([], []))
    print(max([1, 3, 2]))
    print(max([100, 99, 98]))


main()
