from playwright.sync_api import Locator

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.add_to_cart_button = page.locator("button[id^='add-to-cart']")
        self.remove_button = page.locator("button[id^='remove']")
        self.shopping_cart_button = page.locator("[data-test='shopping_cart_link']")
        self.cart_badge = page.locator("[data-test='shopping_cart_badge']")
        self.inventory_item_name = page.locator(".inventory_item_name")
        self.inventory_item_price = page.locator(".inventory_item_price")

    def get_product_container(self, product_name: str)-> Locator: 
        """Фильтрация картрочек по нужному имени"""
        return self.inventory_items.filter(has_text =product_name)

    def open_product_details(self, product_name: str):
        """Открытие карточки товара путем нажатия на название"""
        container = self.get_product_container(product_name)
        container.locator(self.inventory_item_name).click()

    def add_to_cart(self, product_name: str):
        """Добавление конкретного товара в корзину"""
        container = self.get_product_container(product_name)
        container.locator(self.add_to_cart_button).click()

    def remove_from_cart(self, product_name: str):
        """Удаление конкретного товара из корзины (сброс состояния)"""
        container = self.get_product_container(product_name)
        container.locator(self.remove_button).click()

    def get_product_price(self, product_name: str):
        """Получение цены конкретного товара"""
        container = self.get_product_container(product_name)
        price_text = container.locator(self.inventory_item_price).inner_text()
        return price_text

    

    