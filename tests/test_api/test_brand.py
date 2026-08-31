from pages.api.brands_client import BrandClient
from playwright.sync_api import expect
from test_data.api_schema import brand_scheme
import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_get_all_brands(api_client):
    brand_client = BrandClient(api_client)
    response = brand_client.get_all_brands()
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.status_text == "OK"
    response_data = response.json()
    assert response_data["responseCode"] == 200
    assert "brands" in response_data
    assert isinstance(response_data["responseCode"],int)
    assert isinstance(response_data["brands"],list)
    brand = response_data["brands"]
    first_product = brand[0]
    assert "id" in first_product
    assert "brand" in first_product
    assert len(brand) >0


@pytest.mark.api
def test_scheme_validate(scheme_validate,api_client):
    brand_client = BrandClient(api_client)
    response = brand_client.get_all_brands()
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.status_text == "OK"
    response_data = response.json()
    brand = response_data["brands"]
    first_product = brand[0]
    is_valid = scheme_validate(first_product,brand_scheme)






