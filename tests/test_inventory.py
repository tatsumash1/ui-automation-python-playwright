from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_add_items_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    inventory_page.add_sauce_labs_backpack()
    # Проверяем, что количество товаров в корзине равно 1
    inventory_page.should_have_cart_count("1")
    # Добавляем второй товар в корзину
    inventory_page.add_sauce_labs_bike_light()
    # Проверяем, что количество товаров в корзине равно 2
    inventory_page.should_have_cart_count("2")

def test_remove_item_from_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товар в корзину
    inventory_page.add_sauce_labs_backpack()
    # Проверяем, что количество товаров в корзине равно 1
    inventory_page.should_have_cart_count("1")
    #Удаляем товар
    inventory_page.remove_sauce_labs_backpack()
    # Проверяем, что количество товаров в корзине равно 0
    inventory_page.should_have_cart_count("0")

def test_sorting_products_lohi(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Сортировка по цене (от низкой к высокой)
    inventory_page.sort_by("lohi")
    # Проверяем, что выбранная сортировка соответствует ожидаемой
    inventory_page.should_have_selected_sorting("lohi")
    # Получаем список цен товаров после сортировки
    prices = inventory_page.get_product_prices()
    # Проверяем, что список цен отсортирован по возрастанию
    assert prices == sorted(prices), "Prices are not sorted from low to high"

def test_sorting_products_hilo(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Сортировка по цене (от высокой к низкой)
    inventory_page.sort_by("hilo")
    # Проверяем, что выбранная сортировка соответствует ожидаемой
    inventory_page.should_have_selected_sorting("hilo")
    # Получаем список цен товаров после сортировки
    prices = inventory_page.get_product_prices()
    # Проверяем, что список цен отсортирован по убыванию
    assert prices == sorted(prices, reverse=True), "Prices are not sorted from high to low"

def test_sorting_products_name_az(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Сортировка по имени (от A до Z)
    inventory_page.sort_by("az")
    # Проверяем, что выбранная сортировка соответствует ожидаемой
    inventory_page.should_have_selected_sorting("az")
    # Получаем список имен товаров после сортировки
    names = inventory_page.get_product_names()
    # Проверяем, что список имен отсортирован по алфавиту
    assert names == sorted(names), "Names are not sorted from A to Z"

def test_sorting_products_name_za(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Сортировка по имени (от Z до A)
    inventory_page.sort_by("za")
    # Проверяем, что выбранная сортировка соответствует ожидаемой
    inventory_page.should_have_selected_sorting("za")
    # Получаем список имен товаров после сортировки
    names = inventory_page.get_product_names()
    # Проверяем, что список имен отсортирован в обратном алфавитном порядке
    assert names == sorted(names, reverse=True), "Names are not sorted from Z to A"

