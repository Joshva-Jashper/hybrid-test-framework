from playwright.sync_api import expect
from pages.api.user_client import UserClient
from test_data.api_schema import user_body,user_body_dup_email,user_body_delete
from test_data.api_user import user_body_
from faker import Faker
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_create_user(api_client):
    user_client = UserClient(api_client)
    faker = Faker()
    user_body["email"] = faker.email()
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


@pytest.mark.api 
def test_delete_user(api_client):
    user_client = UserClient(api_client)
    response = user_client.create_user(user_body_delete)
    expect(response).to_be_ok()
    response_data = response.json()
    assert response.status == 200
    assert response.status_text == "OK"
    assert response_data["responseCode"] == 201
    assert "User created!" in response_data["message"]
    delete_email = user_body_delete["email"]
    delete_password = user_body_delete["password"]
    delete_response = user_client.delete_user(delete_email,delete_password)
    expect(delete_response).to_be_ok()
    delete_response.status == 200
    delete_response.status_text == "OK"
    delete_response_data = delete_response.json()
    assert delete_response_data["responseCode"] == 200
    assert "Account deleted!" in delete_response_data["message"]

@pytest.mark.api
def test_get_user_by_email(api_client):
    get_client = UserClient(api_client)
    user_response = get_client.get_user_by_email("traceywillis@example.com")
    expect(user_response).to_be_ok()
    assert user_response.status == 200
    assert user_response.status_text == "OK"
    user_data = user_response.json()
    assert user_data["responseCode"] == 200
    assert "user" in user_data
    assert user_data["user"]["email"] == "traceywillis@example.com"


    








