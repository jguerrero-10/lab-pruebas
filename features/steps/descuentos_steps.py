from behave import given, when, then
from app.descuentos import calcular_precio_final


@given('un producto que cuesta {precio:g}')
def step_precio(context, precio):
    context.precio = precio


@when('aplico un descuento de {descuento:g}')
def step_descuento(context, descuento):
    context.error = None
    try:
        context.resultado = calcular_precio_final(context.precio, descuento)
    except ValueError as e:
        context.error = e


@then('el precio final es {esperado:g}')
def step_resultado(context, esperado):
    assert context.resultado == esperado


@then('el sistema rechaza el descuento')
def step_rechazo(context):
    assert context.error is not None