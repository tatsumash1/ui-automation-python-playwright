class CheckoutStepOne:
    def __init__(self, page):
        self.page = page
        self.firstname_input = page.locator("[data-test='firstName']")
        self.lastname_input = page.locator("[data-test='lastName']")
        self.postalcode_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")

    def information_input(self):
        self.firstname_input.fill("John")
        self.lastname_input.fill("Doe")
        self.postalcode_input.fill("12345")

    def click_continue(self):
        self.continue_button.click()

    def click_cancel(self):
        self.cancel_button.click()
