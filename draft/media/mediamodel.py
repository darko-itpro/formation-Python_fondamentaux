#!/usr/bin/env python

"""
Ce module propose le modèle de base d'une gestion de série tel que vu lors de la
formation. Il est destiné à proposer une *correction* et à être disponible pour
ceux ayant… saboté leur module.
"""


class Episode:
    """
    Un épisode d'une série
    """
    def __init__(self, title: str, number: int, season=None):
        """
        Constructeur d'un objet représentant un épisode.

        Pour les puristes, il ne s'agit pas d'un objet car celui-ci n'a pas de
        comportement à proporement parler, mais d'un *transporteur de données*.

        Le numéro de saison peut être optionnel si la saison n'est pas connue.

        :param title: Titre de l'épisode
        :param number: Numéro de l'épisode dans la saison.
        :param season: Numéro de saison, optionnel (doit alors être None).
        """
        try:
            if not title or title.isspace():
                raise ValueError('Empty title')
        except AttributeError:
            raise ValueError('Title may not be a String')

        self._title = title
        self._number = int(number)
        self._season_number = int(season) if season else None

    def _get_number(self):
        """
        Cette méthode n'est pas une méthode dans cet objet. Plus bas, elle est
        un paramètre de la classe property qui est une autre manière
        d'instancier une property.

        :return: Le numéro de l'épisode dans la saison.
        """
        return self._number

    @property
    def title(self):
        return self._title

    @property
    def season_number(self):
        return self._season_number

    def __lt__(self, other):
        """
        Methode surchargée pour permettre un tri naturel sur le numéro d'épisode.

        :param other: un autre Episode ou un objet possédant une méthode number()
        :return: True si cet objet est inférieur, sinon False.
        """

        return self.number < other.number

    def __eq__(self, other):
        """
        Méthode surchargée pour permettre de comparer les épisodes entre eux.

        :param other: Un autre objet.
        :return: True si l'objet comparé est un épisode ayant le même numéro et
        le même numéro de saison. False sinon.
        """
        if not isinstance(other, Episode):
            return False

        return (self.number, other.number) == (self.season_number,
                                               other.season_number)

    number = property(_get_number)  # Voir documentaiton de la méthode _get_number


class TvShow:
    """
    Classe représentant la notion d'une série télévisée
    """
    def __init__(self, name):
        self._name = name
        self._episodes = []

    def add_episode(self, title: str, number: int, season_number: int = None):
        """
        Ajoute un épisode à la série si il n'existe pas déjà.

        :param title: Titre de l'épisode
        :param number: Numéro de l'épisode dans la saison
        :param season_number: Saison de l'épisode, optionnel.
        :raise ValueError: lorsqu'un épisode existe déjà.
        """
        new_episode = Episode(title, number, season_number)
        if new_episode in self._episodes:
            raise ValueError(f'Duplicate Episode [{title}]')

        self._episodes.append(new_episode)

    @property
    def episodes(self):
        return self._episodes.copy()

    @property
    def name(self):
        return self._name

    def get_episodes(self, season:int = None):
        """
        Retourne les épisodes de la série. Si le paramètre est un numéro de
        saison, retourne une liste des épisodes de la série filtré sur cette
        saison.

        :param season: La saison selon laquelle filtrée ou None.
        :return: une liste d'épisodes selon le critère de sélection.
        :rtype: list
        """
        if season is None:
            return self.episodes
        else:
            return [episode
                    for episode in self.episodes
                    if episode.season_number == season]
