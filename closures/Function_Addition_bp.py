from collections import defaultdict

class FuncAdd:
    # Good Luck!
    funcs = defaultdict(list)

    def __init__(self, func):
        name = func.__name__
        FuncAdd.funcs[name].append(func)
        self.name = name

    def __call__(self, *args, **kwargs):
        vals = []
        if self.name not in FuncAdd.funcs:
            raise NameError()
        for f in FuncAdd.funcs[self.name]:
            vals.append(f(*args, **kwargs))
        return tuple(vals)

    @classmethod
    def delete(cls, self):
        del cls.funcs[self.name]

    @classmethod
    def clear(cls):
        cls.funcs = defaultdict(list)
