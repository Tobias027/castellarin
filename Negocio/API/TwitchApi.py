import os
import dotenv
import requests
import time

class TwitchApi:
    
    dotenv.load_dotenv()
    
    CLIENT_ID= os.environ.get("ID_cliente")
    CLIENT_SECRET=os.environ.get("Secret_cliente")
    
    def __init__(self):
        self.TOKEN = None
        self.TOKEN_EXPIRES=0
    
    def generate_token(self):
        
        response= requests.post(
            'https://id.twitch.tv/oauth2/token',
            data={
            "client_id":self.CLIENT_ID,
            "client_secret":self.CLIENT_SECRET,
            "grant_type":"client_credentials"
            }      
        )
        
        if response.status_code==200:
            data= response.json()
            self.TOKEN=data["access_token"]
            self.TOKEN_EXPIRES=time.time()+data["expires_in"]

        else:
            self.TOKEN = None
            self.TOKEN_EXPIRES=0
            
    def token_valid(self):
        return time.time()<self.TOKEN_EXPIRES
    
    def live(self, user:str):
        
        if not self.token_valid():
            self.generate_token()
            
        response= requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={user}",
            headers={
                "Client-ID": self.CLIENT_ID,
                "Authorization": f"Bearer {self.TOKEN}"
            }
        )
        
        if response.status_code ==200 and response.json()["data"]:
            data=response.json()["data"]
            title = data[0]['title']
            return {"bool":True,"title":title}
        return {"bool":False,"title": ""}