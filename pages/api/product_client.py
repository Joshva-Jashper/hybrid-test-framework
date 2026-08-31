class ProductClient():

    def __init__(self,api_client):
        self.api_client = api_client
        
    def get_all_products(self):
        return self.api_client.get("/api/productsList")

        