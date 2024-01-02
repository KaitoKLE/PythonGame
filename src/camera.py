from pygame import Rect

from constants import TILES_SIZE


class Camera:
    """Follows the player in the center of the actual display"""
    def __init__(self, w, h, character):
        self.__rect = Rect(character.x, character.y, w, h)
        self.__focus = character
    
    @property
    def x(self):
        return self.__rect.x - TILES_SIZE / 2
    
    @property
    def y(self):
        return self.__rect.y - TILES_SIZE / 2
    
    def update(self):
        self.__rect.x = -(self.__focus.x - self.__rect.width / 2)
        self.__rect.y = -(self.__focus.y - self.__rect.height / 2)
    
    def focus(self, character):
        self.__focus = character
        self.update()
