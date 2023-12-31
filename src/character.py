import random

import pygame.image

from constants import TILES_SIZE, MOV_SPEED


class Character:
    def __init__(self, char_id, pos, name, size, color):
        self.name = name
        self.id = char_id
        self.__pos = list(pos)
        self.__xy = [pos[0] * TILES_SIZE, pos[1] * TILES_SIZE]
        self.__speed = (0, 0)
        self.sprite = pygame.image.load('D:\\Luis Ernesto\\Documentos\\Proyectos\\PythonGame\\resources\\py.png')
    
    @property
    def col(self):
        return self.__pos[0]
    
    @property
    def row(self):
        return self.__pos[1]
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def x(self):
        return self.__xy[0]
    
    @property
    def y(self):
        return self.__xy[1]
    
    @property
    def speed(self):
        return self.__speed
    
    def step(self, steps, matrix):
        try:
            if matrix[self.col + steps[0]][self.row + steps[1]] == 0:
                matrix[self.col][self.row] = 0
                self.__pos[0] += steps[0]
                self.__pos[1] += steps[1]
                matrix[self.col][self.row] = self.id
        except IndexError:
            pass
    
    def move(self, map_info):
        self.__constraint(map_info.size)
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
    
    def __constraint(self, map_size):
        if self.col > map_size[0]:
            self.__pos[0] = map_size[0]
        if self.col < 0:
            self.__pos[0] = 0
        if self.row > map_size[1]:
            self.__pos[1] = map_size[1]
        if self.row < 0:
            self.__pos[1] = 0


class Player(Character):
    def __init__(self, pos, name, size, color):
        super().__init__(1, pos, name, size, color)


class NPC(Character):
    def __init__(self, char_id, pos, name, size, color):
        super().__init__(char_id, pos, name, size, color)
        self.__m_cooldown = 0
        
    def step(self, steps, matrix):
        options = (-1, 0, 1)
        if random.choice((True, False)):
            steps = (random.choice(options), 0)
        else:
            steps = (0, random.choice(options))
        super().step(steps, matrix)
    
    def move(self, map_info):
        if self.speed == (0, 0) and self.__m_cooldown < 1:
            self.step(None, map_info.matrix)
            self.__m_cooldown = random.randint(1, 500)
        self.__m_cooldown -= 1
        super().move(map_info)
