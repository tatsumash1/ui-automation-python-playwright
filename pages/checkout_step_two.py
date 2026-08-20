class Checkout_step_two:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")
        self.invenory_items = page.locator("#inventory_item")
        self.total_price = page.locator("#total_label")
    
    def click_finish(self):
        self.page.locator("#finish").click