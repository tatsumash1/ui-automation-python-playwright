from playwright.sync_api import Page, locator, has_text

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")

    def get_product_container(self, product_name: str)-> locator: 
        """Фильтрация картрочек по нужному имени"""
        return self.inventory_items.filter(has_text(product_name))

    #def open_product_details(self, product_name: str):

    

    