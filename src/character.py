class Character:
    def __init__(self, pos, sprite):
        self.__pos = list(pos)
        self.dx = 0
        self.dy = 0
        self.col_dx = False
        self.col_dy = False
        self.sprite_data = sprite

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, new_pos):
        self.__pos = new_pos

    @property
    def x(self):
        return self.__pos[0]

    @x.setter
    def x(self, new_x):
        self.pos = [new_x, self.y]

    @property
    def y(self):
        return self.__pos[1]

    @y.setter
    def y(self, new_y):
        self.pos = [self.x, new_y]

    def update(self):
        self.__pos[0] += self.dx
        self.__pos[1] += self.dy
