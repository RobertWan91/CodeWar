"""
Implement the "count" decorator, which adds an attribute "call_count" to a function passed in to it,
and increments it every time the function is called.


The behavior of the decorated function must be the same as before. Your decorator must be well-behaved,
i.e. the returned function must have the same name and docstring as the original, and must be able to
handle the same arguments.

"""
from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0  # initialize of the attribute - call_count
    return wrapper






