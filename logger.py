from datetime import datetime
from pathlib import Path
import logging
import os

# copied from TweetBot v1

# log format
formatter = logging.Formatter("[%(asctime)-15s] [%(levelname)s] %(message)s")

# creates a directory for the logs based on the year and the month
YEAR = datetime.now().strftime('%Y')
MONTH = datetime.now().strftime('%m')
CURRENTPATH = os.path.dirname(os.path.realpath(__file__))
LOGGER_PATH = CURRENTPATH + '/logs/' + YEAR + '/' + MONTH + '/'
Path(LOGGER_PATH).mkdir(parents=True, exist_ok=True)

# log file name as the date
DATENOW = datetime.now().strftime('%Y-%m-%d')
FILENAME = DATENOW + '.log'

# apply all above
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
logger_file_handler = logging.FileHandler(LOGGER_PATH + FILENAME)
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)
