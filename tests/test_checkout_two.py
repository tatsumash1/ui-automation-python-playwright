from pages.checkout_step_two import Checkout_step_two
from playwright.sync_api import expect

def click_finish_button(checkout_step_two):
    checkout_step_two.click_finish()
    excepted_url = "https://www.saucedemo.com/checkout-complete.html"
    expect(checkout_step_two.page).to_have_url(excepted_url)

def click_cancel_button(checkout_step_two):
    checkout_step_two.click_cancel()
    excepted_url = "https://www.saucedemo.com/cart.html"
    expect(checkout_step_two.page).to_have_url(excepted_url)