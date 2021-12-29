import pytest
from classes.function_addition import FuncAdd

@FuncAdd
def foo():
    return 'Hello'

@FuncAdd
def foo():
    return 'World'

@FuncAdd
def spam():
    return 'Spam'


def test_func_add():
    assert foo() == ('Hello', 'World')


def test_func_delete():
    FuncAdd.delete(foo)
    with pytest.raises(NameError):
        foo()

    assert spam() == ('Spam', )


def test_func_clear():
    FuncAdd.clear()
    with pytest.raises(NameError):
        foo()
    with pytest.raises(NameError):
        spam()
