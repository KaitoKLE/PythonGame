from numpy import array, transpose
from pygame import Surface, SRCALPHA
from pygame.sprite import Group as SpritesGroup

from engine.data_manager import DataManager
from engine.file_system import FileSystem
from game_objects.npc import NPC
from settings.constants import TILES_SIZE
from engine.special import Position


def scan_tile_set(file_path, size=(TILES_SIZE, TILES_SIZE), margin=0, spacing=0):
    tiles = []
    image = FileSystem.load_image(file_path, scale=2)
    rect = image.get_rect()
    x0 = y0 = margin
    w, h = rect.size
    dx = size[0] + spacing
    dy = size[1] + spacing
    for x in range(x0, w, dx):
        for y in range(y0, h, dy):
            tile = Surface(size, SRCALPHA)
            tile.blit(image, (0, 0), (x, y, *size))
            tiles.append(tile)
    return tiles


class Map:
    def __init__(self, map_id):
        map_data = DataManager.get_map_data(map_id)
        self.__all_characters = SpritesGroup()
        self.__npcs = SpritesGroup()
        self.__size_grid = map_data.map_size
        self.__image = Surface((self.__size_grid[1] * TILES_SIZE, self.__size_grid[0] * TILES_SIZE), SRCALPHA)
        self.__collisions = []
        self.__player_spawn = Position(*map_data.player_spawn)
        self.__put_npcs(map_data.npc_locations)
        self.__build(scan_tile_set(map_data.ts_path), map_data.layers)

    @property
    def all_characters(self):
        return self.__all_characters

    @property
    def player_spawn(self):
        return self.__player_spawn

    @property
    def collisions(self):
        return self.__collisions

    def __put_npcs(self, npcs: list):
        for npc in npcs:
            npc_id = npc[0]
            start_pos_grid = npc[1]
            name, sprite_sheet = DataManager.get_npc_data(npc_id)
            NPC(npc_id, start_pos_grid, name, sprite_sheet, self.__npcs, self.__all_characters)

    def __build(self, tile_set, layers):
        empty_tile = Surface((TILES_SIZE, TILES_SIZE), SRCALPHA)
        for i in range(self.__size_grid[0]):
            row = []
            for j in range(self.__size_grid[1]):
                tile = (tile_set[layers[0][i, j]] if layers[0][i, j] != -1 else empty_tile).copy()
                if layers[1][i, j] != -1:
                    tile.blit(tile_set[layers[1][i, j]], (0, 0))
                    row.append(1)
                else:
                    row.append(0)
                self.__image.blit(tile, (j * TILES_SIZE, i * TILES_SIZE))
            self.__collisions.append(row)
        self.__collisions = transpose(array(self.__collisions))
        self.__collisions[int(self.__player_spawn.x), int(self.__player_spawn.y)] = 1  # player collision

    def render(self):
        surface = self.__image.copy()
        self.all_characters.draw(surface)
        return surface
