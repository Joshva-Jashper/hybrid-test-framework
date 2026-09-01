class UserLogin:
    def __init__(self,api_client):
        self.api_client = api_client

    def login_with_user_credentials(self,email,password):
        return self.api_client.post("/api/verifyLogin",data = {"email" : email,"password" : password})
        