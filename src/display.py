import logging

import pygame
import pygame.gfxdraw

from constants import MAIN_PATH, W_MIN_WIDTH, W_MIN_HEIGHT


class Display:
    def __init__(self):
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

    def draw(self, map_to_draw, player):
        self.canvas.blit(map_to_draw.tile_map.image, (0, 0))
        for npc in map_to_draw.npc_list:
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
        character.sprite.sprite = pygame.draw.rect(
            self.canvas, character.sprite.color, (character.x, character.y, character.sprite.size,
                                                  character.sprite.size))


