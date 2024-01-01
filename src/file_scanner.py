import json
import logging


class FileScanner:
    @classmethod
    def scan_json(cls, path):
        try:
            with open(path) as file:
                return json.load(file)
        except (FileNotFoundError, PermissionError, IOError) as e:
            logging.exception('Could not scan file: ')
            return None
