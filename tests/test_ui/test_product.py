from playwright.sync_api import expect
from utils.read_file import dict_read
from pages.ui.products import ProductsPage
from pages.ui.base_page import BasePage
import pytest
from faker import Faker


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
    expect(product_page.product_list_exists()).to_be_visible()




@pytest.mark.ui
@pytest.mark.parametrize("product_name",dict_read("./test_data/add_to_cart.json"))
def test_add_product_to_cart(page,product_name):
    if isinstance(product_name,tuple):
        product_name = product_name[0]
    base_page = BasePage(page)
    product_page = ProductsPage(page)
    base_page.click_product()
    count = product_page.product_search_fill(product_name)
    product = product_page.add_to_cart_button()
    product.wait_for(state="visible")
    product.scroll_into_view_if_needed()
    product.hover(force=True)
    product.click(force=True)
    expect(product_page.product_added()).to_be_visible()
    product_page.click_continue_shopping()

    assert count >= 0


@pytest.mark.ui
@pytest.mark.parametrize("category_name, sub_category_name",dict_read("./test_data/category.json"))
def test_category(page,category_name,sub_category_name):
    product_page = ProductsPage(page)
    category = product_page.category()
    true_element = None
    for element in category:
        element_name = element.inner_text().strip()
        if element_name.lower() == category_name.lower():
            element.click()
            true_element = element
            break
    if true_element is not None:
        sub_category = page.locator(f"#{category_name} a").filter(has_text=sub_category_name).first
        sub_category.wait_for(state="visible")
        sub_category.click()
        expect(product_page.product_list_exists()).to_be_visible()


@pytest.mark.ui
def test_product_review(page):
    base_page = BasePage(page)
    base_page.click_product()
    product_page = ProductsPage(page)
    product_page.click_view_product()
    faker = Faker()
    product_page.add_review(faker.user_name(),faker.email(),faker.text())
    expect(product_page.review_success_msg()).to_contain_text("Thank you for your review.")














