from os.path import dirname

MAIN_PATH = dirname(dirname(__file__))
PLAYER_SPRITE = f'{MAIN_PATH}/resources/icon.png'

# Game settings
MOV_SPEED = 3
DEFAULT_FRAME_RATE = 60

# Display settings
W_MIN_WIDTH = 1024
W_MIN_HEIGHT = 640
POINTER_DEFAULT_SIZE = 25

# TileSet and TileMap settings
TILES_SIZE = 64

# Looking at
LOOKING_DOWN = 2
LOOKING_UP = 8
LOOKING_LEFT = 4
LOOKING_RIGHT = 6
