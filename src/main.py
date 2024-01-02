import logging

from game import Game
from src.constants import GAME_NAME
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
        logging.critical('Error while scanning data files')
except Exception as e:
    print('THE PROGRAM HAS CRASHED!')
    logging.exception(f'The game crashed: {e}')
    logging.critical('THE GAME CANNOT CONTINUE IN THIS STATE...')
logging.info(f'{GAME_NAME} is finishing\n' + '=' * 100)
logging.shutdown()
