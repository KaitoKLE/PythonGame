from logging import info
from datetime import timedelta, datetime
from threading import Thread

from pygame import event as system_event, mouse, time, key as keyboard, init as pygame_init
from pygame.constants import QUIT, KEYUP, KEYDOWN

from display.camera import Camera
from engine.data_manager import DataManager
from display.canvas import Canvas
from engine.map import Map
from game_objects.player import Player
from settings.constants import (TIME_SPEED, LOADING_ST, PLAYING_ST, STOPPING_ST, PAUSED_ST,
                                RIGHT_VECTOR, LEFT_VECTOR, UP_VECTOR, DOWN_VECTOR, STAY_VECTOR,
                                ACTION_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY, UP_KEY, MENU_KEY, RUN_KEY, EXIT_KEY,
                                FULL_SCREEN)
from engine.mouse import MouseCursor
from engine.file_system import FileSystem


class Game:
    """Overall class to manage game behavior."""

    def __init__(self):
        """Initialize the game."""
        info('Initializing')
        pygame_init()
        mouse.set_visible(False)  # hide the system pointer to only see the game pointer :D
        game_data = FileSystem.parse_json('settings.json')
        self.__name = game_data['name']
        self.__version = game_data['version']
        self.__status: int = LOADING_ST
        self.__clock = time.Clock()
        self.__display: Canvas = Canvas(self.__name)
        self.__game_time = datetime(1790, 1, 14, 12, 0, 0)
        self.__current_map: Map = None
        self.__player: Player = Player('Player')
        self.__camera: Camera = Camera(self.__display.width, self.__display.height, self.__player)
        self.__thread = Thread(target=self.__load_assets, daemon=True)
        self.__thread.start()
        self.__player_directional_input = STAY_VECTOR
        self.__mouse: MouseCursor = MouseCursor()

    @property
    def name(self) -> str:
        """Return the name of the game."""
        return self.__name

    @property
    def version(self) -> str:
        """Return the version of the game."""
        return self.__version

    @property
    def map(self):
        """
        This is a property function that returns the current map.
        """
        return self.__current_map

    @property
    def player(self):
        """
        This is a property method that returns the value of the player attribute.
        """
        return self.__player

    @property
    def camera(self):
        """
        Getter method for the camera property.
        """
        return self.__camera

    @property
    def game_time(self):
        """
        This is a property function that returns the game time.
        """
        return self.__game_time

    @property
    def status(self):
        """
        This is a property function that returns the game status.
        """
        return self.__status

    @property
    def mouse(self):
        """
        This is a property function that returns the mouse cursor.
        """
        return self.__mouse

    @property
    def fps(self):
        """
        This is a property function that returns the frames per second.
        """
        return int(self.__clock.get_fps())

    def start_loop(self):
        """Start the main loop for the game."""
        self.__loop()

    def stop_loop(self):
        """Stop the main loop for the game."""
        info('Stopping')
        self.__status = STOPPING_ST

    def load_map(self, map_id='test_zone'):
        """
        Load a map with the given map_id, set the status to loading, create a new Map object, kill the player, spawn the player at the map's player spawn point, add all characters from the map to the player, and set the status to playing.
        
        :param map_id: str, the identifier of the map to load
        :return: None
        """
        self.__status = LOADING_ST
        self.__current_map = Map(map_id)
        self.__player.kill()
        self.__player.spawn(self.__current_map.player_spawn)
        self.__player.add(self.__current_map.all_characters)
        self.__status = PLAYING_ST

    def __load_assets(self):
        """
        Initializes the routine by loading assets, initializing the DataManager, loading the map, and registering event types.
        """
        info('Loading assets...')
        result = DataManager.init()
        if not result:
            raise Exception('Something went wrong while loading assets')
        self.load_map()  # TODO: replace this method with the game HOME UI
        info('Done loading assets!')

    def __loop(self):
        info('Main loop started')
        while self.__status != STOPPING_ST:
            self.__update()
        info('Stopped running')

    def __update(self):
        """
        Update the game state based on the current status and user inputs.
        """
        delta = self.__clock.tick()
        self.__update_system_events()
        if self.__status == PLAYING_ST:
            self.__current_map.all_characters.update(self.__current_map, self.__player_directional_input)
            self.__camera.update()
            self.__time_flow(delta)
        self.__display.update(self)

    def __update_system_events(self):
        """Checks for game events"""
        for event in system_event.get():
            if event.type == QUIT:
                info('An event to QUIT has been started')
                self.stop_loop()
            if event.type == KEYDOWN:
                self.__key_down(event.key)
            if event.type == KEYUP:
                pass  # Unneeded for now...
        if self.__status == PLAYING_ST:
            self.__player_movement()
        self.__mouse.update()

    def __key_down(self, key):
        """
        Handle the key press event and perform corresponding actions based on the input key.
        :param key: The key that was pressed
        :return: None
        """
        if key == EXIT_KEY:
            info('User is quitting')
            self.stop_loop()
        elif key == ACTION_KEY:
            # for player interaction, unused for now
            pass
        if key == MENU_KEY:
            self.__status = PAUSED_ST if self.__status != PAUSED_ST else PLAYING_ST
        if key == FULL_SCREEN:
            info('Full screen event has been started. However, this function is temporarily disabled')
            pass
            # new_size = self.__display.change_fullscreen_mode()
            # FIXME: camera glitches when size is changed...
            # self.__camera.size = self.__display.size

    def __player_movement(self):
        """
        This function handles player movement based on the keys pressed, updating the player's direction and running state accordingly.
        No parameters or return types are specified.
        """
        pressed_keys = keyboard.get_pressed()
        if pressed_keys[RIGHT_KEY]:
            direction = RIGHT_VECTOR
        elif pressed_keys[LEFT_KEY]:
            direction = LEFT_VECTOR
        elif pressed_keys[UP_KEY]:
            direction = UP_VECTOR
        elif pressed_keys[DOWN_KEY]:
            direction = DOWN_VECTOR
        else:
            direction = STAY_VECTOR
        self.__player_directional_input = direction
        self.__player.running = pressed_keys[RUN_KEY]

    def on_event(self, event):
        pass

    def __time_flow(self, delta):
        delta *= TIME_SPEED
        self.__game_time += timedelta(seconds=delta / 1000)
