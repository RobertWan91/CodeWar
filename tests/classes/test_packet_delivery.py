import pytest
from classes.packet_delivery import Package, DimensionsOutOfBoundError


@pytest.fixture
def args_value_list():
    return [
        [20, 30, 10, 10],
        [0.2, 0.2, 0.2, 0.02],
        [350, 300, 150, 40],
        [99, 99, 99, 40]
    ]


@pytest.fixture
def args_dict():
    return {'value': [0.2, 0.2, 0.2, 0.2],
            'length': 351,
            'width': 310,
            'height': 160,
            'weight': 50}


def test_package_creation(args_value_list):
    for inp in args_value_list:
        p = Package(*inp)
        assert p.length == inp[0]
        assert p.width == inp[1]
        assert p.height == inp[2]
        assert p.weight == inp[3]


def test_assign_invalid_values(args_dict):
    p = Package(*args_dict['value'])
    with pytest.raises(DimensionsOutOfBoundError):
        p.length = args_dict['length']
    with pytest.raises(DimensionsOutOfBoundError):
        p.width = args_dict['width']
    with pytest.raises(DimensionsOutOfBoundError):
        p.height = args_dict['height']
    with pytest.raises(DimensionsOutOfBoundError):
        p.weight = args_dict['weight']

