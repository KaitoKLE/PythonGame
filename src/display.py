import logging

import pygame
import pygame.gfxdraw

from constants import MAIN_PATH, W_MIN_WIDTH, W_MIN_HEIGHT
from tiles import TileSet, TileMap


def detect_collisions(ch1, ch2):
    prev_movement_dir = (ch1.dx, ch1.dy)
    c1_rect = pygame.Rect(ch1.x, ch1.y, ch1.sprite_data.size, ch1.sprite_data.size)
    c2_rect = pygame.Rect(ch2.x, ch2.y, ch2.sprite_data.size, ch2.sprite_data.size)
    if c1_rect.colliderect(c2_rect):
        ch1.dx = 0
        ch1.dy = 0
        if prev_movement_dir[0] < 0:  # left
            c1_rect.move_ip(5, 0)
        elif prev_movement_dir[0] > 0:  # right
            c1_rect.move_ip(-5, 0)
        if prev_movement_dir[1] < 0:  # up
            c1_rect.move_ip(0, 5)
        elif prev_movement_dir[1] > 0:  # down
            c1_rect.move_ip(0, -5)
        return c1_rect.x, c1_rect.y


class Display:
    def __init__(self, game):
        # DEBUG MAP
        ts = TileSet(f'{MAIN_PATH}\\resources\\test_tileset.png')
        ts.load()
        self.tile_map = TileMap(ts)
        self.tile_map.set_zero()
        self.width = W_MIN_WIDTH
        self.height = W_MIN_HEIGHT
        self.canvas = pygame.display.set_mode((self.width, self.height), False)
        try:
            pygame.display.set_icon(
                pygame.image.load(f'{MAIN_PATH}/resources/icon.png')
            )
        except (FileNotFoundError, IOError, PermissionError) as e:
            logging.error(f'Cannot load the image file: {e}')
        pygame.display.set_caption('Python game')

    @property
    def center(self):
        return int(self.width / 2), int(self.height / 2)

    def draw(self, npcs, player):
        self.tile_map.render()
        for npc in npcs:
            self.draw_character(npc)
        self.draw_character(player)
        pygame.display.flip()

    def background(self, color):
        pygame.draw.rect(self.canvas, color, (0, 0, self.width, self.height))

    def update_size(self, new_w, new_h):
        logging.info('Updating display size...')
        self.canvas = pygame.display.set_mode((new_w, new_h), False)
        self.width = new_w
        self.height = new_h

    def draw_character(self, character):
        character.sprite_data.sprite = pygame.draw.rect(
            self.canvas, character.sprite_data.color, (character.x, character.y, character.sprite_data.size,
                                                       character.sprite_data.size))


class Sprite:
    def __init__(self, size, look, color, path):
        self.size = size
        self.looking_at = look
        self.color = color
        self.sprite = pygame.image.load(path)
