from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_successful_login(logged_in_page_valid):
    expect(logged_in_page_valid).to_have_url("https://www.saucedemo.com/inventory.html")

def test_unsuccessful_login(logged_in_page_invalid):
    expect(logged_in_page_invalid.locator(".error-message-container")).to_be_visible()
    expect(logged_in_page_invalid.locator(".error-message-container")).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_blocked_user_login(logged_in_page_blocked):
    expect(logged_in_page_blocked.locator(".error-message-container")).to_be_visible()
    expect(logged_in_page_blocked.locator(".error-message-container")).to_have_text("Epic sadface: Sorry, this user has been locked out.")