import logging

import pygame

from character import Character
from display import Display, detect_collisions
from sprite import Sprite
from constants import (LOOKING_DOWN, PLAYER_SPRITE, DEFAULT_FRAME_RATE, MOV_SPEED, LOOKING_RIGHT,
                       LOOKING_LEFT, LOOKING_UP, TILES_SIZE)
from map import Map


class Game:
    def __init__(self):
        logging.info('Game is initializing')
        pygame.init()
        self.running = False
        self.clock = pygame.time.Clock()
        self.active_keys = set()
        self.display = Display()
        self.player = Character((8, 4), 'Player', TILES_SIZE, (255, 255, 255))
        self.current_map = Map(0, [])
        logging.info('The game is now ready to start running')

    def loop(self):
        self.running = True
        logging.info('Game is running')
        while self.running:
            self.events()
            self.update()
            self.display.draw(self.current_map, self.player)
            self.clock.tick(DEFAULT_FRAME_RATE)
        logging.info('The game stopped running')

    def stop(self):
        logging.info('Stopping game')
        self.running = False

    def update(self):
        self.player.move()
        self.constraint(self.player)
        self.process_collisions()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info('An event to QUIT has been started')
                self.stop()
            elif event.type == pygame.KEYDOWN:
                self.active_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                self.active_keys.discard(event.key)
        self.process_keyboard_events()

    def process_keyboard_events(self):
        if self.player.speed == (0, 0):
            if pygame.K_RIGHT in self.active_keys:
                self.player.speed = (MOV_SPEED, 0)
        # if pygame.K_RIGHT in self.active_keys:
        #     self.player.dx = MOVEMENT_DEFAULT_SPEED
        #     self.player.sprite.looking_at = LOOKING_RIGHT
        # elif pygame.K_LEFT in self.active_keys:
        #     self.player.dx = -MOVEMENT_DEFAULT_SPEED
        #     self.player.sprite.looking_at = LOOKING_LEFT
        # else:
        #     self.player.dx = 0
        # if pygame.K_UP in self.active_keys:
        #     self.player.dy = -MOVEMENT_DEFAULT_SPEED
        #     self.player.sprite.looking_at = LOOKING_UP
        # elif pygame.K_DOWN in self.active_keys:
        #     self.player.dy = MOVEMENT_DEFAULT_SPEED
        #     self.player.sprite.looking_at = LOOKING_DOWN
        # else:
        #     self.player.dy = 0

    def constraint(self, character):
        if character.x > self.display.width - character.sprite.size:
            character.x = self.display.width - character.sprite.size
        if character.x < 0:
            character.x = 0
        if character.y > self.display.height - character.sprite.size:
            character.y = self.display.height - character.sprite.size
        if character.y < 0:
            character.y = 0

    def process_collisions(self):
        pass
        # for npc in self.current_map.npc:
        #     result = detect_collisions(self.player, npc)
        #     if result:
        #         self.player.x = result[0]
        #         self.player.y = result[1]
