class ProductsPage:
    def __init__(self,page):
        self.page =                  page
        self.product_search =        self.page.locator("#search_product")
        self.product_list =          self.page.locator('[class="title text-center"]')
        self.individual_product =    self.page.locator('[class="col-sm-4"]')
        self.product_search_click =  self.page.locator("#submit_search")

    def product_search_fill(self,product_name):
        self.product_search.fill(product_name)
        self.product_search_click.click()

        products = self.individual_product.all()
        return len(products)


    def product_list_exists(self):
        return self.product_list




