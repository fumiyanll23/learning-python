import pytest

from .homework import greeting

@pytest.fixture(params = [
    ('world', 'hello, world'),
    ('Fumiyan', 'hello, Fumiyan'),
    ('Kotaroh Saigoh', 'hello, Kotaroh Saigoh'),
    ('Takara Tagawa', 'hello, Takara Tagawa'),
    ('Hiroto Matsumoto', 'hello, Hiroto Matsumoto'),
    ('Hiroto Inoue', 'hello, Hiroto Inoue'),
    ('Taketo Mikawa', 'hello, Taketo Mikawa'),
    ('Kohshin Yoshida', 'hello, Kohshin Yoshida'),
    ('Shinnya Kawabuchi', 'hello, Shinnya Kawabuchi'),
    ('Taishi Kamimura', 'hello, Taishi Kamimura'),
])
def params(request):
    return request.param

def test_a_greeting(params):
    S, expected = params
    assert greeting(S) == expected
