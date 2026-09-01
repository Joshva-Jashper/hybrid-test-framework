from playwright.sync_api import expect,Page
from test_data.api_schema import user_body
from pages.api.user_client import UserClient
from pages.ui.login_signup_page import LoginSignupPage
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




