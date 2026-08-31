from playwright.sync_api import expect
from pages.api.user_client import UserClient
from test_data.api_schema import user_body,user_body_dup_email
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_create_user(api_client):
    user_client = UserClient(api_client)
    response = user_client.create_user(user_body)
    expect(response).to_be_ok()
    response_data = response.json()
    assert response.status == 200
    assert response.status_text == "OK"
    assert response_data["responseCode"] == 201
    assert "User created!" in response_data["message"]

@pytest.mark.api
def test_create_user_with_duplicate_email(api_client):
    product_client = UserClient(api_client)
    response = product_client.create_user(user_body_dup_email)
    expect(response).to_be_ok()
    response_data = response.json()
    assert response.status == 200
    assert response.status_text == "OK"
    assert response_data["responseCode"] == 400
    assert "Email already exists!" in response_data["message"]








