import pytest

from .homework import bubble_sort

@pytest.fixture(params = [
    ([3, 5, 1, 4, 2], [1, 2, 3, 4, 5]),
    ([-3, -5, -2, 7, 6, -4, 10, 9, -1, 8], [-5, -4, -3, -2, -1, 6, 7, 8, 9, 10]),
])
def params(request):
    return request.param

def test_a_greeting(params):
    As, expected = params
    assert bubble_sort(As) == expected
