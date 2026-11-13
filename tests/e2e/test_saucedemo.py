from playwright.sync_api import Page, expect

URL = 'https://www.saucedemo.com'


def login(page: Page, usuario='standard_user', clave='secret_sauce'):
    page.goto(URL)
    page.fill('#user-name', usuario)
    page.fill('#password', clave)
    page.click('#login-button')


def test_login_exitoso(page: Page):
    login(page)
    expect(page).to_have_url(f'{URL}/inventory.html')


def test_login_con_clave_incorrecta(page: Page):
    login(page, clave='incorrecta')
    expect(page.locator('[data-test=error]')).to_contain_text('do not match')


def test_agregar_producto_al_carrito(page: Page):
    login(page)
    page.click('#add-to-cart-sauce-labs-backpack')
    expect(page.locator('.shopping_cart_badge')).to_have_text('1')
def test_flujo_completo_de_compra(page: Page):
    login(page)
    page.click('#add-to-cart-sauce-labs-backpack')
    page.click('.shopping_cart_link')
    expect(page).to_have_url(f'{URL}/cart.html')
    page.click('#checkout')
    page.fill('#first-name', 'Ana')
    page.fill('#last-name', 'Perez')
    page.fill('#postal-code', '110111')
    page.click('#continue')
    page.click('#finish')
    expect(page.locator('.complete-header')).to_have_text('Thank you for your order!')
def test_login_usuario_bloqueado(page: Page):
    login(page, usuario='locked_out_user')
    expect(page.locator('[data-test=error]')).to_contain_text('locked out')