class UpdateClient:
    def __init__(self,api_client):
        self.api_client =api_client

    def update_user(self,data):
        return self.api_client.put("/api/updateAccount",data=data) 
       