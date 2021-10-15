"""List utility functions."""

__author__ = "730482618"


# TODO: Implement your functions here.

def all(all_in: list[int], number: int) -> bool:
    i: int = 0 
    while i < len(all_in): 
        if all_in[i] != number:
            return False
        i += 1
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    i: int = 0 
    while i < len(list_one) and len(list_two):
        if list_one == list_two:
            return True
        i += 1
    return False


def max(input_list: list[int]) -> int:
    maximum = input_list[0]
    for i in input_list:
        if i > maximum:
            maximum = i
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    return maximum


def main() -> None:
    print(all([1, 2, 3], 1))
    print(all([1, 1, 1], 2))
    print(all([1, 1, 1], 1))
    print(is_equal([1, 0, 1], [1, 0, 1]))
    print(is_equal([1, 1, 0], [1, 0, 1]))
    print(max([1, 3, 2]))
    print(max([100, 99, 98]))


main()
