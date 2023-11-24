import pytest
from main import is_valid_numeric_input, divide, add

def test_invalid_numeric_input():
    assert is_valid_numeric_input('a', 1) == False

def test_valid_numeric_input():
    assert is_valid_numeric_input(1, 1) == True

def test_add():
    assert add(1,2) == 3

def test_divide_by_zero():
    assert divide(1,0) == "Cannot divide by zero!"

def test_divide_by_nonzero():
    assert divide(6,2) == 3