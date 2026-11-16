def calcular_precio_final(precio, porcentaje_descuento):
    if precio < 0:
        raise ValueError('El precio no puede ser negativo')
    if not 0 <= porcentaje_descuento <= 100:
        raise ValueError('El descuento debe estar entre 0 y 100')
    return round(precio * (1 - porcentaje_descuento / 100), 2)