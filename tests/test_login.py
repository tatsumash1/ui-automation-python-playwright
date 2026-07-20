from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_unsuccessful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    expect(page.locator(".error-message-container")).to_be_visible()
    expect(page.locator(".error-message-container")).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_blocked_user_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(page.locator(".error-message-container")).to_be_visible()
    expect(page.locator(".error-message-container")).to_have_text("Epic sadface: Sorry, this user has been locked out.")