import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv('PROJECT_NAME', 'elements')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
