"""List utility functions part 2."""

__author__ = "730482618"

# Define your functions below


def only_evens(number_list: list[int]) -> list[int]:
    """Finds evens numbers in the list."""
    evens: list[int] = []
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0: 
            evens.append(number_list[i])
    return evens


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Makes list which is a subset of the given list."""
    subset_list: list[int] = []
    i: int = 0
    if start < 0:
        start = 0
    if end > len(a_list): 
        end = len(a_list)
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return []
    while i < (len(a_list)):
        if i >= start and i < end:
            subset_list.append(a_list[i])
        i += 1        
    return subset_list


def concat(list_one: list[int], list_two: list[int]):
    """Make a list that combines two lists together."""
    combine_list: list[int] = []
    combine_list = list_one + list_two
    return combine_list 


def main() -> None: 
    """Print the outputs here."""
    print(only_evens([1, 2, 3]))
    print(only_evens([1, 5, 3]))
    print(only_evens([4, 4, 4]))
    print(sub([10, 20, 30, 40], 1, 3))
    print(concat([1, 2, 3], [4, 5, 6]))


main()