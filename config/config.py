import yaml


# Function to load YAML config
def load_config(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)