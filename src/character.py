import time

from src.constants import TILES_SIZE, MOV_SPEED
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

    def move(self, map_size):
        self.constraint(map_size)
        # LEFT & RIGHT
        if self.col * TILES_SIZE > self.__xy[0] and abs(self.col * TILES_SIZE - self.__xy[0]) > MOV_SPEED:
            self.__speed = (MOV_SPEED, 0)
        elif self.col * TILES_SIZE < self.__xy[0] and abs(self.col * TILES_SIZE - self.__xy[0]) > MOV_SPEED:
            self.__speed = (-MOV_SPEED, 0)
        # UP & DOWN
        elif self.row * TILES_SIZE < self.__xy[1] and abs(self.row * TILES_SIZE - self.__xy[1]) > MOV_SPEED:
            self.__speed = (0, -MOV_SPEED)
        elif self.row * TILES_SIZE > self.__xy[1] and abs(self.row * TILES_SIZE - self.__xy[1]) > MOV_SPEED:
            self.__speed = (0, MOV_SPEED)
        # NOT MOVING
        else:
            self.__speed = (0, 0)
            self.__xy = [self.col * TILES_SIZE, self.row * TILES_SIZE]
        # APPLY CHANGES
        self.__xy[0] += self.__speed[0]
        self.__xy[1] += self.__speed[1]
    
    def constraint(self, map_size):
        if self.col > map_size[0]:
            self.col = map_size[0]
        if self.col < 0:
            self.col = 0
        if self.row > map_size[1]:
            self.row = map_size[1]
        if self.row < 0:
            self.row = 0
