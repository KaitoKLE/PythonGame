import json
import logging
import os

from pygame import image, Surface, error as pygame_error, transform

# important paths
RESOURCES = '../resources'
SPRITE_SHEETS = '/spritesheets/'
ICON_PATH = '../resources/icon.png'
LOG_FILE = '../logging.log'
PLAYER_SPRITE = 'player.png'
MOUSE_SPRITE = 'mouse.png'
NPC_JSON = '../resources/data_files/npcs.json'
MAPS_DATA = '../resources/data_files/maps/'


def exec_operation(file, operation):
    try:
        return operation(file)
    except (FileNotFoundError, PermissionError, IOError) as e:
        logging.error(e)
        return None


class FileSystem:

    @classmethod
    def scan_json(cls, path):
        try:
            file = exec_operation(path, open)
            data = exec_operation(file, json.load)
            file.close()
            return data
        except json.decoder.JSONDecodeError as e:
            logging.error(f'There was an error while parsing a json file: {e}')

    @classmethod
    def load_image(cls, path, fail=(1, 1)):
        try:
            return exec_operation(path, image.load)
        except pygame_error as e:
            logging.error(f'Could not load image file: {e}')
            return Surface(fail)

    @classmethod
    def load_image_scaled(cls, path, scale=2):
        img = cls.load_image(path)
        if isinstance(scale, int):
            img = transform.scale(img, (img.get_size()[0] * scale, img.get_size()[1] * scale))
        elif isinstance(scale, tuple) or isinstance(scale, list):
            img = transform.scale(img, scale)
        return img

    @classmethod
    def load_sprite(cls, key):
        path = RESOURCES + SPRITE_SHEETS + key
        image = cls.load_image(path)
        json_path = path.replace('.png', '.json')
        properties = cls.scan_json(json_path) if os.path.exists(json_path) else {}
        return image, properties

    @classmethod
    def scan_maps(cls) -> dict:
        data = {}
        files = exec_operation(MAPS_DATA, os.scandir)
        for file in files:
            data[os.path.splitext(file.name)[0]] = cls.scan_json(file.path)
        return data
