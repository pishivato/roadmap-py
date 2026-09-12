

def sumar(a,b):
    return a+b

def test_sumar_positivos():
    assert sumar(2,3) == 5

def test_sumar_negativos():
    assert sumar(-1,-1) == -2

def test_sumar_falla():
    assert sumar(2,2) == 5