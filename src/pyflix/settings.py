"""
Fichier à importer pour utiliser le logger.

Ce fichier doit être importé en premier. Vous devez également importer `logging` dans
le fichier où vous utiliserez le logger. Le fichier `file.log` sera créé à la racine
du projet.
"""

import logging
from pathlib import Path
from platformdirs import user_data_path, user_log_path

APP_NAME = "formation-python-pyflix"

DATA_PATH = user_data_path(APP_NAME, ensure_exists=True)
LOG_FILE = user_log_path(APP_NAME, ensure_exists=True) / "pyflix-file.log"

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%H:%M:%S",
                    filename=LOG_FILE,
                    encoding='utf-8',
                    )
