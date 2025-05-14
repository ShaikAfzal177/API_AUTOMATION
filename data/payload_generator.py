

from data.api_payload import APIPayload


class PayloadGenerator:

    @staticmethod
    def get_payload( payload_type, *args, **kwargs):
        """
        Master method to return payloads based on input string.
        :param payload_type: str - Type of payload to generate
        :param args: Optional parameters (like product_id)
        :return: dict - Payload
        """
        if payload_type == "generate-create":
            return APIPayload.generate_create_payload()
        elif payload_type == "generate-update":
            return APIPayload.generate_update_payload(*args)
        elif payload_type == "generate-user-password":
            return APIPayload.generate_user_payload()
        elif payload_type == "generate-username":
            return APIPayload.generate_username_payload()
        else:
            raise ValueError(f"Unknown payload type: {payload_type}")
