import pytest
from app.descuentos import calcular_precio_final


@pytest.mark.parametrize('precio, descuento, esperado', [
    (100, 0, 100),
    (200, 25, 150),
    (50, 100, 0),
    (0, 30, 0),
    (80, 50, 40),
])
def test_precio_final(precio, descuento, esperado):
    assert calcular_precio_final(precio, descuento) == esperado


def test_precio_negativo():
    with pytest.raises(ValueError):
        calcular_precio_final(-1, 10)


@pytest.mark.parametrize('descuento', [-5, 101])
def test_descuento_fuera_de_rango(descuento):
    with pytest.raises(ValueError):
        calcular_precio_final(100, descuento)