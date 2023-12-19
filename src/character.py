class Character:
    def __init__(self, pos, name, sprite):
        self.name = name
        self.__pos = list(pos)
        self.dx = 0
        self.dy = 0
        self.sprite_data = sprite

    @property
    def x(self):
        return self.__pos[0]

    @x.setter
    def x(self, new_x):
        self.__pos[0] = new_x

    @property
    def y(self):
        return self.__pos[1]

    @y.setter
    def y(self, new_y):
        self.__pos[1] = new_y

    def move(self):
        self.__pos[0] += self.dx
        self.__pos[1] += self.dy
