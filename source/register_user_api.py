import requests
from config import config


class RegisterUserAPI:

    def __init__(self):
        self.config = config.load_config("config/config.yaml")
        self.base_url = self.config["base_url"]
        self.session=requests.Session()

    def register_user(self, payload):
        return self.session.post(f"{self.base_url}/register", json=payload)

    def login(self, payload):
        return  self.session.post(f"{self.base_url}/login", json=payload)