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
        self.category_locator =                     self.page.locator('[data-parent="#accordian"]')
        self.view_product =                         self.page.locator('[class="nav nav-pills nav-justified"] a').first
        self.review_username =                      self.page.get_by_placeholder("Your Name")
        self.review_email =                         self.page.locator("#email")
        self.review =                               self.page.get_by_placeholder("Add Review Here!")
        self.review_submit_button =                 self.page.locator("#button-review")
        self.review_added_successfully =            self.page.locator('#review-section')


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

    def category(self):
        return self.category_locator.all()

    def click_view_product(self):
        self.view_product.click()

    def add_review(self,username,email,review):
        self.review_username.fill(username)
        self.review_email.fill(email)
        self.review.fill(review)
        self.review_submit_button.click(timeout = 3000)


    def review_success_msg(self):
        return self.review_added_successfully


