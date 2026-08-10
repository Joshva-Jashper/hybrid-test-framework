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

def test_product_list_exists(page):
    base_page = BasePage(page)
    base_page.click_product()
    product_page = ProductsPage(page)
    expect(product_page.product_list_exists()).to_be_visible(timeout=3000)






