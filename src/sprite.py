import pygame


class Sprite:
    def __init__(self, size, look, color, path):
        self.size = size
        self.looking_at = look
        self.color = color
        self.sprite = pygame.image.load(path)
