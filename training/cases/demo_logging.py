#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module de démonstration de l'usage d'un logger. Les logs sont ajoutés à un
fichier `file.log`.
"""

import logging

logging.basicConfig(filename="file.log", level=logging.INFO)
logging.warning("Un warning")
logging.info("Une info")
