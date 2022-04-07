import logging


# Creation d'un logger *custom*
logger = logging.getLogger(__name__)

# Création des handlers, un vers la console, un vers un fichier
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)

f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.ERROR)

# Création des formatters et ajout aux handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Ajout des handlers au logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
