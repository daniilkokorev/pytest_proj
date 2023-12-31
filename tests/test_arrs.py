import pytest

from utils import arrs


@pytest.fixture
def num_list():
    return [1, 2, 3, 4]


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_slice_coll_zero():
    assert arrs.my_slice([]) == []


def test_slice_start_zero(num_list):
    assert arrs.my_slice(num_list) == [1, 2, 3, 4]
