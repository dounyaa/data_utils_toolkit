import logging
import sys

from pythonjsonlogger import json as jsonlogger


def get_logger(name: str) -> logging.Logger:
    """
    Return a JSON-configured logger for the given name. 
    The same logger instance is reused across calls.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(fmt="%(asctime)s %(name)s %(levelname)s %(message)s")
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(console_handler)
    logger.propagate = False

    return logger