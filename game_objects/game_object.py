from pygame import Rect, Surface, Vector2
from pygame.sprite import Sprite, Group as SpritesGroup

from display.sprite import AnimatedSprite
from engine.special import Position


class GameObject(Sprite):
    def __init__(self, pos, sprite, rect: Rect, *groups: SpritesGroup):
        if not isinstance(sprite, (Surface, Sprite, AnimatedSprite)):
            raise TypeError(f'Inappropriate argument type for {GameObject.__class__}: {type(sprite)}')
        super().__init__(*groups)
        self._grid_pos = Position(*pos)
        self._sprite = sprite
        self._rect = rect

    @property
    def gridx(self):
        """Position X of the character in the GRID"""
        return int(self._grid_pos.x)

    @property
    def gridy(self):
        """Position Y of the character in the GRID"""
        return int(self._grid_pos.y)

    @property
    def grid_position(self):
        return self._grid_pos

    @property
    def coord(self):
        """
        Returns a Vector2 with the (X, Y) position of the character in the current map
        WARNING: Vector2 values are FLOAT, NOT INT
        """
        return Vector2(self._rect.x, self._rect.y)

    @coord.setter
    def coord(self, new_value: Vector2):
        """
        Receives a Vector2 and updates the rect with the new location
        """
        self._rect.x = new_value.x
        self._rect.y = new_value.y

    @property
    def image(self) -> Surface:
        """
        Returns the sprite the character is currently drawing. Mostly used internally by pygame
        WARNING: DO NOT REMOVE NOR RENAME THIS PROPERTY
        """
        return self._sprite.frame

    @property
    def rect(self):
        """
        Returns the rect of the character's sprite. Mostly used internally by pygame
        WARNING: DO NOT REMOVE NOR RENAME THIS PROPERTY
        """
        return self._rect
