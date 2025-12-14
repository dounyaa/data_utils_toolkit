import logging
import sys

from data_utils_toolkit.logger import get_logger


def test_get_logger():
    logger1 = get_logger("test")
    logger2 = get_logger("test")

    assert isinstance(logger1, logging.Logger)

    assert logger1 is logger2

    assert len(logger1.handlers) == 1
    assert len(logger2.handlers) == 1

    assert logger1.level == logging.INFO
    
    handler = logger1.handlers[0]
    assert handler.stream == sys.stdout