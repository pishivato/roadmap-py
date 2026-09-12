import pytest

def sumar(a,b):
    return a+b

@pytest.mark.parametrize("a, b, resultado_esperado", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (10, -5, 5),
])
def test_sumar_parametrizado(a, b, resultado_esperado):
    assert sumar(a, b) == resultado_esperado