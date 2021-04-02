import pytest

from .my_greeting import my_greeting

@pytest.fixture(params = [
    ('Fumiyan', 'hello, Fumiyan'),
    ('Kotaroh Saigoh', 'hello, Kotaroh Saigoh'),
    ('Takara Tagawa', 'hello, Takara Tagawa'),
    ('Fumiya Narita', 'hello, Fumiya Narita'),
    ('Hiroto Matsumoto', 'hello, Hiroto Matsumoto'),
    ('Hiroto Inoue', 'hello, Hiroto Inoue'),
    ('Taketo Mikawa', 'hello, Taketo Mikawa'),
    ('Kohshin Yoshida', 'hello, Kohshin Yoshida'),
    ('Shinnya Kawabuchi', 'hello, Shinnya Kawabuchi'),
    ('Taishi Kamimura', 'hello, Taishi Kamimura'),
])
def params(request):
    return request.param

def test_my_greeting(params):
    S, expected = params
    assert my_greeting(S) == expected
