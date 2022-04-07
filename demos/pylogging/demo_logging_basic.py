"""
Module de démonstration de l'usage d'un logger avec une configuration *basique*.
Les logs sont ajoutés à un fichier `file.log`.
"""

import logging
import demos.pylogging.demo_logging_second as second

logging.basicConfig(filename="file.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug('Un debug')
logging.info('Une info')
logging.warning("Un warning")
logging.error("Une erreur")
logging.critical('Critique')

try:
    int("toto")
except ValueError:
    logging.error("Convert error", exc_info=True)
    logging.exception("Exception logger call")

second.do_something()
