from playwright.sync_api import Page

class BasePage:
    def __init__(self,page):
        self.page =                                            page
        self.signup_login =                                    self.page.locator('[href="/login"]')
        self.product =                                         self.page.locator('[href="/products"]')
        self.cart =                                            self.page.get_by_role("link",name="Cart")
        self.contact_us =                                      self.page.locator('[href="/contact_us"]')

    def click_signup_login(self):
        self.signup_login.click()

    def click_product(self):
        self.product.click()

    def click_cart(self):
        self.cart.click()

    def click_contact(self):
        self.contact_us.click()







