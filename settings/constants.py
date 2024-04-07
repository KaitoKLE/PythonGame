"""
Settings file for project.
"""
from os.path import dirname
from sys import path as syspath
from pygame.constants import *
from pygame import Vector2

# add engine path to the python path
# syspath.append(dirname(dirname(__file__)))

# Game settings
# VERSION = 1.5
# GAME_NAME = f'PythonGame v{VERSION} BETA'
WALK_SPEED = 4
RUN_SPEED = WALK_SPEED * 4
FRAME_RATE = 60
TIME_SPEED = 10  # x times slower/faster than real time

# Game statuses
STOPPING_ST = 0
PLAYING_ST = 1
PAUSED_ST = 2
LOADING_ST = 3

# Keyboard settings
ACTION_KEY = K_c
BACK_KEY = K_x
RUN_KEY = K_LSHIFT
MENU_KEY = K_SPACE
DOWN_KEY = K_DOWN
RIGHT_KEY = K_RIGHT
LEFT_KEY = K_LEFT
UP_KEY = K_UP
FULL_SCREEN = K_DELETE
EXIT_KEY = K_ESCAPE

# Some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
GREY_LIGHT = (100, 100, 100)
GREY_DARK = (40, 40, 40)
CYAN = (0, 255, 255)
BROWN = (165, 42, 42)
DEFAULT_COLOR_KEY = -1  # (180, 30, 190)  # some purple color :D This is for sprites and images transparency

# TileSet and TileMap settings
TILES_SIZE = 64

# DIRECTION VECTORS
RIGHT_VECTOR = Vector2(1, 0)
LEFT_VECTOR = Vector2(-1, 0)
UP_VECTOR = Vector2(0, -1)
DOWN_VECTOR = Vector2(0, 1)
STAY_VECTOR = Vector2()
