from src.data_manager import DataManager
from tiles import TileMap


class Map:
    def __init__(self, map_id):
        map_data = DataManager.get_map_data(map_id)
        self.__tile_map = TileMap(
            map_data.tile_set_path,
            map_data.map_shape_z0,
            map_data.map_shape_z1,
            map_data.map_shape_z2
        )
        self.__collisions = map_data.collision
        self.__npc_list = map_data.npc
    
    @property
    def npc_list(self):
        return self.__npc_list
    
    @property
    def image_z0(self):
        return self.__tile_map.image_z0
    
    @property
    def image_z1(self):
        return self.__tile_map.image_z1
    
    @property
    def image_z2(self):
        return self.__tile_map.image_z2
    
    @property
    def collisions(self):
        return self.__collisions
