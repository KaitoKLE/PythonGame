import random

from pygame import Vector2
from pygame.sprite import Group as SpritesGroup

from game_objects.entity import Entity
from settings.constants import STAY_VECTOR


class NPC(Entity):
    def __init__(self, char_id, pos, name, sprite, *groups: SpritesGroup):
        super().__init__(char_id, pos, name, sprite, *groups)
        self.__m_cooldown = 0
        self.__following = None

    @property
    def following(self):
        return self.following

    @following.setter
    def following(self, new_value):
        self.__following = new_value

    def __random_move(self):
        options = (-1, 0, 1)
        if random.choice((True, False)):
            direction = Vector2(random.choice(options), 0)
        else:
            direction = Vector2(0, random.choice(options))
        self.__m_cooldown = random.randint(1, 500)
        return direction

    def update(self, map_info, direction):
        if self._blocked:
            return
        if self.__m_cooldown < 1:
            direction = self.__random_move()
        else:
            direction = STAY_VECTOR
        self.__m_cooldown -= 1
        super().update(map_info, direction)
