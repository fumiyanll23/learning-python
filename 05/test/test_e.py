import pytest

from .homework import gcd

@pytest.fixture(params = [
    ([12, 30], 6),
    ([252, 105], 21),
])
def params(request):
    return request.param

def test_a_greeting(params):
    As, expected = params
    assert gcd(As) == expected
