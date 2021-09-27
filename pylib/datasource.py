"""
Ce module est une source de données pour les différents exercices.

Ces données sont hétéroclytes, évidemment, dans un "vrai" projet, elles seraient organisées par
arborescence fonctionnelle.
"""

import random
random.seed()

bbt_s12 = [['The Conjugal Configuration', True, 20],
           ['The Wedding Gift Wormhole', True, 21],
           ['The Procreation Calculation', True, 20],
           ['The Tam Turbulence', True, 19],
           ['The Planetarium Collision', True, 19],
           ['The Imitation Perturbation', True, 19],
           ['The Grant Allocation Derivation', True, 19],
           ['The Consummation Deviation', True, 22],
           ['The Citation Negation', True, 20],
           ['The VCR Illumination', False, 20],
           ['The Paintball Scattering', False, 19],
           ['The Propagation Proposition', False, 20],
           ['The Confirmation Polarization', False, 20],
           ['The Meteorite Manifestation', False, 19],
           ['The Donation Oscillation', False, 21],
           ['The D & D Vortex', False, 20],
           ['The Conference Valuation', False, 19],
           ['The Laureate Accumulation', False, 21],
           ['The Inspiration Deprivation', False, 20],
           ['The Decision Reverberation', False, 19],
           ['The Plagiarism Schism', False, 19],
           ['The Maternal Conclusion', False, 20],
           ['The Change Constant', False, 19],
           ['The Stockholm Syndrome', False, 23]]


def time_loader():
    """
    Fonction simulant la collecte d'une donnée à partir d'une source de données.
    """
    return "30"


def get_start_time():
    """
    Fonction simulant la collecte de la donnée à partir d'une source de données.
    """
    return "20h42"


def get_season(user=None):
    """
    Fonction permétant d'accéder à la saison d'une série. Si un paramètre user est passé, le retour
    sera adapté à l'utilisateur

    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par une liste
    [titre:str, vu:bool, durée:int]. Sinon, une liste de titres.
    """
    if user is None:
        return [title for title, *_ in bbt_s12]
    else:
        return bbt_s12


def _to_dict(title, duration, viewed):
    episode = {"title": title, "duration": duration}
    if viewed:
        episode['viewed'] = True
    else:
        if random.random() > 0.8:
            episode['viewed'] = False

    return episode

def load_season(user=None):
    return [_to_dict(title, duration, viewed)
            for title, viewed, duration in bbt_s12]


def get_movies():
    """
    Fonction permétant d'obtenir une liste de médias.
    """
    return [["The Philosopher's Stone", 152, True],
            ["The Chamber of Secrets", 161, True],
            ["The Prisoner of Azkaban", 142, False],
            ["the Goblet of Fire", 157, True],
            ["the Order of the Phoenix", 138, False],
            ["the Half-Blood Prince", 153, True],
            ["the Deathly Hallows – Part 1", 126, False],
            ["the Deathly Hallows – Part 2", 130, False]]
