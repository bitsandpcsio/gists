import pytest
from add_3_numbers import add_3_numbers

def test_add_3_numbers_1():
    assert add_3_numbers(1, 1, 1) == 3

def test_add_3_numbers_2():
    assert add_3_numbers(7, 1, 3) == 11

def test_add_3_numbers_3():
    assert add_3_numbers(45, 897, 999) == 1941
