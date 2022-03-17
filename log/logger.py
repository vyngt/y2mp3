"""
App's Logger
"""
import logging


def logger(
    name: str,
    fmt="%(asctime)s - %(name)s - %(message)s",
    dfm: str | None = None,
):
    """
    blah blah...\n
    simple settings\n
    - fmt="%(asctime)s - %(name)s - %(message)s"\n
    - dfm="%Y-%m-%d %H:%M:%S"\n
    """
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.INFO)

    sth = logging.StreamHandler()
    sth.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt, dfm)
    sth.setFormatter(formatter)

    _logger.addHandler(sth)
    return _logger
