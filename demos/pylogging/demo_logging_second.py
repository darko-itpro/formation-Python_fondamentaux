"""
Second logging module which has to be called from the basic.
"""

import logging

logging.warning("Log called in module root")


def do_something():
    logging.warning("In secondary module")