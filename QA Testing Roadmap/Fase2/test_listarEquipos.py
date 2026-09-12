import httpx

BASE_URL = "http://127.0.0.1:8000"

def test_listar_equipos_status_200():
    respuesta = httpx.get(f"{BASE_URL}/equipos")
    assert respuesta.status_code == 200

def test_listar_equipos_es_lista():
    respuesta = httpx.get(f"{BASE_URL}/equipos")
    datos = respuesta.json()
    assert isinstance(datos, list)

def test_equipos_tienen_campos_esperados():
    respuesta = httpx.get(f"{BASE_URL}/equipos")
    datos = respuesta.json()
    primer_equipo = datos[0]
    assert "id" in primer_equipo
    assert "nombre" in primer_equipo
    assert "ip" in primer_equipo
    assert "activo" in primer_equipo