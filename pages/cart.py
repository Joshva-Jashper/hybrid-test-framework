from playwright.sync_api import Page

class Cart:
    def __init__(self,page: Page):
        self.page =                         page
        self.check_out_button =             self.page.locator('a:has-text("Proceed To Checkout")')
        self.cart_products    =             self.page.locator('tbody tr')
        self.remove_product_cart =          self.page.locator('[class="cart_quantity_delete"]')

    def click_check_out_button(self):
        self.check_out_button.click()

    def get_products_cart(self):
        return self.cart_products.all()

    def get_remove_product(self):
        return self.remove_product_cart.all()


