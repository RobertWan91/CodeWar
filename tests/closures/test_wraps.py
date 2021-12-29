import pytest
from closures.wraps import wraps


def f():
    """This is a test"""
    pass


f.attr = 'This is also a test'
f.__wrapped__ = 'This is still a bald faced lie'


@wraps(f)
def wrapper():
    pass


def test_wraps():
    assert wrapper.__name__ == 'f'
    assert wrapper.__qualname__ == f.__qualname__
    assert wrapper.attr == 'This is also a test'
