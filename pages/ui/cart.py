from playwright.sync_api import Page,expect

class Cart:
    def __init__(self,page: Page):
        self.page =                         page
        self.check_out_button =             self.page.locator('a:has-text("Proceed To Checkout")')
        self.cart_products    =             self.page.locator('tbody tr')
        self.remove_product_cart =          self.page.locator('[class="cart_quantity_delete"]')
        self.checkout =                     self.page.get_by_text("Proceed To Checkout")
        self.checkout_price =               self.page.locator('[class="cart_total_price"]')
        self.deleivery_details_title =      self.page.locator('#address_delivery li:nth-child(1)')
        self.delivery_details_name =        self.page.locator('#address_delivery li:nth-child(2)')
        self.billing_address_title =        self.page.locator('#address_invoice li:nth-child(1)')
        self.billing_address_name =         self.page.locator('#address_invoice li:nth-child(2)')
        self.comment_box =                  self.page.locator('[class="form-control"]')
        self.place_order =                  self.page.get_by_text("Place Order")
        self.checkout_without_login =       self.page.get_by_text("Register / Login account to proceed on checkout.")
        self.continue_to_cart =             self.page.get_by_role("button",name ="Continue On Cart",exact = True)


        

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

    def get_product_total_price(self,product):
        product_total_price = product.locator('[class="cart_total"]').inner_text()
        total_price = int(product_total_price.replace("Rs."," ").strip())
        return total_price

    def get_delivery_address_title(self):
        return self.deleivery_details_title

    def get_delivery_name(self):
        return self.delivery_details_name

    def get_billing_title(self):
        return self.billing_address_title

    def get_billing_name(self):
        return self.billing_address_name

    def get_comment_box(self,message):
        self.comment_box.fill(message)

    def click_palce_order(self):
        self.place_order.click()    

    def get_checkout_without_login_msg(self):
        return self.checkout_without_login    

    def click_continue_to_cart_btn(self):
        self.continue_to_cart.click()
        
        



    



