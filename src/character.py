import random

import pygame.image

from constants import TILES_SIZE, MOV_SPEED


class Character:
    def __init__(self, char_id, pos, name):
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
    
    def step(self, steps, collisions):
        x = self.col + steps[0]
        y = self.row + steps[1]
        if x in range(collisions.shape[0]) and y in range(collisions.shape[1]):
            if collisions[x, y] == 0:
                collisions[self.col, self.row] = 0
                self.__pos[0] += steps[0]
                self.__pos[1] += steps[1]
                collisions[self.col, self.row] = self.id
    
    def update(self, map_info):
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


class Player(Character):
    def __init__(self, pos, name):
        super().__init__(1, pos, name)


class NPC(Character):
    def __init__(self, char_id, pos):
        super().__init__(char_id, pos, f'NPC {char_id}')
        self.__m_cooldown = 0
    
    def step(self, steps, collisions):
        options = (-1, 0, 1)
        if random.choice((True, False)):
            steps = (random.choice(options), 0)
        else:
            steps = (0, random.choice(options))
        super().step(steps, collisions)
    
    def update(self, map_info):
        if self.speed == (0, 0) and self.__m_cooldown < 1:
            self.step(None, map_info.collisions)
            self.__m_cooldown = random.randint(1, 500)
        self.__m_cooldown -= 1
        super().update(map_info)
