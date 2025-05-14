import json
import pytest
import pandas as pd


import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import config
from data.payload_generator import PayloadGenerator
from source.login_page import LoginPage
from source.product_api import ProductAPI
from source.register_user_api import RegisterUserAPI

config = config.load_config("config/config.yaml")

@pytest.fixture(scope="session")
def browser():
    print("Launching a browser")
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    yield  driver
    driver.quit()

@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)



@pytest.fixture()
def context():
    return {}

@pytest.fixture
def yaml_file():
    return config["YAML_FILE"]

@pytest.fixture(scope="session")
def product_api():
    return ProductAPI()

@pytest.fixture(scope="session")
def register_api():
    return RegisterUserAPI()

@pytest.fixture()
def new_product(product_api):
    # payload=PayloadGenerator.generate_create_payload()
    payload=PayloadGenerator.get_payload("generate-create")
    response=product_api.create_product(payload)
    # print(response.status_code)
    data=response.json()
    product_id=data["product"]["id"]
    yield  product_id, payload
    product_api.delete_product(product_id)



# @pytest.fixture(params=json.load(open("data/registered_users.json")))
# def registered_user(request):
#     return request.param

# @pytest.fixture(params=pd.read_excel("data/register_user.xlsx", sheet_name="Sheet").to_dict(orient="records"))
# def registered_user(request):
#     return request.param

@pytest.fixture(params=yaml.safe_load(open("data/register_user.yaml")))
def registered_user(request):
    return request.param


