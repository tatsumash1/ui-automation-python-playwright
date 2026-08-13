import pytest

#Логин
@pytest.fixture(scope="function")
def logged_in_page_valid(page):
    page.goto("https://saucedemo.com/")
    page.locator("#username").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    return page

@pytest.fixture(scope="function")
def logged_in_page_invalid(page):
    page.goto("https://saucedemo.com/")
    page.locator("#username").fill("problem_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    return page

@pytest.fixture(scope="function")
def logged_in_page_blocked(page):
    page.goto("https://saucedemo.com/")
    page.locator("#username").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    return page

# Переход на страницу продуктов (связанная с фикстурой logged_in_page)
@pytest.fixture(scope="function")
def products_page(logged_in_page):
    page = logged_in_page

    assert page.locator(".inventory_list").is_visible(), "PRODUCTS PAGE NOT VISIBLE"

    return page

#Очистка корзины (связанная с фикстурой products_page)
@pytest.fixture
def clean_cart(products_page):

    page = products_page

    page.locator(".add-to-cart-sauce-labs-backpack").click()

    assert page.locator(".shopping_cart_badge") .text_content() == "1", "CART IS NOT UPDATED"

    yield products_page

    remove_buttons = page.locator('[data-test^="remove-"]')

    for i in range(remove_buttons.count()):
        remove_buttons.nth(0).click()

        
