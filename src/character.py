import time

from src.constants import TILES_SIZE
from src.sprite import Sprite


class Character:
    def __init__(self, pos, name, size, color):
        self.name = name
        self.__pos = list(pos)
        self.__xy = [pos[0] * TILES_SIZE, pos[1] * TILES_SIZE]
        self.__speed = (0, 0)
        self.dx = 0
        self.dy = 0
        self.sprite = Sprite(size, color)
    
    @property
    def col(self):
        return self.__pos[0]
    
    @col.setter
    def col(self, value):
        self.__pos = [value, self.row]
    
    @property
    def row(self):
        return self.__pos[1]
    
    @row.setter
    def row(self, value):
        self.__pos = [self.col, value]

    @property
    def x(self):
        return self.__xy[0]

    @property
    def y(self):
        return self.__xy[1]
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = tuple(value)

    def move(self):
        pass
