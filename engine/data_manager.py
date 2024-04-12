import logging

from numpy import array, transpose

from engine.file_system import FileSystem
from engine.special import MapData

# KEYS, should be the same as the ones in the involved json file
NAME = 'name'
TS = 'tile_set'
NPCS = 'npc'
SPRITE_SHEET = 'sprite_sheet'
PLAYER_SPAWN = 'player_spawn'
LAYERS = 'layers'


class DataManager:
    __maps = {}
    __npcs = {}

    @classmethod
    def get_map_data(cls, map_id):
        if len(cls.__maps) == 0:
            raise Exception('Tried to access dada before loading...')
        try:
            return cls.__maps[map_id]
        except KeyError:
            raise Exception(f'The map id "{map_id}" is not registered')

    @classmethod
    def init(cls):
        logging.info(f'Scanning data files...')
        cls.__npcs = FileSystem.parse_json('npcs.json')
        maps = FileSystem.scan_maps()
        for key in maps.keys():
            cls.__maps[key] = cls.__convert_map_data(maps[key])
        if None in [cls.__maps, cls.__npcs]:
            logging.critical('At least one file could not be scanned')
            return False
        logging.info('Finished scanning data files!')
        return True

    @classmethod
    def __convert_map_data(cls, data):
        map_name = data[NAME]
        ts_path = data[TS]
        player_spawn = data[PLAYER_SPAWN]
        npc_locations = [tuple(x) for x in data[NPCS]]
        layers = []
        for layer in data[LAYERS]:
            layers.append(array(list(data[layer])))
        return MapData(map_name, ts_path, player_spawn, npc_locations, layers[0].shape, layers)

    @classmethod
    def get_npc_data(cls, npc_id):
        return cls.__npcs[npc_id][NAME], cls.__npcs[npc_id][SPRITE_SHEET]
