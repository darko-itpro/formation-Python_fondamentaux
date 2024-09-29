import logging


# Création des formatters pour gérer les formats d'affichage
daily_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                 datefmt='%H:%M:%S')
complete_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Création des handlers, un vers la console, un vers un fichier
console_handler = logging.StreamHandler()

file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.ERROR)

# Association des formatters aux handlers
console_handler.setFormatter(daily_format)
file_handler.setFormatter(complete_format)

# Creation d'un logger *custom*
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ajout des handlers au logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug('Un debug')
logger.info('Une info')
logger.warning("Un warning")
logger.error("Une erreur")
logger.critical('Critique')
