import logging

import pygame
from pygame import FULLSCREEN
from pygame.display import set_icon, set_caption, set_mode, flip, Info as get_screen_info

from file_system import FileSystem, ICON_PATH
from settings import (GAME_NAME, LOADING_ST, PAUSED_ST)
from special import Size
from ui import UI


# Display settings
SCALE = 0.7  # the game window will occupy this percent of the screen


class Display:
    def __init__(self):

        screen_info = get_screen_info()
        self.__screen_size = screen_info.current_w, screen_info.current_h
        self.__w_min_width = int(self.__screen_size[0] * SCALE)
        self.__w_min_height = int(self.__w_min_width * SCALE)
        self.__current_size = Size(self.__w_min_width, self.__w_min_height)
        self.__WINDOWED_SIZE = self.__current_size
        self.__fullscreen = False
        logging.info(
            f'Screen size: {self.__screen_size}. Game display size: {self.__current_size.width, self.__current_size.height}'
        )
        self.__canvas = set_mode(self.__current_size, False)
        self.__ui = UI(self)
        set_icon(FileSystem.load_image(ICON_PATH))
        set_caption(GAME_NAME)

    @property
    def width(self):
        return self.__current_size.width

    @property
    def height(self):
        return self.__current_size.height

    @property
    def size(self):
        return self.__current_size

    @property
    def canvas(self):
        return self.__canvas

    def update(self, game):
        self.__background()
        set_caption(f'{GAME_NAME} | {game.fps} FPS')
        if game.status not in (LOADING_ST, PAUSED_ST):
            self.__draw(game)
        self.__ui.update(game)
        flip()

    def fullscreen(self):
        if self.__fullscreen:
            new_size = self.resize(self.__WINDOWED_SIZE)
        else:
            new_size = self.resize((0, 0), True)
        self.__fullscreen = not self.__fullscreen
        return new_size

    def resize(self, new_size: tuple, full_screen=False):
        logging.info('Updating display size')
        if full_screen:
            logging.info(f'Going full screen: {self.__screen_size}')
            set_mode(new_size, FULLSCREEN)
        else:
            logging.info(f'New display size in windowed mode: {new_size}')
            set_mode(new_size)
        self.__current_size = new_size
        return new_size

    def __draw(self, game):
        map_obj = game.map.render()
        self.__canvas.blit(map_obj, (-game.camera.x, -game.camera.y))

    def __background(self, color='black'):
        self.__canvas.fill(color)
