#Fuck my life
#Why tf do i even do this shit?
import requests
import time
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def getAccessToken(server, username, password):
        accessresponse = requests.post(server+"/login", data="client_id=ANDR&grant_type=password&username="+username+"&password="+password).json()
        accesstoken = accessresponse['access_token']
        return accesstoken
def getLoginToken(server, accesstoken):
    loginresponse = requests.get(server+"/3/logintoken", auth=BearerAuth(accesstoken)).json()
    return loginresponse
#What was wrong about API v1?
