"""
App's Logger
"""
import logging

FORMATTER = "%(asctime)s - %(name)s - %(message)s"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str):
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.INFO)

    sth = logging.StreamHandler()
    sth.setLevel(logging.INFO)

    formatter = logging.Formatter(FORMATTER, DATETIME_FORMAT)
    sth.setFormatter(formatter)

    _logger.addHandler(sth)
    return _logger
