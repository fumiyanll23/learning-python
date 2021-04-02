import pytest

from .my_factorial import my_factorial

@pytest.fixture(params = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
])
def params(request):
    return request.param

def test_my_greeting(params):
    N, expected = params
    assert my_factorial(N) == expected
