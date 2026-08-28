from pages.product_page import ProductPage
from playwright.sync_api import expect
import pytest


PRODUCTS_DATA=[
    {"name": "Sauce Labs Backpack", "price": "29.99"},
    {"name": "Sauce Labs Bike Light", "price": "9.99"},
    {"name": "Sauce Labs Bolt T-Shirt", "price": "15.99"},
    {"name": "Sauce Labs Fleece Jacket", "price": "49.99"},
    {"name": "Sauce Labs Onesie", "price": "7.99"},
    {"name": "Test.allTheTheThings() T-Shirt (Red)", "price": "15.99"}
]

@pytest.mark.parametrize(
        "product", 
        PRODUCTS_DATA, 
        ids=lambda product: product["name"]
)
def test_product_card(logged_in_page_valid, product):
    product_page = ProductPage(logged_in_page_valid)

    actual_price = product_page.get_product_price(
        product["name"]
    ).strip("$")

    assert actual_price == product["price"], f"Ожидаемая цена {product['price']}, фактическая {actual_price}"

    product_page.add_to_cart(product["name"])

    expect(product_page.cart_badge).to_have_text("1")

    product_page.remove_from_cart(product["name"])

    expect(product_page.cart_badge).to_be_hidden()
