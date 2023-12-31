from pygame import Rect


class Camera:
    def __init__(self, w, h, character):
        self.__rect = Rect(character.x, character.y, w, h)
        self.__focus = character
    
    @property
    def x(self):
        return self.__rect.x
    
    @property
    def y(self):
        return self.__rect.y
    
    def update(self):
        self.__rect.x = -(self.__focus.x - self.__rect.width / 2)
        self.__rect.y = -(self.__focus.y - self.__rect.height / 2)
    
    def focus(self, character):
        self.__focus = character
        self.update()
