import pytest

from .homework import average

@pytest.fixture(params = [
    ([1, 2, 3, 4, 5], 3.0),
    ([11, 7, 1, -23, -49, 100, 4, 21, -99, 3], -2.4)
])
def params(request):
    return request.param

def test_a_greeting(params):
    As, expected = params
    assert average(As) == expected
