class BrandClient:
    def __init__(self,api_client):
        self.api_client = api_client

    def get_all_brands(self):
        return self.api_client.get("/api/brandsList")    
