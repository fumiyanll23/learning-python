import pytest

from .homework import fibonacci

@pytest.fixture(params = [
    (1, 1),
    (2, 1),
    (30, 832040),
    (3, 2),
    (5, 5),
    (10, 55),
    (15, 610),
    (20, 6765),
    (25, 75025),
    (35, 9227465),
])
def params(request):
    return request.param

def test_d_fibonacci(params):
    N, expected = params
    assert fibonacci(N) == expected
