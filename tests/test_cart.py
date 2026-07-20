from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

def test_add_to_cart_and_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Логин
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем два товара в корзину
    inventory_page.add_sauce_labs_backpack()
    inventory_page.add_sauce_labs_bike_light()

    # Проверяем, что количество товаров в корзине равно 2
    inventory_page.should_have_cart_count("2")

    # Переходим на страницу корзины
    cart_page.click_cart_button()

    # Удаляем один товар из корзины
    cart_page.remove_sauce_labs_backpack()

    # Проверяем, что количество товаров в корзине равно 1
    inventory_page.should_have_cart_count("1")

    # Кликаем на кнопку checkout
    cart_page.click_checkout()

    # Проверяем, что мы находимся на странице checkout
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

def test_continue_shopping(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Логин
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем один товар в корзину
    inventory_page.add_sauce_labs_backpack()

    # Переходим на страницу корзины
    page.goto("https://www.saucedemo.com/cart.html")

    # Кликаем на кнопку continue shopping
    cart_page.click_continue_shopping()

    # Проверяем, что мы находимся на странице инвентаря
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_burger_menu_navigation(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Логин
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Переходим на страницу корзины
    page.goto("https://www.saucedemo.com/cart.html")

    # Кликаем на кнопку бургер-меню
    cart_page.click_burger_menu()

    # Проверяем, что меню открыто
    expect(page.locator(".bm-menu-wrap")).to_be_visible()

