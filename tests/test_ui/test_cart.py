from playwright.sync_api import expect
import pytest
from pages.ui.base_page import BasePage
from pages.ui.products import ProductsPage
from pages.ui.login_signup_page import LoginSignupPage
from pages.ui.cart import Cart
from pages.ui.payment import Payment
from faker import Faker

@pytest.mark.ui
@pytest.mark.smoke
def test_product_cart_with_one_product(page):
    cart_page = Cart(page)
    base_page = BasePage(page)
    product_page = ProductsPage(page)
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

    total_price = 0
    for el in cart_page.get_products_cart():
        price = cart_page.calculate_total_price(el)
        total_price += price
   
    cart_page.get_checkout()
    checkout_price = cart_page.get_checkout_price()
    assert total_price == checkout_price 

    base_page.click_cart()
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()
   


        

@pytest.mark.ui
def test_checkout_after_removing_product(page):
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

    total_price = 0
    for el in cart_page.get_products_cart():
        price = cart_page.calculate_total_price(el)
        total_price += price
    
    cart_page.get_checkout()
    checkout_price = cart_page.get_checkout_price()
    assert total_price == checkout_price 

    base_page.click_cart()
    full_product = cart_page.get_products_cart()
    first_product = full_product[0]
    first_product_price = cart_page.get_product_total_price(first_product)
    remove_product = cart_page.get_remove_product()
    remove_first_product = remove_product[0]
    remove_first_product.click()

    cart_page.get_checkout()
    checkout_price = cart_page.get_checkout_price()
    assert total_price-first_product_price == checkout_price

    base_page.click_cart()
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()



@pytest.mark.ui        
def test_cart_after_navigation(page):
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
    base_page.click_contact()
    base_page.click_cart()
    expect(cart_page.cart_products).to_have_count(len(product_list))
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()


@pytest.mark.ui
@pytest.mark.smoke
def test_verify_end_end(page):
    base_page = BasePage(page)
    product_page = ProductsPage(page)
    cart_page = Cart(page)
    payment_page = Payment(page)
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
    total_price = 0
    for el in cart_page.get_products_cart():
        price = cart_page.calculate_total_price(el)
        total_price += price
    
    cart_page.get_checkout()
    checkout_price = cart_page.get_checkout_price()
    assert total_price == checkout_price 

    expect(cart_page.get_delivery_address_title()).to_contain_text("Your delivery address")
    expect(cart_page.get_billing_title()).to_contain_text("Your billing address")
    delivery_name = cart_page.get_delivery_name().inner_text()
    billing_name = cart_page.get_billing_name().inner_text()
    assert delivery_name == billing_name

    faker = Faker()
    cart_page.get_comment_box(faker.text())
    cart_page.click_palce_order()

    payment_page.fill_payment_details(faker.user_name(),faker.credit_card_number(),faker.credit_card_security_code(),faker.month(),faker.year())
    expect(payment_page.get_confirmation_msg()).to_contain_text("Congratulations! Your order has been confirmed!")
    payment_page.click_continue_btn()

    base_page.click_cart()
    remove_product = cart_page.get_remove_product()
    for el in remove_product:
        el.click()



    
    






             


    




    

