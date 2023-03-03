"""
Fichier à importer pour utiliser le logger.

Ce fichier doit être importé en premier. Vous devez également importer `logging` dans
le fichier où vous utiliserez le logger. Le fichier `file.log` sera créé à la racine
du projet.
"""

import logging
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%H:%M:%S",
                    filename=ROOT_PATH / "file.log",
                    )
