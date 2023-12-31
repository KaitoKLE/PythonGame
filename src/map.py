import numpy

from constants import MAIN_PATH
from tiles import TileSet, TileMap


def load_map_data(map_id):
    if map_id == 0:  # test map, for debug purposes only
        ts = TileSet(f'{MAIN_PATH}\\resources\\test_tileset.png')
        tile_map = TileMap(ts, (14, 20))
        return tile_map


class Map:
    def __init__(self, map_id, npc_list):
        tile_map = load_map_data(map_id)
        self.__image = tile_map.image
        self.__size = tile_map.size[1] - 1, tile_map.size[0] - 1
        self.__matrix = numpy.zeros((tile_map.size[1], tile_map.size[0]))
        self.__npc_list = npc_list
    
    @property
    def npc_list(self):
        return self.__npc_list
    
    @property
    def image(self):
        return self.__image
    
    @property
    def size(self):
        return self.__size
    
    @property
    def matrix(self):
        return self.__matrix
