from constants import MAIN_PATH, W_MIN_WIDTH, W_MIN_HEIGHT, TILES_SIZE
from tiles import TileSet, TileMap


def load_map_data(map_id):
    if map_id == 0:  # test map, for debug purposes only
        ts = TileSet(f'{MAIN_PATH}\\resources\\test_tileset.png')
        ts.load()
        tile_map = TileMap(ts, (int(W_MIN_WIDTH / TILES_SIZE), int(W_MIN_HEIGHT / TILES_SIZE)))
        tile_map.set_zero()
        return tile_map


class Map:
    def __init__(self, map_id, npc_list):
        self.__tile_map = load_map_data(map_id)
        self.__npc_list = npc_list
        
    @property
    def size(self):
        pos = self.__tile_map.size
        return pos[1] - 1, pos[0] - 1  # I accidentally inverted the x and y in the game logic... sorry about that :P
    
    @property
    def npc(self):
        return self.__npc_list
    
    @property
    def tile_map(self):
        return self.__tile_map
