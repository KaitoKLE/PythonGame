from time import strftime

import pygame
from pygame import draw, Surface
from pygame.font import Font

from settings.paths import UI_FONT, CLOCK_FONT
from engine.mouse import MouseCursor
from engine.special import UIColors
from settings.constants import WHITE, BLACK, LOADING_ST, PAUSED_ST

# UI settings
DEFAULT_UI_COLORS = UIColors(WHITE, BLACK)


def ui_font(text, color, size):
    return Font(UI_FONT, size).render(text, True, color)


def number_font(text, color):
    return Font(CLOCK_FONT, 36).render(text, True, color)


class UI:
    def __init__(self, display):
        self.__display = display
        self.__ui_colors = DEFAULT_UI_COLORS

    def loading_screen(self):
        text = ui_font('Loading...', self.__ui_colors.primary, 64)
        pos_x = self.__display.canvas.get_width() - text.get_width() * 1.5
        pos_y = self.__display.canvas.get_height() - text.get_height() * 2
        self.__display.canvas.blit(text, (pos_x, pos_y))

    def pause_menu(self):
        # TEMPORAL IMPLEMENTATION
        text = ui_font('PAUSED', self.__ui_colors.primary, 64)
        x = self.__display.canvas.get_width() / 2 - text.get_width() / 2
        y = self.__display.canvas.get_height() / 2 - text.get_height() / 2
        self.__display.canvas.blit(text, (x, y))

    def draw_cursor(self, mouse: MouseCursor):
        self.__display.canvas.blit(mouse.image, mouse.pos)

    def draw_clock(self, game_time: {strftime}):
        text_clock = number_font(game_time.strftime('%I:%M %p'), self.__ui_colors.primary)
        text_clock.set_alpha(150)
        text_date = number_font(game_time.strftime('%d/%m/%Y'), self.__ui_colors.primary)
        text_date.set_alpha(150)
        surface = self.__draw_rect(
            (text_date.get_width() + 20, text_clock.get_height() + text_date.get_height() + 20),
            2,
            (self.__ui_colors.secondary, self.__ui_colors.primary),
        )
        surface.blit(text_clock, (10, 10))
        surface.blit(text_date, (10, text_clock.get_height() + 10))
        surface.set_alpha(150)
        self.__display.canvas.blit(surface, (10, 10))

    def update(self, game):
        if game.status == LOADING_ST:
            self.loading_screen()
        elif game.status == PAUSED_ST:
            self.pause_menu()
        else:
            self.draw_clock(game.game_time)
        self.draw_cursor(game.mouse)

    def __draw_rect(self, size, border=0, colors=None):
        if not colors:
            colors = self.__ui_colors
        surface = Surface(size, pygame.SRCALPHA)
        border = (0, border)
        for i in range(2):
            draw.rect(surface, colors[i], (0, 0, size[0], size[1]), border[i])
        return surface
