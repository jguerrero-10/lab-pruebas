import pytest
from app.api import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(str(tmp_path / 'test.db'))
    return app.test_client()


def crear(client, nombre='Cuaderno', precio=20):
    return client.post('/productos', json={'nombre': nombre, 'precio': precio})


def test_crear_y_calcular_precio(client):
    r = crear(client)
    assert r.status_code == 201
    pid = r.get_json()['id']
    r2 = client.get(f'/productos/{pid}/precio-final?descuento=10')
    assert r2.status_code == 200
    assert r2.get_json()['precio_final'] == 18


def test_producto_inexistente(client):
    assert client.get('/productos/999/precio-final').status_code == 404


def test_precio_negativo_rechazado(client):
    assert crear(client, precio=-5).status_code == 400


def test_descuento_invalido(client):
    pid = crear(client).get_json()['id']
    r = client.get(f'/productos/{pid}/precio-final?descuento=150')
    assert r.status_code == 400