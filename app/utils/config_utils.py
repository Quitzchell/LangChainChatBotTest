import json
import os


class ConfigUtils:
    @staticmethod
    def load_config(config_path: str) -> dict:
        try:
            with open(config_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise ValueError("Invalid or missing configuration file.")

    @staticmethod
    def write_config(config_path: str, config_data):
        with open(config_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=4)

    @staticmethod
    def get_filename(file_path):
        base_name = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(base_name)
        return filename
