from playwright.sync_api import expect, Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.product_name = page.locator("[data-test='inventory-item-name']")
        self.product_price = page.locator("[data-test='inventory-item-price']")
        self.add_to_cart_sauce_labs_backpack_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_sauce_labs_backpack_button = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.add_to_cart_sauce_labs_bike_light_button = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")

    def add_sauce_labs_backpack(self):
        self.add_to_cart_sauce_labs_backpack_button.click()

    def add_sauce_labs_bike_light(self):
        self.add_to_cart_sauce_labs_bike_light_button.click()

    def remove_sauce_labs_backpack(self):
        self.remove_sauce_labs_backpack_button.click()
    
    def should_have_cart_count(self, count: str):
        if count == "0":
            expect(self.cart_badge).to_have_count(0)
        else:
            expect(self.cart_badge).to_have_text(count)

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)
    
    def get_product_names(self):
        return self.product_name.all_inner_texts()
    
    def get_product_prices(self):
        prices = self.product_price.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]
    
    def should_have_selected_sorting(self, value: str):
        expect(self.sort_dropdown).to_have_value(value)
