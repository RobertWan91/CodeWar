import pytest
from closures.memoize import memoize


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


