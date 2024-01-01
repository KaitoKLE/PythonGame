import numpy

from tiles import TileMap


class Map:
    def __init__(self, map_id):
        self.__tile_map = TileMap(map_id, (14, 20))
        self.__collisions = numpy.zeros((self.__tile_map.size[1], self.__tile_map.size[0]))
        self.__npc_list = []
    
    @property
    def npc_list(self):
        return self.__npc_list
    
    @property
    def image(self):
        return self.__tile_map.image
    
    @property
    def collisions(self):
        return self.__collisions
