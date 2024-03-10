"""Module to represent a generic character."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pygame import Vector2, Rect
from pygame.sprite import Group as SpritesGroup

from settings import TILES_SIZE, WALK_SPEED, RUN_SPEED, DOWN_VECTOR, RIGHT_VECTOR, LEFT_VECTOR, UP_VECTOR
from sprite import AnimatedSprite
from .game_object import GameObject

if TYPE_CHECKING:
    from map import Map


def can_step_in(destiny, collisions):
    if ((destiny[0] in range(collisions.shape[0]) and destiny[1] in range(collisions.shape[1])) and
            collisions[destiny[0], destiny[1]] == 0):
        return True


class Entity(GameObject):
    """Represents a generic character. Should not be used, but its subclasses"""

    def __init__(self, char_id, pos, name, sprite, *groups: SpritesGroup):
        sprite = AnimatedSprite(sprite)
        rect = Rect(pos[0] * TILES_SIZE, pos[1] * TILES_SIZE, sprite.width, sprite.height)
        super().__init__(pos, sprite, rect, *groups)
        self._name = name
        self._id = char_id
        self._speed = 0
        self.__running = False
        self._blocked = False  # avoids movement and facing change while the character is interacting with something

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, new_value):
        self.__running = new_value

    def block(self):
        """Avoids the character moving away while being interacted with"""
        self._blocked = True

    def release(self):
        """Lets the character move freely again after being interacted with"""
        self._blocked = False

    def __collide(self, direction: Vector2, map_info: Map):
        """Returns True if the character is colliding"""
        new_pos = self._grid_pos + direction
        return map_info.collisions[int(new_pos.x), int(new_pos.y)] == 1

    def __update_grid_pos(self, map_info: Map, direction: Vector2):
        map_info.collisions[self.gridx, self.gridy] = 0
        self._grid_pos += direction
        map_info.collisions[self.gridx, self.gridy] = 1

    def __move(self, player_input: Vector2):
        """Updates the X and Y values of the character to match the grid coordinates"""
        if abs(self.gridx * TILES_SIZE - self.coord.x) > WALK_SPEED:  # LEFT & RIGHT
            if self.gridx * TILES_SIZE > self.coord.x:
                direction = RIGHT_VECTOR
            else:
                direction = LEFT_VECTOR
        elif abs(self.gridy * TILES_SIZE - self.coord.y) > WALK_SPEED:  # UP & DOWN
            if self.gridy * TILES_SIZE < self.coord.y:
                direction = UP_VECTOR
            else:
                direction = DOWN_VECTOR
        else:  # NOT MOVING
            self._sprite.update(player_input)
            self._speed = 0
            self.coord = Vector2(self.gridx * TILES_SIZE, self.gridy * TILES_SIZE)
            return
        # APPLY CHANGES
        self.coord += direction * self._speed
        self._sprite.update(direction)

    def update(self, map_info: Map, direction: Vector2):
        if self._blocked:
            return
        if self._speed == 0 and not self.__collide(direction, map_info):
            self.__update_grid_pos(map_info, direction)
            self._speed = RUN_SPEED if self.__running is True else WALK_SPEED
        self.__move(direction)
