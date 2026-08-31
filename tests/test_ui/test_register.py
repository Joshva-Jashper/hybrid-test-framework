from playwright.sync_api import expect
from faker import Faker

from pages.ui.base_page  import BasePage
from pages.ui.login_signup_page import LoginSignupPage
from pages.ui.signup import Signup
import pytest
from utils.read_file import dict_read


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.no_auth
def test_register(page):
    base_page = BasePage(page)
    login_signup = LoginSignupPage(page)
    signup = Signup(page)
    faker = Faker()
    base_page.click_signup_login()
    expect(login_signup.check_signup_form()).to_be_visible()
    login_signup.signup(faker.email(), faker.user_name())
    expect(signup.signup_form_check()).to_be_visible()
    signup.signup("married",faker.first_name(), faker.last_name(), faker.password(),"1", "12", "2005", faker.company(),
                                                    faker.address(),"India", faker.state(), faker.zipcode(), faker.city(), str(faker.phone_number()))
    expect(signup.signup_done()).to_be_visible()



@pytest.mark.no_auth
@pytest.mark.ui
def test_already_registered_user(page):
    base_page = BasePage(page)
    login_signup = LoginSignupPage(page)
    signup = Signup(page)
    base_page.click_signup_login()
    expect(login_signup.check_signup_form()).to_be_visible()
    login_signup.signup("alex.kumar.qa3@example.com", "alexkumarqa03")
    expect(login_signup.check_user_exists()).to_be_visible()















