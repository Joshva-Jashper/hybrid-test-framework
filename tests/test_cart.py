from playwright.sync_api import expect
import pytest
from pages.base_page import BasePage
from pages.products import ProductsPage
from pages.login_signup_page import LoginSignupPage
from pages.cart import Cart

@pytest.mark.ui
@pytest.mark.smoke
def test_product_cart_with_one_product(page):
    cart_page = Cart(page)
    base_page = BasePage(page)
    product_page = ProductsPage(page)
    # base_page.click_signup_login()
    # login_page = LoginSignupPage(page)
    # base_page.click_signup_login()
    # login_page.login("jane.doe.qa01@xample.com", "SecurePass@123")

    base_page.click_product()
    product_page.product_search_fill("top")
    product = product_page.add_to_cart_button()
    product.wait_for(state="visible")
    product.scroll_into_view_if_needed()
    product.hover(force=True)
    product.click(force=True)
    expect(product_page.product_added()).to_be_visible()
    product_page.click_continue_shopping()

    base_page.click_cart()
    products = cart_page.get_products_cart()
    
    assert len(products) == 1
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()


@pytest.mark.ui
@pytest.mark.smoke
def test_product_cart_with_multiple_products(page):
    cart_page = Cart(page)
    base_page = BasePage(page)
    product_page = ProductsPage(page)
    base_page.click_product()

    product_list = ["top", "dress", "tshirt"]
    for el in product_list:
        product_page.product_search_fill(el)
        product = product_page.add_to_cart_button()
        product.wait_for(state="visible")
        product.scroll_into_view_if_needed()
        product.hover(force=True)   
        product.click(force=True)
        expect(product_page.product_added()).to_be_visible()
        product_page.click_continue_shopping()
    base_page.click_cart()
    expect(cart_page.cart_products).to_have_count(len(product_list))
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()
    page.wait_for_timeout(10000)    
    


        


