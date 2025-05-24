import time
from fileinput import close

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from config import config
from response.response_file import ResponseFile
from source.base_page import BasePage



class FlipkartPage(BasePage):
    search_box=(By.XPATH, "//input[@class='Pke_EE']")
    login_popup=(By.CSS_SELECTOR, "._30XB9F")
    products_locator=(By.CSS_SELECTOR, ".KzDlHZ")
    product_name_locator=(By.CSS_SELECTOR, ".VU-ZEz")
    price_locator=(By.CSS_SELECTOR, ".Nx9bqj.CxhGGd")
    description_locator=(By.CSS_SELECTOR, "div[class='yN+eNk w9jEaj'] p")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.logger = BasePage.get_logger()
        self.config=config.load_config("config/config.yaml")
    def load_flipkart(self):
        self.driver.get(self.config["flipkart_url"])
        time.sleep(5)

    def search_product(self, product_name):

        try:
            close_button=self.wait_for_element(self.login_popup)
            # Click the close button
            close_button.click()

            self.logger.info("Login popup closed successfully.")

        except Exception as e:
            self.logger.info("Popup not found or already closed. Skipping...")
        self.wait_for_element(self.search_box)
        search=self.driver.find_element(*self.search_box)
        search.send_keys(product_name)
        search.send_keys(Keys.RETURN)

        time.sleep(5)
    def click_the_product(self):
        products=self.driver.find_elements(*self.products_locator)
        i=1
        for product in products:
            if i==3:
                product.click()
                break
            i+=1
        # time.sleep(5)
    def get_product_details(self):
        window_handle=self.driver.window_handles
        self.driver.switch_to.window(window_handle[1])
        name=self.driver.find_element(*self.product_name_locator).text
        price=self.driver.find_element(*self.price_locator).text
        price =int(price.replace("₹", "").replace(",",""))
        description=self.driver.find_element(*self.description_locator).text
        self.payload={ "name": name,"description": description,"price":price}

    def product_create(self,product_api):

        response = product_api.create_product(self.payload)
        data = response.json()
        if "product" in data:
            ResponseFile.response_validate(data, self.payload, parent_key="product", message="Product added successfully")
            return data
        else:
            ResponseFile.response_validate(data, self.payload,message="Product already exists")


    def product_delete(self,product_api,product_id):
        response = product_api.delete_product(product_id)
        data=response.json()
        ResponseFile.response_validate(data, message="Product deleted successfully")
