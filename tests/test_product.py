from playwright.sync_api import expect
from utils.read_file import dict_read
from pages.products import ProductsPage
from pages.base_page import BasePage
import pytest



@pytest.mark.ui
@pytest.mark.parametrize("product_name,found_or_not",dict_read("./test_data/products.json"))
def test_products_find(page,product_name,found_or_not):
    product_page = ProductsPage(page)
    base_page = BasePage(page)
    base_page.click_product()
    product_count = product_page.product_search_fill(product_name)
    if found_or_not == "yes":
        assert product_count > 1
    else:
        assert product_count == 1

@pytest.mark.ui
def test_product_list_exists(page):
    base_page = BasePage(page)
    base_page.click_product()
    product_page = ProductsPage(page)
    expect(product_page.product_list_exists()).to_be_visible(timeout=3000)




@pytest.mark.ui
@pytest.mark.parametrize("product_name",dict_read("./test_data/add_to_cart.json"))
def test_add_product_to_cart(page,product_name):
    if isinstance(product_name,tuple):
        product_name = product_name[0]
    base_page = BasePage(page)
    product_page = ProductsPage(page)
    base_page.click_product()
    count = product_page.product_search_fill(product_name)
    first_product = product_page.add_to_cart_button()
    for el in first_product:
        el.click(force=True,timeout=3000)
        expect(product_page.product_added()).to_be_visible(timeout=3000)
    assert count >= 0
    product_page.click_continue_shopping()










