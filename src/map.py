from constants import MAIN_PATH
from tiles import TileSet, TileMap


def load_tile_map(tile_map_id):
    if tile_map_id == 0:  # test map, for debug purposes only
        ts = TileSet(f'{MAIN_PATH}\\resources\\test_tileset.png')
        ts.load()
        tile_map = TileMap(ts)
        tile_map.set_zero()
        return tile_map


class Map:
    def __init__(self, tile_map_id, npc_list):
        self.tile_map = load_tile_map(tile_map_id)
        self.npc_list = npc_list
