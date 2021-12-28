"""Implement the "memoize" decorator, which adds memoization capabilities to a function in order to make it more efficient
. In short, memoization means storing computed values instead of recomputing every time.
In the example below, this means that you only calculate fib(n) once for every n.

The decorated function must return the same values as before for the same inputs. Your decorator must be well-behaved,
 i.e. the returned function must have the same name and docstring as the original.
 """
from functools import wraps


def memoize(func):
    mem_dict = {}

    @wraps(func)
    def wrapper(args):
        if args not in mem_dict:
            mem_dict[args] = func(args)
        return mem_dict[args]
    return wrapper
