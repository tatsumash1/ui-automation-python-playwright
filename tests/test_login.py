from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://saucedemo.com")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_container")).to_be_visible()