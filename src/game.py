import logging

import pygame

from character import Player, NPC
from constants import FRAME_RATE, TILES_SIZE
from display import Display
from map import Map
from src.camera import Camera


class Game:
    def __init__(self):
        logging.info('Game is initializing')
        pygame.init()
        self.running = False
        self.pause = None
        self.clock = pygame.time.Clock()
        self.active_keys = set()
        self.display = Display()
        self.player = Player((8, 5), 'Player', TILES_SIZE, (255, 255, 255))
        self.camera = Camera(self.display.width, self.display.height, self.player)
        self.current_map = Map(0, [
            NPC(2, (3, 4), 'NPC', 12, 12)
        ])
        logging.info('The game is now ready to start running')
    
    def loop(self):
        self.running = True
        logging.info('Game is running')
        while self.running:
            self.events()
            if not self.pause:
                self.update()
                self.display.draw(self.current_map, self.player, self.camera)
            self.clock.tick(FRAME_RATE)
        logging.info('The game stopped running')
    
    def stop(self):
        logging.info('Stopping game')
        self.running = False
    
    def update(self):
        for char in [self.player] + self.current_map.npc_list:
            char.move(self.current_map)
        self.camera.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info('An event to QUIT has been started')
                self.stop()
            elif event.type == pygame.KEYDOWN:
                self.active_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                self.active_keys.discard(event.key)
        self.keyboard_events()
    
    def keyboard_events(self):
        if self.player.speed == (0, 0) and not self.pause:
            if pygame.K_RIGHT in self.active_keys:
                step = (1, 0)
            elif pygame.K_LEFT in self.active_keys:
                step = (-1, 0)
            elif pygame.K_UP in self.active_keys:
                step = (0, -1)
            elif pygame.K_DOWN in self.active_keys:
                step = (0, 1)
            else:
                step = (0, 0)
            self.player.step(step, self.current_map.matrix)
        if pygame.K_ESCAPE in self.active_keys:
            self.pause = True
        else:
            self.pause = False
