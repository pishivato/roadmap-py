import pytest

@pytest.fixture
def lista_usuarios():
    return ["ana", "beto", "carla"]

def test_cantidad_usuarios(lista_usuarios):
    assert len(lista_usuarios) == 3

def test_primer_usuario(lista_usuarios):
    assert lista_usuarios[0] == "ana"