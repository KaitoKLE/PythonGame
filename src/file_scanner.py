import json
import logging

import pygame


class FileScanner:
    
    @classmethod
    def scan_json(cls, path):
        try:
            with open(path) as file:
                return json.load(file)
        except (FileNotFoundError, PermissionError, IOError) as e:
            logging.error(f'Could not scan file: {e}')
            return None
    
    @classmethod
    def load_image(cls, path):
        try:
            return pygame.image.load(path)
        except (FileNotFoundError, PermissionError, IOError) as e:
            logging.error(f'Could not scan file: {e}')
            return pygame.Surface((1, 1))
