import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import config
from source.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    APP_LOGO = (By.XPATH, "//div[@class='app_logo']")
    PRODUCT_LIST=(By.XPATH, "//div[@class='inventory_item']/div[@class='inventory_item_description']")
    PRODUCT_NAME=(By.CLASS_NAME, "inventory_item_name ")
    ADD_CART=(By.XPATH, ".//button[text()='Add to cart']")
    CART=(By.ID, "shopping_cart_container")
    CART_ITEM=(By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_ID=(By.ID, "checkout" )
    FIST_NAME=(By.ID, "first-name")
    LAST_NAME=(By.ID, "last-name")
    PIN=(By.ID, "postal-code")
    CONTINUE_ID=(By.ID, "continue")
    FINISH_ID=(By.ID, "finish")
    SUCCESS_MESSAGE=(By.XPATH, "//h2[@class='complete-header']")

    def __init__(self, driver):
        super(). __init__(driver)
        self.conf = config.load_config("config/config.yaml")
        self.sauce_url = self.conf["sauce_url"]
        self.driver=driver

    def load(self):
        self.driver.get(self.sauce_url)

    def login_user(self, username, password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.wait_for_element(self.APP_LOGO)
        # wait=WebDriverWait(self.driver,10)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))
        # assert
    def page_logo(self):
        return self.driver.find_element(*self.APP_LOGO).text == "Swag Labs"

    def select_product(self,product_name):
        products=self.driver.find_elements(*self.PRODUCT_LIST)
        for product in products:
            if  product.find_element(*self.PRODUCT_NAME).text == product_name:
                print(product.find_element(*self.PRODUCT_NAME).text)
                product.find_element(*self.ADD_CART).click()

                return True

    def cart_item_validate(self, product_name):
        self.driver.find_element(*self.CART).click()
        cart_item_name=self.driver.find_element(*self.CART_ITEM).text
        return cart_item_name== product_name


    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_ID).click()

    def add_details(self,fist_name, last_name, pin):
        self.driver.find_element(*self.FIST_NAME).send_keys(fist_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.PIN).send_keys(pin)
        self.driver.find_element(*self.CONTINUE_ID).click()
        self.driver.find_element(*self.FINISH_ID).click()


    def order_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text == "Thank you for your order!"






