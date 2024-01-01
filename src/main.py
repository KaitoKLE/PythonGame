import logging

from game import Game
from src.data_manager import DataManager


def init_logging():
    try:
        logging.basicConfig(filename='../logging.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s: %(message)s')
    except (PermissionError, IOError):
        logging.error('ERROR: The logging module was NOT successfully initialized!')


# run the game
init_logging()
try:
    if DataManager.init():
        Game().loop()
    else:
        logging.critical('The game cannot run in this state...')
except Exception as e:
    print('THE PROGRAM HAS CRASHED!')
    logging.exception(f'The game crashed: {e}')
logging.info(f'Program is finishing\n' + '=' * 100)
logging.shutdown()
