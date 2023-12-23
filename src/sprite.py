import pygame


class Sprite:
    def __init__(self, size, color):
        self.__size = size
        self.__color = color
        
    @property
    def size(self):
        return self.__size
    
    @property
    def color(self):
        return self.__color
