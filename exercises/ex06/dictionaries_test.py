"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color

__author__ = "730482618"


def test_invert() -> None: 
    Dict_1: dict[str, str] = {'apple': 'cat'}
    assert invert(Dict_1) == {'cat': 'apple'}


def test_favorite_color() -> None: 
    Dict_2: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(Dict_2) == {'blue'}
