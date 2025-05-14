from itertools import product


class ResponseFile:

    @staticmethod
    def response_validate(data, payload=None, parent_key=None, message=None, user=None):
        if parent_key:
            assert data["product"]["name"] == payload["name"]
            assert data["product"]["description"]==payload["description"]
            assert data["product"]["price"] ==payload["price"]
            assert data["message"]==message
        elif message and user:
            assert data["message"] ==message
            assert data["user"]['username'] == user
        elif message:
            assert data["message"] == message

        else:
            assert data["name"] == payload["name"]
            assert data["description"] == payload["description"]
            assert data["price"] == payload["price"]
