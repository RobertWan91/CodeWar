import functools
class FuncAdd:
    fn_list = {}

    def __init__(self, fn):
        self.fn = fn

        if self.fn.__name__ not in FuncAdd.fn_list:
            FuncAdd.fn_list[self.fn.__name__] = [self.fn]
        else:
            FuncAdd.fn_list[self.fn.__name__].append(self.fn)
        functools.update_wrapper(self, fn)

    def __call__(self, *args, **kwargs):

        if FuncAdd.fn_list[self.fn.__name__] is None:
            raise NameError
        else:
            return tuple(sub_fn(*args, **kwargs) for sub_fn in FuncAdd.fn_list[self.fn.__name__])

    @classmethod
    def delete(cls, fn):
        cls.fn_list[fn.__name__] = None

    @classmethod
    def clear(cls):
        for key, value in cls.fn_list.items():
            cls.fn_list[key] = None


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
