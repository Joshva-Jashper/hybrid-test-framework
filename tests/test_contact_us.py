from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.contact import ContactUs
import pytest
from faker import Faker

@pytest.mark.ui
@pytest.mark.no_auth
def test_check_contact_us(page):
    base_page = BasePage(page)
    contact_page = ContactUs(page)
    faker = Faker()

    base_page.click_contact()
    expect(contact_page.get_contact_header()).to_contain_text("Get In Touch")

    contact_page.fill_contact_details(faker.user_name(),faker.email(),faker.sentence(),faker.sentence(),"/home/joshva_jashper/Documents/hybrid-test-framework/file.txt")
    


