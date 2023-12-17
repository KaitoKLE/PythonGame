import logging
from random import choice, randint

import pygame

from character import Character
from display import Display, Sprite, detect_collisions, L_DOWN, L_RIGHT, L_UP, L_LEFT, PLAYER_SPRITE

# GAME SETTINGS
MOVEMENT_DEFAULT_SPEED = 5
DEFAULT_FRAME_RATE = 60


class Game:
    def __init__(self):
        logging.info('Game is initializing')
        pygame.init()
        self.running = False
        self.clock = pygame.time.Clock()
        self.display = Display(self)
        self.active_keys = set()
        self.player = Character(self.display.center, 'Player', Sprite(40, L_DOWN, (255, 255, 255), PLAYER_SPRITE))
        self.npcs = (
            Character((500, 400), 'Red NPC', Sprite(40, L_DOWN, (255, 0, 0), PLAYER_SPRITE)),
            Character((200, 500), 'Green NPC', Sprite(40, L_DOWN,(0, 255, 0), PLAYER_SPRITE)),
            Character((80, 300), 'Blue NPC', Sprite(40, L_DOWN, (0, 0, 255), PLAYER_SPRITE))
        )
        logging.info('The game is now ready to start running')

    def loop(self):
        self.running = True
        logging.info('Game is running')
        while self.running:
            self.update()
            self.display.draw(self.npcs, self.player)
        logging.info('The game stopped running')

    def stop(self):
        logging.info('Stopping game')
        self.running = False

    def update(self):
        self.events()
        self.player.move()
        self.constraint(self.player)
        self.process_collisions()
        self.clock.tick(DEFAULT_FRAME_RATE)

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
        if pygame.K_RIGHT in self.active_keys:
            self.player.dx = MOVEMENT_DEFAULT_SPEED
            self.player.sprite_data.looking_at = L_RIGHT
        elif pygame.K_LEFT in self.active_keys:
            self.player.dx = -MOVEMENT_DEFAULT_SPEED
            self.player.sprite_data.looking_at = L_LEFT
        else:
            self.player.dx = 0
        if pygame.K_UP in self.active_keys:
            self.player.dy = -MOVEMENT_DEFAULT_SPEED
            self.player.sprite_data.looking_at = L_UP
        elif pygame.K_DOWN in self.active_keys:
            self.player.dy = MOVEMENT_DEFAULT_SPEED
            self.player.sprite_data.looking_at = L_DOWN
        else:
            self.player.dy = 0

    def constraint(self, character):
        if character.x > self.display.width - character.sprite_data.size:
            character.x = self.display.width - character.sprite_data.size
        if character.x < 0:
            character.x = 0
        if character.y > self.display.height - character.sprite_data.size:
            character.y = self.display.height - character.sprite_data.size
        if character.y < 0:
            character.y = 0

    def process_collisions(self):
        for npc in self.npcs:
            result = detect_collisions(self.player, npc)
            if result:
                self.player.x = result[0]
                self.player.y = result[1]
