from functools import partial
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)


def update_wrapper(wrapper,
                   wrapped,
                   assigned=WRAPPER_ASSIGNMENTS,
                   updated=WRAPPER_UPDATES):
    """Update a wrapper function to look like the wrapped function
       wrapper is the function to be updated
       wrapped is the original function
       assigned is a tuple naming the attributes assigned directly
       from the wrapped function to the wrapper function (defaults to
       functools.WRAPPER_ASSIGNMENTS)
       updated is a tuple naming the attributes of the wrapper that
       are updated with the corresponding attribute from the wrapped
       function (defaults to functools.WRAPPER_UPDATES)
    """
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    # TODO: worth further investigation
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper


def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):
    """Decorator factory to apply update_wrapper() to a wrapper function
       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    """
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)


# decorator version
def wraps(wrapped):
    def wrapper(func):
        for attr in ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'):
            try:
                value = getattr(wrapped, attr)
            except AttributeError:
                pass
            else:
                setattr(func, attr, value)
        func.__dict__.update(getattr(wrapped, attr, {}))
        func.__wrapped__ = wrapped
        return func
    return wrapper


WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)


def wraps(func):
    # double layer decorator for parametrized decorator
    def wrapper(wrapped):
        for attr in WRAPPER_ASSIGNMENTS:
            try:
                value = getattr(wrapped, attr)
            except AttributeError:
                pass
            else:
                setattr(func, attr, value)
        for attr in WRAPPER_UPDATES:
            getattr(wrapped, attr).update(getattr(func, attr, {}))
        wrapped.__wrapped__ = func
        return func
    return wrapper


def identity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wraps func"""
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    @identity
    def return_one():
        """Return one"""
        return 1
    print(return_one())
