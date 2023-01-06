"""
Ce code illustre le log lorsque l'application comporte plusieurs modules. Pour les besoins
de l'illustration, le module `demo_logging_second` comporte un log à la racine.
"""

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

import demos.pylogging.demo_logging_second as ls

ls.do_something()
