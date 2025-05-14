import uuid
from faker import Faker
faker=Faker()

class APIPayload:

    @staticmethod
    def generate_create_payload():
        return {

            "name": f"Iphone-{uuid.uuid4().hex[:4]}",
            "description": "latest apple iphone",
            "price": faker.random_int(50000, 1000000)

        }


    @staticmethod
    def generate_update_payload( product_id):
        return {
            "id": product_id,
            "name": f"Iphone-{uuid.uuid4().hex[:4]}",
            "description": "latest apple iphone",
            "price": faker.random_int(50000, 1000000)
        }


    @staticmethod
    def generate_user_payload():
        payload = {
            "username": f"{faker.user_name()}",
            "password": f"{faker.password()}"
        }

        return payload


    @staticmethod
    def generate_username_payload():
        return {
            "username": f"{faker.user_name()}"

        }