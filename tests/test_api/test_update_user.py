from playwright.sync_api import expect
from pages.api.update_client import UpdateClient
from pages.api.user_client import UserClient
import pytest

from test_data.api_schema import user_body_update,username,email

@pytest.mark.api
def test_update_user(api_client):
    user_client = UpdateClient(api_client)
    response = user_client.update_user(user_body_update)
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.status_text == "OK"
    response_data = response.json()
    assert response_data["responseCode"] == 200
    assert "User updated!" in response_data["message"]

    get_client = UserClient(api_client)
    user_response = get_client.get_user_by_email("joshva@gmail.com")
    expect(user_response).to_be_ok()
    assert user_response.status == 200
    assert user_response.status_text == "OK"
    user_data = user_response.json()
    assert user_data["responseCode"] == 200
    assert "user" in user_data
    assert username == user_data["user"]["name"]
    assert email == user_data["user"]["email"]

    