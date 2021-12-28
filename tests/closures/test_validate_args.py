import pytest
from closures.validate_args import validate_args, InvalidArgument


@validate_args(str)
def hello_world(input_string):
    return 'Hello ' + input_string


@validate_args(str, int)
def hello_multiple(input_str, input_int):
    return 'Hello ' + input_str * input_int


def test_single_validate_args():
    assert hello_world('world') == 'Hello world'


def test_invalid_single_validate_args():
    with pytest.raises(InvalidArgument):
        hello_world(1)


def test_multiple_validate_args():
    assert hello_multiple('world', 2) == 'Hello worldworld'


def test_invalid_multiple_validate_args():
    with pytest.raises(InvalidArgument):
        hello_multiple(1, 2)

