"""
Ceci est un module destiné à recevoir le code des fonctions mutualisées au sein
des notebooks. Vous pouvez y ajouter les fonction set les ressources que vous
pensez utiles.

Notez que dans un projet *normal* un module de ce type ne devrait être dédié
qu'à une seule unité fonctionnelle. Dans le cadre de la formation, nous allons
nous permettre de transgresser ce principe. Mais vous pouvez évidemment créer
d'autres modules (fichiers texte avec l'extension .py).

Notez également que ce commentaire est une documentation du module. Il s'agit
d'une docstring du module.
"""


def duration_for(how_many: int, unit_duration=7):
    """
    Calcul une durée totale en fonction d'une unité de temps.

    :param how_many: Le nombre d'unités de temps. Doit être positif.
    :param unit_duration: La durée d'une unité de temps, par défaut de 7 qui
    correspond à la durée d'une journée de travail. Doit être positif.
    :return: La durée totale.
    """
    how_many = int(how_many)
    unit_duration = int(unit_duration)

    if how_many < 0:
        raise ValueError('Your duration should be positive or null')

    if unit_duration < 0:
        raise ValueError('Your unit duration should be positive or null')

    return how_many * unit_duration


def to_minutes(hours: int, minutes=0):
    """
    calcul une durée en minutes en fonction d'heures et minutes.

    :param hours: une durée en heure, doit être positif.
    :param minutes: Une durée optionnelle en minutes. 0 par défaut. Doit être
    positif.
    :return: La durée totale en minutes.
    """
    hours = int(hours)
    minutes = int(minutes)
    if hours < 0 or minutes < 0:
        raise ValueError("Les durées doivent être positives")

    return int(hours) * 60 + int(minutes)
