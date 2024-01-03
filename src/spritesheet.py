"""Module to represent a sprite sheet, and individual sprites."""
import logging

import pygame

from src.constants import TILES_SIZE, DEFAULT_COLOR_KEY

# LOOKING AT
FACING_DOWN = 0
FACING_RIGHT = 1
FACING_LEFT = 2
FACING_UP = 3

# WALKING ANIM
STEPING_LEFT = 0
STATIC = 1
STEPING_RIGHT = 2


class SpriteSheet:
    """Represents a set of sprites."""
    
    def __init__(self, path):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(path).convert()
        except pygame.error as e:
            logging.critical(f"Unable to load sprite sheet image '{path}': {e}")
    
    def image_at(self, pos, colorkey=DEFAULT_COLOR_KEY, sprite_size=TILES_SIZE):
        """Load a specific image from a specific (x, y) position."""
        rect = pygame.Rect(pos[0] * sprite_size, pos[1] * sprite_size, sprite_size, sprite_size)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    def images_at(self, positions, colorkey=DEFAULT_COLOR_KEY, sprite_size=TILES_SIZE):
        """Load a bunch of images and return them as a list."""
        return [self.image_at(pos, colorkey, sprite_size) for pos in positions]
