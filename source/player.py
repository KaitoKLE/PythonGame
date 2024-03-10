from pygame import Vector2
from pygame.sprite import Group as SpritesGroup

from source.entity import Entity
from source.settings import TILES_SIZE
from source.file_system import PLAYER_SPRITE


class Player(Entity):
    def __init__(self, name, *groups: SpritesGroup):
        super().__init__(1, (0, 0), name, PLAYER_SPRITE, *groups)

    def spawn(self, pos):
        self._grid_pos = Vector2(pos)
        self._rect.topleft = self._grid_pos * TILES_SIZE
