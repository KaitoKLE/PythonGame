import pygame

from constants import TILES_SIZE, MAIN_PATH


class TileSet:
    def __init__(self, file_path, size=(TILES_SIZE, TILES_SIZE), margin=0, spacing=0):
        self.tiles = []
        image = pygame.image.load(file_path)
        rect = image.get_rect()
        x0 = y0 = margin
        w, h = rect.size
        dx = size[0] + spacing
        dy = size[1] + spacing
        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(size)
                tile.blit(image, (0, 0), (x, y, *size))
                self.tiles.append(tile)


class TileMap:
    def __init__(self, tile_set_path, map_):
        self.size = map_.shape
        self.tile_set = TileSet(tile_set_path)
        self.map = map_
        self.image = pygame.Surface((TILES_SIZE * self.size[1], TILES_SIZE * self.size[0]))
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tile_set.tiles[self.map[i, j]]
                self.image.blit(tile, (j * TILES_SIZE, i * TILES_SIZE))
