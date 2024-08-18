"""Конфигурационный файл для логгирования тест-кейсов pytest"""


import logging
import os

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = ('%(asctime)s - %(levelname)s'
              ' - %(filename)s - %(lineno)d - %(message)s')


def setup_logging(log_file_name, log_level=logging.DEBUG):
    """Logger initialization ."""

    current_dir = os.path.dirname(os.path.abspath(__file__))

    log_dir = os.path.join(current_dir, "APIlogs")

    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, log_file_name)

    logger = logging.getLogger(__name__ + "." + log_file_name.split(".")[0])
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
