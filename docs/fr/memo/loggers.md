# Les loggers

Plutôt que d’afficher une chaine de caractères que je vais qualifier de *débug*,  il est préférable 
d’utiliser un logger.

En effet, la fonction `print()` est à réserver à l’affichage avec l’utilisateur. Les loggers 
servent à conserver des traces de l’exécution. Traces qui peuvent aussi bien être un suivi de 
l’exécution que des avertissements que quelque chose ne s’est pas tout à fait déroulé comme prévu. 

De plus, utiliser un logger permet de bien définir pourquoi vous voulez restituer telle information.

La manière la plus simple, et à laquelle nous nous limiterons dans cette formation, pour utiliser 
un logger va être la suivante.

Au début de vos scripts, importez la bibliothèque `logging`. En soi, vous n’avez rien d’autre à 
faire.

```python
import logging
```

Vous pouvez alors utiliser les différents niveaux de logs :

```python
logging.debug('Un debug')
logging.info('Une info')
logging.warning("Un warning")
logging.error("Une erreur")
logging.critical('Critique')
```

Vous pouvez cependant configurer les logs avec la configuration basique. Juste après l’import, 
configurez le logger de la manière suivante :

```python
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
```

Enfin, pour ne pas mélanger les logs et les affichages si vous en avez besoin, vous pouvez aussi 
déclarer que les logs seront dirigés dans un fichier :

```python
logging.basicConfig(filename="file.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
```