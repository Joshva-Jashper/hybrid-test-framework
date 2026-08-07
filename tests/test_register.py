from playwright.sync_api import expect


from pages.base_page  import BasePage
from pages.login_signup_page import LoginSignupPage
from pages.signup import Signup
import pytest
from utils.read_file import dict_read


@pytest.mark.ui
@pytest.mark.parametrize("email,username,status,firstname,lastname,password,day,month,year,company,address,country,state,zipcode,city,mobile_number",
                         dict_read("../test_data/signup.json"))
def test_register(page,email,username,status,firstname,lastname,password,day,month,year,company,address,country,state,zipcode,city,mobile_number):
    base_page = BasePage(page)
    login_signup = LoginSignupPage(page)
    signup = Signup(page)
    base_page.click_signup_login()
    expect(login_signup.check_signup_form()).to_be_visible(timeout=3000)
    login_signup.signup(email,username)
    expect(signup.signup_form_check()).to_be_visible(timeout=3000)
    signup.signup(status,firstname,lastname,password,day,month,year,company,address,country,state,zipcode,city,mobile_number)
    expect(signup.signup_done()).to_be_visible(timeout=3000)










