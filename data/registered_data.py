import json
import os.path
import random
import uuid

import yaml


from data.save_data_in_files import SaveData


class RegisteredData:

    @staticmethod
    def save_register_data(user_file, payload):
        if user_file.endswith(".json"):
            SaveData.save_json(user_file,payload)

        elif user_file.endswith(".xlsx"):
            SaveData.save_excel(user_file, payload)

        elif user_file.endswith(".yaml") or user_file.endswith(".yml"):
            SaveData.save_yaml(user_file, payload)

