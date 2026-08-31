from playwright.sync_api import Page,expect

class Payment:
    def __init__(self,page):
        self.page = page
        self.card_name =                   self.page.locator('[name="name_on_card"]')
        self.card_number =                 self.page.locator('[name="card_number"]')
        self.cvc_number =                  self.page.locator('[name="cvc"]')
        self.expiry_month =                self.page.locator('[name="expiry_month"]')
        self.expiry_year =                 self.page.locator('[name="expiry_year"]')
        self.place_order =                 self.page.locator("#submit")
        self.order_confirmation_msg =      self.page.get_by_text("Congratulations! Your order has been confirmed!")
        self.continue_btn =                self.page.get_by_text("Continue")
        


    def fill_payment_details(self,card_name,card_number,cvc,expiry_month,expiry_year):
        self.card_name.fill(card_name)
        self.card_number.fill(card_number)
        self.cvc_number.fill(cvc)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year)
        self.place_order.click()    


    def get_confirmation_msg(self):
        return self.order_confirmation_msg     

    def click_continue_btn(self):
        self.continue_btn.click()