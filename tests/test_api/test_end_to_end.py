from playwright.sync_api import expect,Page
from test_data.api_schema import user_body
from pages.api.user_client import UserClient
from pages.ui.login_signup_page import LoginSignupPage
from pages.ui.signup import Signup
from pages.ui.base_page import BasePage
from faker import Faker
import pytest

@pytest.mark.e2e
def test_register_api_ui(api_client,page:Page):
    user_client = UserClient(api_client)
    faker = Faker()
    email = faker.email()
    user_body["email"] = email
    password = user_body["password"]
    response = user_client.create_user(user_body)
    expect(response).to_be_ok()
    response_data = response.json()
    assert response.status == 200
    assert response.status_text == "OK"
    assert response_data["responseCode"] == 201
    assert "User created!" in response_data["message"]

    page.goto("https://automationexercise.com/")
    login_page = LoginSignupPage(page)
    base_page = BasePage(page)
    base_page.click_signup_login()
    login_page.login(email,password)
    expect(login_page.success_full_login()).to_be_visible()


@pytest.mark.e2e
def test_register_ui_api(api_client,page:Page):
    page.goto("https://automationexercise.com/")
    base_page = BasePage(page)
    login_signup = LoginSignupPage(page)
    signup = Signup(page)
    faker = Faker()
    email = faker.email()
    name = faker.user_name()
    base_page.click_signup_login()
    expect(login_signup.check_signup_form()).to_be_visible()
    login_signup.signup(email, name)
    expect(signup.signup_form_check()).to_be_visible()
    signup.signup("married",faker.first_name(), faker.last_name(), faker.password(),"1", "12", "2005", faker.company(),
                                                faker.address(),"India", faker.state(), faker.zipcode(), faker.city(), str(faker.phone_number()))
    expect(signup.signup_done()).to_be_visible()
   
    get_client = UserClient(api_client)
    user_response = get_client.get_user_by_email(email)
    expect(user_response).to_be_ok()
    assert user_response.status == 200
    assert user_response.status_text == "OK"
    user_data = user_response.json()
    assert user_data["responseCode"] == 200
    assert "user" in user_data
    assert user_data["user"]["email"] == email
    assert user_data["user"]["name"] == name


@pytest.mark.e2e
def test_delete_user_via_ui(api_client,page:Page):
    user_client = UserClient(api_client)
    faker = Faker()
    email = faker.email()
    password = faker.password()
    user_body["email"] = email
    user_body["password"] = password
    response = user_client.create_user(user_body)
    expect(response).to_be_ok()
    response_data = response.json()
    assert response.status == 200
    assert response.status_text == "OK"
    assert response_data["responseCode"] == 201
    assert "User created!" in response_data["message"]

    delete_response = user_client.delete_user(email,password)
    expect(delete_response).to_be_ok()
    delete_response.status == 200
    delete_response.status_text == "OK"
    delete_response_data = delete_response.json()
    assert delete_response_data["responseCode"] == 200
    assert "Account deleted!" in delete_response_data["message"]

    page.goto("https://automationexercise.com/")
    base_page = BasePage(page)
    login_page = LoginSignupPage(page)
    base_page.click_signup_login()
    login_page.login(email,password)
    expect(login_page.not_success_full_login()).to_be_visible()






        









