from playwright.sync_api import Page, locator, has_text

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")

    def get_product_container(self, product_name: str)-> locator: 
        """Фильтрация картрочек по нужному имени"""
        return self.inventory_items.filter(has_text(product_name))

    def open_product_details(self, product_name: str):
        """Открытие карточки товара путем нажатия на название"""
        container = self.get_product_container(product_name)
        container.locator(".inventory_item_name").click()

    def add_to_cart(self, product_name: str):
        """Добавление конкретного товара в корзину"""
        container = self.get_product_container(product_name)
        container.locator(".add-to-cart").click()

    def get_product_price(self, product_name: str):
        """Получение цены конкретного товара"""
        container = self.get_product_container(product_name)
        price_text = container.locator(".inventory_item_price").text_content()
        return price_text

    

    