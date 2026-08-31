from playwright.sync_api import expect
from pages.ui.base_page import BasePage
from pages.ui.cart import Cart
from pages.ui.products import ProductsPage
import pytest


@pytest.mark.ui
@pytest.mark.no_auth
def test_guest_checkout_attempt(page):
    base_page = BasePage(page)
    product_page = ProductsPage(page)
    cart_page = Cart(page)
    base_page.click_product()
    count = product_page.product_search_fill("T shirt")
    product = product_page.add_to_cart_button()
    product.wait_for(state="visible")
    product.scroll_into_view_if_needed()
    product.hover(force=True)
    product.click(force=True)
    expect(product_page.product_added()).to_be_visible()
    product_page.click_continue_shopping()
    assert count >= 0    

    base_page.click_cart()
    cart_page.get_checkout()
    expect(cart_page.get_checkout_without_login_msg()).to_contain_text("Register / Login account to proceed on checkout.")
    cart_page.click_continue_to_cart_btn()
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()

        








        


