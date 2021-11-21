"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730482618"


def test_sub() -> None: 
    List_1: list[int] = [10, 20, 30, 40]
    assert sub(List_1, 1, 3) == [20, 30]


def test_only_evens() -> None: 
    List_2: list[int] = [12, 13, 14, 15]
    assert only_evens(List_2) == [12, 14]


def test_concat() -> None:
    List_3: list[int] = [70, 80, 90]
    List_4: list[int] = [100, 110, 120]
    assert concat(List_3, List_4) == [70, 80, 90, 100, 110, 120]

    