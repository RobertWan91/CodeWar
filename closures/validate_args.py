"""
Implement the validate_args decorator, which raises an error (InvalidArgument) when the decorated function is called
with arguments of the wrong type. Validate_args takes in a sequence of argument types as a variable number of arguments.
You do not have to check that the number of arguments matches, only their type (number of arguments will not be tested).

Your decorator must be well-behaved, i.e. the returned function must have the same name and docstring as the original,
and must be able to handle the same arguments.
"""
from functools import wraps


class InvalidArgument(ValueError):
    pass


def validate_args(*type):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args):
            if all(map(isinstance, args, type)):
                return fn(*args)
            else:
                raise InvalidArgument
        return wrapper
    return decorator

