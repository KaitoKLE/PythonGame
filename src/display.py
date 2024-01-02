import logging

import pygame
import pygame.gfxdraw

from constants import MAIN_PATH, W_MIN_WIDTH, W_MIN_HEIGHT, GAME_NAME
from src.file_scanner import FileScanner


class Display:
    def __init__(self):
        self.width = W_MIN_WIDTH
        self.height = W_MIN_HEIGHT
        self.canvas = pygame.display.set_mode((self.width, self.height), False)
        pygame.display.set_icon(FileScanner.load_image(f'{MAIN_PATH}/resources/icon.png'))
        pygame.display.set_caption(GAME_NAME)

    @property
    def center(self):
        return int(self.width / 2), int(self.height / 2)

    def draw(self, map_to_draw, player, camera):
        self.canvas.fill('black')
        map_obj = map_to_draw.image_z0.copy()
        map_obj.blit(player.sprite, (player.x, player.y))
        for person in [player] + map_to_draw.npc_list:
            map_obj.blit(person.sprite, (person.x, person.y))
        map_obj.blit(map_to_draw.image_z1, (0, 0))
        map_obj.blit(map_to_draw.image_z2, (0, 0))
        self.canvas.blit(map_obj, (camera.x, camera.y))
        pygame.display.flip()

    def background(self, color):
        pygame.draw.rect(self.canvas, color, (0, 0, self.width, self.height))

    def update_size(self, new_w, new_h):
        logging.info('Updating display size...')
        self.canvas = pygame.display.set_mode((new_w, new_h), False)
        self.width = new_w
        self.height = new_h
