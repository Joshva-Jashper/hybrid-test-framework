from playwright.sync_api import expect
from pages.ui.base_page import BasePage
from pages.ui.signup import Signup
from pages.ui.login_signup_page import LoginSignupPage
from utils.read_file import dict_read
import pytest

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.parametrize("email,password,success_or_failure",dict_read("./test_data/login.json"))
@pytest.mark.no_auth
def test_login_with_credentials(page,email,password,success_or_failure):
    base_page = BasePage(page)
    login_page = LoginSignupPage(page)
    base_page.click_signup_login()
    login_page.login(email,password)
    if success_or_failure == "success":
        expect(login_page.success_full_login()).to_be_visible()
    else:
        expect(login_page.not_success_full_login()).to_be_visible()

@pytest.mark.ui
@pytest.mark.no_auth
def test_login_logout(page):
    base_page = BasePage(page)
    login_page = LoginSignupPage(page)
    base_page.click_signup_login()
    login_page.login("jane.doe.qa01@xample.com","SecurePass@123")
    expect(login_page.success_full_login()).to_be_visible()
    login_page.click_logout_button()
    expect(login_page.check_login_form()).to_be_visible()


@pytest.mark.ui
@pytest.mark.no_auth
def test_delete_user(page):
    base_page = BasePage(page)
    login_page = LoginSignupPage(page)
    signup = Signup(page)
    base_page.click_signup_login()
    login_page.login("jane.doe.qa01@xample.com", "SecurePass@123")
    expect(login_page.success_full_login()).to_be_visible()
    login_page.click_delete_account()
    expect(login_page.account_deleted_msg()).to_be_visible()
    base_page.click_signup_login()
    login_page.login("jane.doe.qa01@xample.com", "SecurePass@123")
    expect(login_page.not_success_full_login()).to_be_visible()
    base_page.click_signup_login()
    expect(login_page.check_signup_form()).to_be_visible()
    login_page.signup("jane.doe.qa01@xample.com", "janedoeqa01")
    expect(signup.signup_form_check()).to_be_visible()
    signup.signup("married", "Jane", "Doe", "SecurePass@123", "15", "June", "1998", "QA Solutions Pvt Ltd",
                  "12 Test Street", "India", "Tamil Nadu", "641001", "Coimbatore", "9876543210")
    expect(signup.signup_done()).to_be_visible()












