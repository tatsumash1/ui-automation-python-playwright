from pages.checkout_step_one import CheckoutStepOne
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_open_checkout_one_page(products_page):
    # Переходим на страницу корзины
    cart_page = CartPage(products_page)
    cart_page.click_cart_button()
    # Кликаем на кнопку checkout
    cart_page.click_checkout()
    # Проверяем, что мы находимся на странице checkout
    expect(products_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    
def test_checkout_one_page_input(products_page):
    # Переходим на страницу checkout
    test_open_checkout_one_page(products_page)
    checkout_step_one = CheckoutStepOne(products_page)
    # Вводим данные
    checkout_step_one.information_input()
    # Кликаем на кнопку continue
    checkout_step_one.click_continue()
    # Проверяем, что мы находимся на странице checkout
    expect(products_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
