import functools
from collections import defaultdict


class FuncAdd:
    fn_list = defaultdict(list)

    def __init__(self, fn):
        self.fn = fn
        FuncAdd.fn_list.append(self.fn)
        functools.update_wrapper(self, fn)

    def __call__(self, *args, **kwargs):

        if self.fn.__name__ not in FuncAdd.fn_list[self.fn.__name__]:
            raise NameError
        else:
            return tuple(sub_fn(*args, **kwargs) for sub_fn in FuncAdd.fn_list[self.fn.__name__])

    @classmethod
    def delete(cls, fn):
        del cls.fn_list[fn.__name__]

    @classmethod
    def clear(cls):
        cls.fn_list = defaultdict(list)


if __name__ == '__main__':
    @FuncAdd
    def foo():
        return 'Hello'

    @FuncAdd
    def foo():
        return 'World'

    @FuncAdd
    def spam():
        return 'Spam'

    assert foo() == ('Hello', 'World')

    FuncAdd.delete(foo)
    print(foo())
