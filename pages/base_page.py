from playwright.sync_api import Page

class BasePage:
    def __init__(self,page):
        self.page =                                            page
        self.signup_login =                                    self.page.locator('[href="/login"]')
        self.product =                                         self.page.locator('[href="/products"]')
        self.cart =                                            self.page.locator('[href="/view_cart"]')
        self.contact_us =                                      self.page.locator('[href="/contact_us"]')

    def click_signup_login(self):
        self.signup_login.click(timeout = 3000)

    def click_product(self):
        self.product.click(timeout = 3000)

    def click_cart(self):
        self.cart.click(timeout = 3000)

    def click_contact(self):
        self.contact_us.click(timeout = 3000)







