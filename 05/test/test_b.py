import pytest

from .homework import average

@pytest.fixture(params = [
    ([1, 2, 3, 4, 5], 3.0),
    ([11, 7, 1, -23, -49, 100, 4, 21, -99, 3], -2.4),
    ([10, -9, 8, -7, 6, -5, 4, -3, 2, -1], 0.5),
    ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -5.5),
    ([69, 61, 74, 6, 96, 53, 5, 48, 24, 73, 78, 67, 13, 46, 15, 81, 83, 5, 12, 71], 49.0),
])
def params(request):
    return request.param

def test_b(params):
    As, expected = params
    assert average(As) == expected
