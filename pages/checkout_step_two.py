from playwright.sync_api import expect
class Checkout_step_two:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")
        self.invenory_items = page.locator("#inventory_item")
        self.inventory_item_name = page.locator(".inventory_item_name")
        self.inventory_item_price = page.locator(".inventory_item_price")
        self.total_price = page.locator("#total_label")
    
    def click_finish(self):
        self.finish_button.click
    
    def click_cancel(self):
        self.cancel_button.click

    def inventory_item_click(self):
        self.inventory_item_name.click()
        expected_url = "https://www.saucedemo.com/inventory-item.html?id=\d+"
        expect(self.page).to_have_url(expected_url)

    def check_total_price(self, expected_total):
        expect(self.total_price).to_have_text(f"Total: ${expected_total}")

    def sum_inventory_item_prices(self):
        prices = self.inventory_item_price.all_inner_texts()
        expected_total = sum(float(price.replace("$", "")) for price in prices)
        return expected_total
