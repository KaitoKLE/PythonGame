import logging

from pygame import error as pygame_error

from game import Game
from file_system import LOG_FILE


def init_logging():
    """Set up the logging module"""
    try:
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                            format='[%(levelname)s]: %(message)s')
    except (PermissionError, IOError):
        print('ERROR: Could not create the log file...')


def main():
    """
    This function initializes logging, creates and starts a game loop, handles exceptions, and shuts down logging.
    """
    init_logging()
    try:
        game = Game()
        game.start_loop()
    except (Exception, pygame_error) as e:
        print('THE PROGRAM HAS CRASHED!')
        logging.exception(e)
        logging.critical('CANNOT CONTINUE IN THIS STATE...')
    logging.info('Finished...\n' + '=' * 100)
    logging.shutdown()


# run the game
if __name__ == "__main__":
    main()
