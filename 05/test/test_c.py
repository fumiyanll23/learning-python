import pytest

from .homework import my_max

@pytest.fixture(params = [
    ([1, 2, 3, 4, 5], 5),
    ([3, -5, -2, 7, -6, 4, 10, -9, 1, 8], 10),
    ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -1),
])
def params(request):
    return request.param

def test_c(params):
    As, expected = params
    assert my_max(As) == expected
