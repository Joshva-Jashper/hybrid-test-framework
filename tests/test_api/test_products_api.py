from pages.api.product_client import ProductClient
from playwright.sync_api import expect
from test_data.api_schema import product_scheme

import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_get_all_products(api_client):
    product_client = ProductClient(api_client)
    response = product_client.get_all_products()
    response_data = response.json()
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.status_text == "OK"
    assert "products" in response_data
    assert response_data["responseCode"] == 200
    assert isinstance(response_data["products"],list)
    assert isinstance(response_data["responseCode"],int)

    product = response_data["products"]

    first_product = product[0]
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert "brand" in first_product
    assert "category" in first_product
    assert len(product)>0



@pytest.mark.api
def test_product_schema_validation(api_client,scheme_validate):
    product_client = ProductClient(api_client)
    response = product_client.get_all_products()
    response_data = response.json()
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.status_text == "OK"
    product = response_data["products"]
    first_product = product[0]
    is_valid = scheme_validate(first_product,product_scheme)
    assert is_valid





