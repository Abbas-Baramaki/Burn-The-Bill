import json
import urllib
class Setting:
    def __init__(self):
        self.my_sites = []
        self.query = ""
        self.accepts = []
        self.proxy_server = ""
        self.ipaddress = ""
        self.max_attempts = 0
        self.errors = []
    
    
    def fill(self) -> None:
        data = open("./_dependencies/data/setting.json","r",encoding="UTF-8").read()
        data = json.loads(data)
        self.my_sites = data["MY_SITES"]
        self.query = data["QUERY"]
        self.accepts = data["ACCEPTIES"]
        self.proxy_server = data["PROXY_SERVER"]
        self.max_attempts = data["MAX_ATTEMPT"]
        self.errors = data["ERRORS"]
        # self.query = urllib.parse.quote(data["QUERY"])

        del data
    
    def ip(self,value):
        self.ipaddress = value
    
    @property
    def ip(self)->str:
        return self.ipaddress
    
    def __str__(self):
        return self.query