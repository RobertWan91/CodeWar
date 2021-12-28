from closures.lazy_executing import make_lazy
import pytest


def test_add_make_lazy():
    def add(a, b):
        return a+b

    add = make_lazy(add, 1, 2)
    assert add() == 3


def test_mod_make_lazy():
    def mod(a, b):
        return a % b

    mod = make_lazy(mod, 5, 3)
    assert mod() == 2
