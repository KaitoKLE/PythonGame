from constants import TILES_SIZE


class Character:
    def __init__(self, pos, name, sprite):
        self.name = name
        self.__pos = list(pos)
        self.__speed = [0, 0]
        self._x = 0
        self._y = 0
        self.sprite_data = sprite
    
    @property
    def col(self):
        return self.__pos[0]
    
    @col.setter
    def col(self, new_x):
        self.__pos[0] = new_x
    
    @property
    def row(self):
        return self.__pos[1]
    
    @row.setter
    def row(self, new_y):
        self.__pos[1] = new_y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, new_value):
        self.__speed = list(new_value)

    # def move(self):
    #     self.__pos[0] += self.dx
    #     self.__pos[1] += self.dy
