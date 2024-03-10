from pygame import Rect

from source.settings import TILES_SIZE, WALK_SPEED


class Camera:
    """Follows the focused character to keep it in the center of the display"""

    def __init__(self, w, h, character):
        self.__CORRECTION = TILES_SIZE / 2
        self.__rect = Rect(*character.coord, w, h)
        self.__focus = character
        self.__fancy_displacing = False

    @property
    def x(self):
        """Returns the position in pixels of the camera in the X coord."""
        return self.__rect.x + self.__CORRECTION

    @property
    def y(self):
        """Returns the position in pixels of the camera in the Y coord."""
        return self.__rect.y + self.__CORRECTION

    @property
    def size(self):
        return self.__rect.size

    @size.setter
    def size(self, new_value):
        self.__rect.size = new_value

    def update(self) -> None:
        """Moves the camera to keep the focus in the center of the display"""
        if self.__fancy_displacing:
            self.__fancy_displacement()
        else:
            self.__rect.center = self.__focus.coord

    def __fancy_displacement(self) -> None:
        """When it is needed to move the camera for a long distance, without teleporting it. like a cinematic"""
        finished = [False, False]
        if self.__focus.coord.x > self.__rect.center[0] + WALK_SPEED:
            self.__rect.x += WALK_SPEED
        elif self.__focus.coord.x < self.__rect.center[0] - WALK_SPEED:
            self.__rect.x -= WALK_SPEED
        else:
            finished[0] = True
        if self.__focus.coord.y > self.__rect.center[1] + WALK_SPEED:
            self.__rect.y += WALK_SPEED
        elif self.__focus.coord.y < self.__rect.center[1] - WALK_SPEED:
            self.__rect.y -= WALK_SPEED
        else:
            finished[1] = True
        if finished[0] and finished[1]:
            self.__fancy_displacing = False

    def focus(self, character, with_fancy_displacing=False) -> None:
        """Focus the camera in a new character"""
        self.__focus = character
        self.__fancy_displacing = with_fancy_displacing
