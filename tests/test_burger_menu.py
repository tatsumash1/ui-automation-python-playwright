from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_burger_menu_navigation(products_page):
    inventory_page = InventoryPage(products_page)
    # Кликаем на кнопку бургер-меню
    inventory_page.click_burger_menu()
    # Проверяем, что меню открыто
    expect(products_page.locator(".bm-menu-wrap")).to_be_visible()
    # Кликаем на кнопку бургер-меню
    inventory_page.click_burger_menu()