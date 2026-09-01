from playwright.sync_api import expect
from pages.api.update_client import UpdateClient
from pages.api.user_client import UserClient
import pytest

from test_data.api_user import user_body_update_,user_body_

@pytest.mark.api
def test_update_user(api_client):
    user_client = UpdateClient(api_client)

    user = UserClient(api_client)
    response_ = user.create_user(user_body_)
    expect(response_).to_be_ok()
    response_data_ = response_.json()
    assert response_.status == 200
    assert response_.status_text == "OK"
    assert response_data_["responseCode"] == 201
    assert "User created!" in response_data_["message"]

    user_body_update_["email"] = user_body_["email"]
    user_body_update_["name"] = user_body_["name"]
    user_body_update_["password"] = user_body_["password"]
    response = user_client.update_user(user_body_update_)
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.status_text == "OK"
    response_data = response.json()
    assert response_data["responseCode"] == 200
    assert "User updated!" in response_data["message"]

    get_client = UserClient(api_client)
    user_response = get_client.get_user_by_email(user_body_["email"])
    expect(user_response).to_be_ok()
    assert user_response.status == 200
    assert user_response.status_text == "OK"
    user_data = user_response.json()
    assert user_data["responseCode"] == 200
    assert "user" in user_data
    assert user_body_update_["name"] == user_data["user"]["name"]
    assert user_body_update_["email"] == user_data["user"]["email"]

    



    