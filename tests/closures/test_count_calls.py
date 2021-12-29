from closures.count_calls import count_calls
import pytest


@count_calls
def multiply(a, b=1):
    """Calculates the product of a and b."""
    return a * b


def test_multiply_no_calls():
    assert multiply.call_count == 0


def test_multiply_three_calls():
    for _ in range(3):
        multiply(1, 2)
    assert multiply.call_count == 3

