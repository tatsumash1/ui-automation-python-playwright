from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart_and_checkout(products_page):
    inventory_page = InventoryPage(products_page)

    # Добавляем два товара в корзину
    inventory_page.add_sauce_labs_backpack()
    inventory_page.add_sauce_labs_bike_light()

    # Проверяем, что количество товаров в корзине равно 2
    inventory_page.should_have_cart_count("2")

    # Переходим на страницу корзины
    cart_page = CartPage(products_page)
    cart_page.click_cart_button()

    # Удаляем один товар из корзины
    cart_page.remove_sauce_labs_backpack()

    # Проверяем, что количество товаров в корзине равно 1
    inventory_page.should_have_cart_count("1")

    # Кликаем на кнопку checkout
    cart_page.click_checkout()

    # Проверяем, что мы находимся на странице checkout
    expect(products_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

def test_continue_shopping(products_page):
    inventory_page = InventoryPage(products_page)
    cart_page = CartPage(products_page)

    # Добавляем один товар в корзину
    inventory_page.add_sauce_labs_backpack()

    # Переходим на страницу корзины
    cart_page.click_cart_button()

    # Кликаем на кнопку continue shopping
    cart_page.click_continue_shopping()

    # Проверяем, что мы находимся на странице инвентаря
    expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_burger_menu_navigation(products_page):
    cart_page = CartPage(products_page)

    # Переходим на страницу корзины
    cart_page.click_cart_button()

    # Кликаем на кнопку бургер-меню
    cart_page.click_burger_menu()

    # Проверяем, что меню открыто
    expect(products_page.locator(".bm-menu-wrap")).to_be_visible()

    # Кликаем на кнопку бургер-меню
    cart_page.click_burger_menu()

    # Проверяем, что меню закрыто
    expect(products_page.locator(".bm-menu-wrap")).not_to_be_visible()