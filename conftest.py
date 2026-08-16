import pytest


BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"


def login(page, username, password=PASSWORD):
    page.goto(BASE_URL)
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()


@pytest.fixture(scope="function")
def logged_in_page_valid(page):
    login(page, "standard_user")
    return page


@pytest.fixture(scope="function")
def logged_in_page_invalid(page):
    login(page, "invalid_user", "invalid_password")
    return page


@pytest.fixture(scope="function")
def logged_in_page_blocked(page):
    login(page, "locked_out_user")
    return page


@pytest.fixture(scope="function")
def products_page(logged_in_page_valid):
    page = logged_in_page_valid
    assert page.locator(".inventory_list").is_visible(), "PRODUCTS PAGE NOT VISIBLE"
    return page


@pytest.fixture
def clean_cart(products_page):
    page = products_page
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    assert page.locator("[data-test='shopping-cart-badge']").text_content() == "1", "CART IS NOT UPDATED"

    yield page

    remove_buttons = page.locator('[data-test^="remove-"]')
    for _ in range(remove_buttons.count()):
        remove_buttons.nth(0).click()
