# language: es
Característica: Cálculo del precio con descuento

  Escenario: Cliente aplica un descuento del 20%
    Dado un producto que cuesta 100
    Cuando aplico un descuento de 20
    Entonces el precio final es 80

  Escenario: Descuento mayor al permitido
    Dado un producto que cuesta 100
    Cuando aplico un descuento de 150
    Entonces el sistema rechaza el descuento
  Escenario: Descuento del 100% deja el producto gratis
    Dado un producto que cuesta 100
    Cuando aplico un descuento de 100
    Entonces el precio final es 0

  Escenario: Precio negativo no es válido
    Dado un producto que cuesta -10
    Cuando aplico un descuento de 20
    Entonces el sistema rechaza el descuento