class UserClient:
    def __init__(self,api_client):
        self.api_client = api_client

    def create_user(self,body):
        return self.api_client.post("/api/createAccount",data=body)

    def get_user_by_email(self,email):
        return self.api_client.get("/api/getUserDetailByEmail",params = {"email" : email})
    

