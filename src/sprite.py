import logging

from numpy import array
from pygame import Vector2, Rect, Surface, SRCALPHA, RLEACCEL, transform, time

from file_system import FileSystem
from settings import DEFAULT_COLOR_KEY, TILES_SIZE, STAY_VECTOR
from special import Size

# DEFAULT SPRITE_SHEET PROPERTIES
DEFAULT = {
    'n_rows': 4,
    'n_cols': 3,
}

# ANIMATIONS KEYS
WALK_DOWN = 'walk_down'
WALK_RIGHT = 'walk_right'
WALK_LEFT = 'walk_left'
WALK_UP = 'walk_up'

# WALKING ANIMATION STAGES
SPRITE_STEP_LEFT = 0
SPRITE_STANDING = 1
SPRITE_STEP_RIGHT = 2
WALKING_ANIM = (SPRITE_STEP_LEFT, SPRITE_STANDING, SPRITE_STEP_RIGHT, SPRITE_STANDING)
WALKING_ANIM_LENGTH = len(WALKING_ANIM)


class AnimatedSprite:
    def __init__(self, path):
        sprite_sheet = SpriteSheet(path)
        self.__current_animation = WALK_DOWN
        self.__frames = {
            WALK_DOWN: sprite_sheet.sprites_at((
                (0, 0), (1, 0), (2, 0)
            )),
            WALK_RIGHT: sprite_sheet.sprites_at((
                (0, 2), (1, 2), (2, 2)
            )),
            WALK_LEFT: sprite_sheet.sprites_at((
                (0, 1), (1, 1), (2, 1)
            )),
            WALK_UP: sprite_sheet.sprites_at((
                (0, 3), (1, 3), (2, 3)
            ))
        }
        self.__frame = self.__frames[WALK_DOWN][SPRITE_STANDING]

    @property
    def frame(self):
        return self.__frame

    @property
    def width(self):
        return self.__frame.get_width()

    @property
    def height(self):
        return self.__frame.get_height()

    def update(self, direction: Vector2, speed=4):
        delta = int(time.get_ticks() / (speed*250) * WALKING_ANIM_LENGTH)
        frame = delta % WALKING_ANIM_LENGTH if direction != STAY_VECTOR else 1
        anim = self.__detect_facing(direction)
        self.__frame = self.__frames[anim][WALKING_ANIM[frame]]
        self.__current_animation = anim

    def __detect_facing(self, direction):
        if direction.y > 0:
            anim = WALK_DOWN
        elif direction.x > 0:
            anim = WALK_RIGHT
        elif direction.x < 0:
            anim = WALK_LEFT
        elif direction.y < 0:
            anim = WALK_UP
        else:
            anim = self.__current_animation
        return anim


class SpriteSheet:
    """Represents a set of sprites."""

    def __init__(self, key):
        """Load the sheet."""
        self.__image, properties = FileSystem.load_sprite(key)
        self.__n_rows = properties.get('n_rows', DEFAULT['n_rows'])
        self.__n_cols = properties.get('n_cols', DEFAULT['n_cols'])
        self.__frames_size = Size(self.__image.get_width() / self.__n_cols, self.__image.get_height() / self.__n_rows)

    def sprite_at(self, pos, sprite_size=(TILES_SIZE, TILES_SIZE), color_key=DEFAULT_COLOR_KEY):
        """Load a specific image from a specific (x, y) position."""
        rect = Rect(pos[0] * sprite_size[0], pos[1] * sprite_size[1], sprite_size[0], sprite_size[1])
        image = Surface(rect.size, SRCALPHA)
        image.blit(self.__image, (0, 0), rect)
        image.set_colorkey(color_key, RLEACCEL)
        image.convert()
        if self.__frames_size.width != TILES_SIZE or self.__frames_size.height != TILES_SIZE:
            image = transform.scale(image, (TILES_SIZE, TILES_SIZE))
        return image

    def sprites_at(self, positions, colorkey=DEFAULT_COLOR_KEY):
        """Load a bunch of images and return them as a list."""
        return [self.sprite_at(pos, self.__frames_size, colorkey) for pos in positions]

    def all_sprites(self):
        """Load a grid of images."""
        sprites = []
        for row in range(self.__n_rows):
            sprites_pos = []
            for col in range(self.__n_cols):
                sprites_pos.append((col, row))
            sprites.append(self.sprites_at(sprites_pos))
        return array(sprites)
