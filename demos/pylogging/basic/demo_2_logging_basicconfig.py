"""
Module de démonstration de l'usage d'un logger avec une configuration *basique*.

IL y a 3 configurations de logger, testez en commentant et décommentant les configurations.
"""

import logging

# configuration du lvl de log
logging.basicConfig(level=logging.INFO)

# configuration du lvl de log et du format, le temps reformaté pour l'heure seule
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s",
#                     datefmt="%H:%M:%S")

# configuration du lvl de log et du format dans un fichier en utilisant le format temps standard
# logging.basicConfig(filename="file.log",
#                     level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug('Un debug')
logging.info('Une info')
logging.warning("Un warning")
logging.error("Une erreur")
logging.critical('Critique')
