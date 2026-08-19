from playwright.sync_api import Page,expect

class Cart:
    def __init__(self,page: Page):
        self.page =                         page
        self.check_out_button =             self.page.locator('a:has-text("Proceed To Checkout")')
        self.cart_products    =             self.page.locator('tbody tr')
        self.remove_product_cart =          self.page.locator('[class="cart_quantity_delete"]')
        self.checkout =                     self.page.get_by_text("Proceed To Checkout")
        self.checkout_price =               self.page.locator('[class="cart_total_price"]')

    def click_check_out_button(self):
        self.check_out_button.click()

    def get_products_cart(self):
        return self.cart_products.all()

    def get_remove_product(self):
        return self.remove_product_cart.all()

    def get_remove_product_locator(self):
        return self.remove_product_cart

    def get_product_price(self):
        return self.product_price

    def get_product_quantity(self):
        return self.product_quantity

    def get_total_product(self):
        return self.product_total_price

    def calculate_total_price(self,product):
        product_price = product.locator('[class="cart_price"]').inner_text()
        product_quantity = product.locator('[class="cart_quantity"]').inner_text()
        product_total_price = product.locator('[class="cart_total"]').inner_text()

        price = int(product_price.replace("Rs.","").strip())
        quantity = int(product_quantity.strip())
        total_price = int(product_total_price.replace("Rs."," ").strip())
        assert price*quantity == total_price

        return total_price

    def get_checkout(self):
        self.checkout.click()

    def get_checkout_price(self):
        checkout_price = self.checkout_price.last.inner_text()
        return int(checkout_price.replace("Rs."," ").strip())    

