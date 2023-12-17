import numpy
import pygame

TILES_SIZE = 64


class TileSet:
    def __init__(self, file, size=(TILES_SIZE, TILES_SIZE), margin=2, spacing=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file: {self.file} tile: {self.size}'


class TileMap:
    def __init__(self, tileset, size=(10, 16), rect=None):
        self.size = size
        self.tileset = tileset
        self.map = numpy.zeros(size, dtype=int)

        h, w = self.size
        self.image = pygame.Surface((TILES_SIZE * w, TILES_SIZE * h))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()

    def render(self):
        display = pygame.display.get_surface()  # surface principal
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                display.blit(tile, (j * TILES_SIZE, i * TILES_SIZE))

    def set_zero(self):
        """
        For debugging purposes only
        """
        self.map = numpy.zeros(self.size, dtype=int)

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'
