from pages.checkout_step_one import CheckoutStepOne
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

def test_open_checkout_one_page(page):
    test_login(page)
    inventory_page = InventoryPage(page)
    inventory_page.open_cart()
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
def test_checkout_one_page_input(page):
    test_open_checkout_one_page(page)
    checkout_step_one = CheckoutStepOne(page)
    checkout_step_one.information_input()
    checkout_step_one.click_continue()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
