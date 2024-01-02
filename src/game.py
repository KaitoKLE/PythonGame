import logging

import pygame

from character import Player
from constants import FRAME_RATE, GAME_NAME
from display import Display
from map import Map
from src.camera import Camera


class Game:
    """Overall class to manage game behavior."""
    def __init__(self):
        """Initialize the game."""
        logging.info(f'{GAME_NAME} is initializing')
        pygame.init()
        self.running = False
        self.pause = None
        self.clock = pygame.time.Clock()
        self.active_keys = set()
        self.display = Display()
        self.player = Player((8, 5), 'Player')
        self.camera = Camera(self.display.width, self.display.height, self.player)
        self.current_map = Map(0)
        logging.info('The game is now ready to start running')
    
    def loop(self):
        """Start the main loop for the game."""
        self.running = True
        logging.info(f'{GAME_NAME} is running')
        while self.running:
            self.events()
            if not self.pause:
                self.update()
                self.display.draw(self.current_map, self.player, self.camera)
            self.clock.tick(FRAME_RATE)
        logging.info(f'{GAME_NAME} stopped running')
    
    def stop(self):
        """Stop the main loop for the game."""
        logging.info(f'Stopping {GAME_NAME}')
        self.running = False
    
    def update(self):
        """Update environment variables"""
        for char in [self.player] + self.current_map.npc_list:
            char.update(self.current_map)
        self.camera.update()
    
    def events(self):
        """Checks for game events"""
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
        """Checks for keyboard events"""
        # if pygame.K_j in self.active_keys:
        #     self.camera.focus(self.current_map.npc_list[1])
        # if pygame.K_k in self.active_keys:
        #     self.camera.focus(self.player)
        self.__directional_input()
        if pygame.K_ESCAPE in self.active_keys:
            self.pause = True
        else:
            self.pause = False
    
    def __directional_input(self):
        """Checks for keyboard input for player movement"""
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
                return
            self.player.step(step, self.current_map.collisions)
