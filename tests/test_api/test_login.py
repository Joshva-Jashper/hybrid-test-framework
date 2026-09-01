from playwright.sync_api import expect
from pages.api.user_login import UserLogin
from pages.api.user_client import UserClient
from test_data.api_schema import user_body
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_user_login_with_valid_credential(api_client):
    user_client = UserLogin(api_client)
    user = UserClient(api_client)
    response = user.create_user(user_body)
    expect(response).to_be_ok()
    response_data = response.json()
    assert response.status == 200
    assert response.status_text == "OK"
    assert response_data["responseCode"] == 201
    assert "User created!" in response_data["message"]
    email = user_body["email"]
    password = user_body["password"]
    login_response = user_client.login_with_user_credentials(email,password)
    expect(login_response).to_be_ok()
    assert login_response.status == 200
    assert login_response.status_text == "OK"
    login_response_data = login_response.json()
    assert login_response_data["responseCode"] == 200
    assert "User exists!" in login_response_data["message"]

@pytest.mark.api
@pytest.mark.smoke
def test_user_login_with_invalid_credential(api_client):
    user_client = UserLogin(api_client)
    login_response = user_client.login_with_user_credentials("jjjjjjj@gmail.com","123456")
    expect(login_response).to_be_ok()
    assert login_response.status == 200
    assert login_response.status_text == "OK"
    login_response_data = login_response.json()
    assert login_response_data["responseCode"] == 404
    assert "User not found!" in login_response_data["message"]
    