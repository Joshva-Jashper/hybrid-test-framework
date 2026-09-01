from playwright.sync_api import APIRequestContext,Playwright
import pytest
from jsonschema import validate

class BaseApiClient:
    def __init__(self,playwright:Playwright,timeout:int=10000):
        self.url = "https://automationexercise.com";
        self.timeout = timeout
        self.request:APIRequestContext = playwright.request.new_context(
                base_url = self.url,
                extra_http_headers = {"Accept" : "application/json"},
                timeout = self.timeout
        )

    def get(self,endpoint:str,params:dict=None,**kwargs):
        return self.request.get(endpoint,params=params,**kwargs)

    def post(self,endpoint:str,data=None,**kwargs):
        if isinstance(data, (str, bytes)):
            return self.request.post(endpoint, data=data, **kwargs)
        return self.request.post(endpoint,form=data,**kwargs)

    def put(self,endpoint:str,data:dict=None,**kwargs):
        return self.request.put(endpoint,form=data,**kwargs)

    def delete(self,endpoint:str,**kwargs):
        return self.request.delete(endpoint,**kwargs)

    def close(self):
        self.request.dispose()        



@pytest.fixture(scope="function")
def api_client(playwright:Playwright):
    client = BaseApiClient(playwright)
    yield client
    client.close()



@pytest.fixture(scope="function")
def scheme_validate():
    def _validate(json,schema):
        try:
            validate(instance=json,schema=schema)
            return True
        except Exception:
            return False
    return _validate

    

                
            
