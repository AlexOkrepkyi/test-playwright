from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_btn = page.locator("[data-test='login-button']")

    def login_standard_user(self):
        self.username.fill("standard_user")
        self.password.fill("secret_sauce")
        self.login_btn.click()
