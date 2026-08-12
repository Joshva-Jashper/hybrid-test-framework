class ProductsPage:
    def __init__(self,page):
        self.page =                                 page
        self.product_search =                       self.page.locator("#search_product")
        self.product_list =                         self.page.locator('[class="title text-center"]')
        self.individual_product =                   self.page.locator('[class="col-sm-4"]')
        self.product_search_click =                 self.page.locator("#submit_search")
        self.add_to_cart =                          self.page.get_by_text("Add to cart").first
        self.product_added_successfully =           self.page.locator('[class="text-center"]')
        self.continue_button =                      self.page.get_by_role("button", name="Continue Shopping")

    def product_search_fill(self,product_name):
        self.product_search.fill(product_name)
        self.product_search_click.click()

        products = self.individual_product.all()
        return len(products)


    def add_to_cart_button(self):
        return self.add_to_cart

    def product_added(self):
        return self.product_added_successfully.first

    def product_list_exists(self):
        return self.product_list

    def click_continue_shopping(self):
        self.continue_button.click()






