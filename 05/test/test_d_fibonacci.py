import pytest

from .homework import fibonacci

@pytest.fixture(params = [
    (1, 1),
    (2, 1),
    (30, 832040),
])
def params(request):
    return request.param

def test_d_fibonacci(params):
    N, expected = params
    assert fibonacci(N) == expected
