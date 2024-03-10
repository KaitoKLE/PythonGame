from pygame import Rect, Surface, time
from pygame.mouse import get_pos
from source.sprite import SpriteSheet
from source.file_system import MOUSE_SPRITE

MOUSE_ANIM_LENGTH = 2


class MouseCursor:
    def __init__(self):
        sprite_sheet = SpriteSheet(MOUSE_SPRITE)
        self.__current_animation = 0
        self.__frames: list = [sprite_sheet.sprite_at((0, 0)), sprite_sheet.sprite_at((1, 0))]
        self._sprite: Surface = self.__frames[0]
        self._rect = Rect(0, 0, *self._sprite.get_size())

    @property
    def image(self):
        return self._sprite

    @property
    def pos(self):
        return self._rect.topleft

    def update(self, speed=4):
        self._rect.center = get_pos()
        delta = int(time.get_ticks() / (speed * 250) * MOUSE_ANIM_LENGTH)
        frame = delta % MOUSE_ANIM_LENGTH
        self._sprite = self.__frames[frame]
