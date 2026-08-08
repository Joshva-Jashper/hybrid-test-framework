from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.signup import Signup
from pages.login_signup_page import LoginSignupPage
from utils.read_file import dict_read
import pytest

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.parametrize("email,password,success_or_failure",dict_read("./test_data/login.json"))
def test_login_with_credentials(page,email,password,success_or_failure):
    base_page = BasePage(page)
    login_page = LoginSignupPage(page)
    base_page.click_signup_login()
    login_page.login(email,password)
    if success_or_failure == "success":
        expect(login_page.success_full_login()).to_be_visible(timeout=3000)
    else:
        expect(login_page.not_success_full_login()).to_be_visible(timeout=3000)







