import pytest
import config
from data.payload_generator import PayloadGenerator
from data.registered_data import RegisteredData
from response.response_file import ResponseFile

# USER_FILE = "data/registered_users.json"
# USER_FILE_1="data/register_user.xlsx"
config = config.config.load_config("config/config.yaml")
JSON_FILE = config["JSON_FILE"]
EXCEL_FILE_1 = config["EXCEL_FILE_1"]
YAML_FILE=config["YAML_FILE"]


@pytest.mark.usefixtures("product_api","register_api")
class TestProductCrud:

    @pytest.mark.smoke
    def test_create_product(self, product_api):
        payload=PayloadGenerator.get_payload("generate-create")
        response=product_api.create_product(payload)
        data=response.json()
        ResponseFile.response_validate(data,payload, parent_key="product", message="Product added successfully")

    @pytest.mark.smoke
    def test_get_all_products(self, product_api):
        response=product_api.get_all_products()
        data=response.json()
        print(data)


    @pytest.mark.smoke
    def test_get_product_by_id(self, product_api, new_product):
        product_id, payload=new_product
        response=product_api.get_product_by_id(product_id)
        data = response.json()
        ResponseFile.response_validate(data, payload)

    @pytest.mark.smoke
    def test_update_product(self, product_api, new_product):
        product_id, _ =new_product
        update_payload = PayloadGenerator.get_payload("generate-update",product_id)
        response=product_api.update_product(update_payload)
        data = response.json()
        ResponseFile.response_validate(data, update_payload, parent_key="product", message="Product updated successfully")

    @pytest.mark.smoke
    def test_delete_product(self,product_api):

        payload = PayloadGenerator.get_payload("generate-create")
        response=product_api.create_product(payload)
        product_id=response.json()["product"]["id"]
        del_response=product_api.delete_product(product_id)
        data=del_response.json()
        ResponseFile.response_validate(data, message="Product deleted successfully")
    @pytest.mark.smoke
    def test_register_user(self, register_api):
        payload = PayloadGenerator.get_payload("generate-user-password")
        response=register_api.register_user(payload)
        data=response.json()
        user_name=payload["username"]
        ResponseFile.response_validate(data, user=user_name, message="User registered successfully")
        RegisteredData.save_register_data(YAML_FILE, payload)

    @pytest.mark.smoke
    def test_register_user_without_password(self, register_api):
        payload = PayloadGenerator.get_payload("generate-username")
        response=register_api.register_user(payload)
        assert response.json()["detail"] == "Missing password"

    @pytest.mark.smoke
    def test_login_user(self,register_api, registered_user):
        response=register_api.login(payload=registered_user)
        data=response.json()
        ResponseFile.response_validate(data, message="Login successful")

