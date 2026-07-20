class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_list = page.locator("div.cart_list")
        self.remove_sauce_labs_backpack_button = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.checkout_button_selector = "[data-test='checkout']"
        self.continue_shopping_button_selector = "[data-test='continue-shopping']"
        self.burger_menu_button_selector = page.locator("#react-burger-menu-btn")
        self.cart_button_selector = page.locator("[data-test='shopping-cart-link']")

    def remove_sauce_labs_backpack(self):
        self.remove_sauce_labs_backpack_button.click()

    def click_checkout(self):
        self.page.locator(self.checkout_button_selector).click()

    def click_continue_shopping(self):
        self.page.locator(self.continue_shopping_button_selector).click()
    
    def click_burger_menu(self):
        self.burger_menu_button_selector.click()

    def click_cart_button(self):
        self.cart_button_selector.click()
    