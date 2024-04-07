from pygame import Vector2
from pygame.sprite import Group as SpritesGroup

from game_objects.entity import Entity
from settings.constants import TILES_SIZE
from settings.paths import PLAYER_SPRITE


class Player(Entity):
    def __init__(self, name, *groups: SpritesGroup):
        super().__init__(1, (0, 0), name, PLAYER_SPRITE, *groups)

    def spawn(self, pos):
        self._grid_pos = Vector2(pos)
        self._rect.topleft = self._grid_pos * TILES_SIZE
