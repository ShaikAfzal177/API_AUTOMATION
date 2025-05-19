from source.base_page import BasePage


class ResponseFile:

    @staticmethod
    def response_validate(data, payload=None, parent_key=None, message=None, user=None):
        logger = BasePage.get_logger()
        logger.info("Starting response validation.")
        logger.debug(f"Response data: {data}")
        logger.debug(f"Payload data: {payload}")
        logger.debug(f"Validation parameters - parent_key: {parent_key}, message: {message}, user: {user}")
        if parent_key:
            assert data["product"]["name"] == payload["name"]
            assert data["product"]["description"]==payload["description"]
            assert data["product"]["price"] ==payload["price"]
            assert data["message"]==message
            logger.info(f"{message}")
        elif message and user:
            assert data["message"] ==message
            assert data["user"]['username'] == user
            logger.info(f"{message}")
        elif message:
            assert data["message"] == message
            logger.info(f"{message}")
        else:
            assert data["name"] == payload["name"]
            assert data["description"] == payload["description"]
            assert data["price"] == payload["price"]
            logger.info(f"product fetched successfully")
