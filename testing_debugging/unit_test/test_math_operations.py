"""
pip install pytest
pytest filename.py
"""

import pytest
from math_operations import add, subtract, multiply, divide

# Test addition
def test_add():
    assert add(2, 3) == 5  # Test addition with positive numbers
    assert add(-1, 1) == 0  # Test adding negative and positive
    assert add(0, 0) == 0  # Test adding zeros

# Test subtraction
def test_subtract():
    assert subtract(5, 3) == 2  # 5 - 3 = 2
    assert subtract(3, 5) == -2  # 3 - 5 = -2
    assert subtract(0, 0) == 0  # 0 - 0 = 0

# Test multiplication
def test_multiply():
    assert multiply(2, 3) == 6  # 2 * 3 = 6
    assert multiply(-1, 5) == -5  # -1 * 5 = -5
    assert multiply(0, 10) == 0  # 0 * 10 = 0

# Test division
def test_divide():
    assert divide(6, 3) == 2  # 6 / 3 = 2
    assert divide(7, 2) == 3.5  # 7 / 2 = 3.5
    
    # Test division by zero, expecting a ValueError
    with pytest.raises(ValueError):
        divide(5, 0)
