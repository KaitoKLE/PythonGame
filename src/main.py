import logging

from game import Game


def init_logging():
    try:
        logging.basicConfig(filename='../logging.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s: %(message)s')
    except (PermissionError, IOError):
        logging.error('ERROR: The logging module was NOT successfully initialized!')


def launch():
    try:
        Game().loop()
    except Exception as e:
        print('THE PROGRAM HAS CRASHED!')
        logging.exception(f'The game crashed: {e}')


if __name__ == '__main__':
    init_logging()
    launch()
    logging.info(f'Program is finishing\n' + '=' * 100)
    logging.shutdown()
