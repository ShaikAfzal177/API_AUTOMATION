import requests


from config import config


class ProductAPI:
    def __init__(self):
        # with open("config/config.yaml") as f:
        #     self.base_url=yaml.safe_load(f)["base_url"]
        self.config = config.load_config("config/config.yaml")
        self.base_url = self.config["base_url"]
        self.session=requests.Session()

    def create_product(self, payload):
        return self.session.post(f"{self.base_url}/add-product", json=payload)

    def get_all_products(self):
        return self.session.get(f"{self.base_url}/get-products")

    def get_product_by_id(self,product_id):
        return self.session.get(f"{self.base_url}/product/{product_id}")

    def update_product(self, payload):
        return self.session.put(f"{self.base_url}/update-product", json=payload)

    def delete_product(self, product_id):
        return self.session.delete(f"{self.base_url}/delete-product/{product_id}")

