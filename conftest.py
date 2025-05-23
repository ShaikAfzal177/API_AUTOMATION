import csv
import json
from email.policy import default

import pytest
import pandas as pd


import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import config
from data.payload_generator import PayloadGenerator
from source.login_page_flipkart import FlipkartPage
from source.login_page_sauce import LoginPage
from source.product_api import ProductAPI
from source.register_user_api import RegisterUserAPI

config = config.load_config("config/config.yaml")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="session")
def browser(request):
    browser_type=request.config.getoption("--browser").lower()
    print(f"Launching a {browser_type} browser")
    if browser_type =="chrome":
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
    elif browser_type =="firefox":
        service=Service(GeckoDriverManager().install())
        driver=webdriver.Firefox(service=service)
    elif browser_type =="edge":
        service=Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    driver.maximize_window()
    yield  driver
    driver.quit()

@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)
@pytest.fixture()
def flipkart_page(browser):
    return FlipkartPage(browser)


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



@pytest.fixture(params=json.load(open("data/registered_users.json")))
def registered_user_json(request):
    return request.param

@pytest.fixture(params=pd.read_excel("data/register_user.xlsx", sheet_name="Sheet").to_dict(orient="records"))
def registered_user_xl(request):
    return request.param

@pytest.fixture(params=yaml.safe_load(open("data/register_user.yaml")))
def registered_user(request):
    return request.param

@pytest.fixture(params=[row for row in csv.DictReader(open("data/register_user.csv"))])
def registered_user_csv(request):
    return request.param
