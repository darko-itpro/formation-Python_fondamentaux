"""
Second logging module which has to be called from the basic.
"""

import logging

logging.warning("failing")


def do_something():
    logging.warning("In secondary module")