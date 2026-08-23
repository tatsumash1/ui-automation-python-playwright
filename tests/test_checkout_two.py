from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import Checkout_step_two
from pages.inventory_page import InventoryPage


def open_checkout_step_two(products_page):
    inventory_page = InventoryPage(products_page)
    inventory_page.add_sauce_labs_backpack()
    inventory_page.open_cart()

    cart_page = CartPage(products_page)
    cart_page.click_checkout()

    checkout_step_one = CheckoutStepOne(products_page)
    checkout_step_one.information_input()
    checkout_step_one.click_continue()

    expect(products_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    return Checkout_step_two(products_page)


def test_finish_button(products_page):
    checkout_step_two = open_checkout_step_two(products_page)

    checkout_step_two.click_finish()

    expect(checkout_step_two.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")


def test_cancel_button(products_page):
    checkout_step_two = open_checkout_step_two(products_page)

    checkout_step_two.click_cancel()

    expect(checkout_step_two.page).to_have_url("https://www.saucedemo.com/inventory.html")
