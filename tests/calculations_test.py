import sys
import os
import math
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import calculations


def test_area_of_circle():
    assert calculations.area_of_circle(0) == 0
    assert calculations.area_of_circle(1) == math.pi
    assert calculations.area_of_circle(2) == math.pi * 4


def test_area_of_circle_negative():
    with pytest.raises(ValueError):
        calculations.area_of_circle(-1)


def test_get_nth_fibonacci_negative():
    with pytest.raises(ValueError):
        calculations.get_nth_fibonacci(-5)


def test_get_nth_fibonacci_base_cases():
    assert calculations.get_nth_fibonacci(0) == 0
    assert calculations.get_nth_fibonacci(1) == 1


def test_get_nth_fibonacci_sequence():
    assert calculations.get_nth_fibonacci(2) == 1
    assert calculations.get_nth_fibonacci(3) == 2
    assert calculations.get_nth_fibonacci(4) == 3
    assert calculations.get_nth_fibonacci(5) == 5
    assert calculations.get_nth_fibonacci(6) == 8