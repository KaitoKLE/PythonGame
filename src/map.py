import numpy

from src.data_manager import DataManager
from tiles import TileMap


class Map:
    def __init__(self, map_id):
        map_data = DataManager.get_map_data(map_id)
        self.__tile_map = TileMap(map_data.tile_set_path, map_data.map_shape)
        self.__collisions = map_data.collision
        self.__npc_list = map_data.npc
    
    @property
    def npc_list(self):
        return self.__npc_list
    
    @property
    def image(self):
        return self.__tile_map.image
    
    @property
    def collisions(self):
        return self.__collisions
