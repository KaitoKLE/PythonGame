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
                tile = pygame.Surface(size, pygame.SRCALPHA)
                tile.blit(image, (0, 0), (x, y, *size))
                self.tiles.append(tile)


class TileMap:
    def __init__(self, tile_set_path, map_z0, map_z1, map_z2):
        self.size = map_z0.shape
        self.tile_set = TileSet(tile_set_path)
        self.map_z0 = map_z0
        self.map_z1 = map_z1
        self.map_z2 = map_z2
        self.image_z0 = pygame.Surface((TILES_SIZE * self.size[1], TILES_SIZE * self.size[0]), pygame.SRCALPHA)
        self.image_z1 = pygame.Surface((TILES_SIZE * self.size[1], TILES_SIZE * self.size[0]), pygame.SRCALPHA)
        self.image_z2 = pygame.Surface((TILES_SIZE * self.size[1], TILES_SIZE * self.size[0]), pygame.SRCALPHA)
        self.__render()
    
    def __render(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                tile_z0 = self.tile_set.tiles[self.map_z0[i, j]]
                self.image_z0.blit(tile_z0, (j * TILES_SIZE, i * TILES_SIZE))
                tile_z1 = self.tile_set.tiles[self.map_z1[i, j]]
                self.image_z1.blit(tile_z1, (j * TILES_SIZE, i * TILES_SIZE))
                tile_z2 = self.tile_set.tiles[self.map_z2[i, j]]
                self.image_z2.blit(tile_z2, (j * TILES_SIZE, i * TILES_SIZE))
