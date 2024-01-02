import logging

import numpy

from character import NPC
from file_scanner import FileScanner
from src.c_dataclasses import MapData
from src.constants import MAIN_PATH

# KEYS, should be the same as the ones in the involved json file
NAME = 'name'
TS = 'tile_set'
NPCS = 'npc'
COLLISION = 'collision'
SHAPE_Z0 = 'map_shape_z0'
SHAPE_Z1 = 'map_shape_z1'


class DataManager:
    maps = None
    
    @classmethod
    def init(cls):
        logging.info(f'Scanning data files...')
        cls.maps = FileScanner.scan_json('\\'.join((MAIN_PATH, 'resources/data_files/maps.json')))
        if None in [cls.maps]:
            logging.critical('At least one file could not be scanned')
            return False
        logging.info('Successfully done')
        return True
    
    @classmethod
    def get_map_data(cls, map_id):
        map_id = str(map_id)
        name = cls.maps[map_id][NAME]
        ts = '\\'.join((MAIN_PATH, cls.maps[map_id][TS]))
        npc = []
        for p in list(cls.maps[map_id][NPCS]):
            npc.append(
                NPC(p[0], p[1])
            )
        col = numpy.transpose(
            numpy.array(
                list(cls.maps[map_id][COLLISION])
            )
        )
        shape_z0 = numpy.array(list(cls.maps[map_id][SHAPE_Z0]))
        shape_z1 = numpy.array(list(cls.maps[map_id][SHAPE_Z1]))
        return MapData(name, ts, npc, col, shape_z0, shape_z1)
