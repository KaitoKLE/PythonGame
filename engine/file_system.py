from json import load as load_json, JSONDecodeError
from logging import error
from os import scandir
from os.path import splitext, exists

from pygame import image, error as pygame_error, transform

from settings.paths import ASSETS, SPRITE_SHEETS, MAPS_DIR, DATA_DIR


class FileSystem:
    __cache = {}

    @classmethod
    def exec_operation(cls, file, operation):
        if (file, operation) in FileSystem.__cache:
            return FileSystem.__cache[(file, operation)]
        try:
            result = operation(file)
            FileSystem.__cache[(file, operation)] = result
            return result
        except (FileNotFoundError, PermissionError, IOError, JSONDecodeError, pygame_error) as e:
            error(e)
            exit()

    @classmethod
    def parse_json(cls, file):
        file = cls.exec_operation(f'{DATA_DIR}/{file}', open)
        data = cls.exec_operation(file, load_json)
        file.close()
        return data

    @classmethod
    def load_image(cls, path, scale=None):
        img = cls.exec_operation(path, image.load)
        if scale:
            if isinstance(scale, int):
                img = transform.scale(img, (img.get_size()[0] * scale, img.get_size()[1] * scale))
            elif isinstance(scale, tuple) or isinstance(scale, list):
                img = transform.scale(img, scale)
        return img

    @classmethod
    def load_sprite(cls, key):
        path = f'{ASSETS}{SPRITE_SHEETS}/{key}'
        img = cls.load_image(path)
        json_path = path.replace('.png', '.json')
        properties = cls.parse_json(json_path) if exists(json_path) else {}
        return img, properties

    @classmethod
    def scan_maps(cls) -> dict:
        data = {}
        files = cls.exec_operation(f'{DATA_DIR}/{MAPS_DIR}', scandir)
        for file in files:
            data[splitext(file.name)[0]] = cls.parse_json(f'{MAPS_DIR}/{file.name}')
        return data
