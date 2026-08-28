from playwright.sync_api import Locator

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.shopping_cart_button = page.locator("[data-test='shopping_cart_link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def get_product_container(self, product_name: str)-> Locator: 
        """Фильтрация картрочек по нужному имени"""
        return self.inventory_items.filter(
            has = self.page.get_by_text(product_name, exact=True)
        )

    def open_product_details(self, product_name: str):
        """Открытие карточки товара путем нажатия на название"""
        container = self.get_product_container(product_name)
        container.locator(".inventory_item_name").click()

    def add_to_cart(self, product_name: str):
        """Добавление конкретного товара в корзину"""
        container = self.get_product_container(product_name)
        container.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name: str):
        """Удаление конкретного товара из корзины (сброс состояния)"""
        container = self.get_product_container(product_name)
        container.get_by_role("button", name="Remove").click()

    def get_product_price(self, product_name: str):
        """Получение цены конкретного товара"""
        container = self.get_product_container(product_name)
        price_text = container.locator(".inventory_item_price").inner_text()
        return price_text

    

    