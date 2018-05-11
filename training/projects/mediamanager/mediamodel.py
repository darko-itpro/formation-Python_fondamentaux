#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module définissant les objets *métier* de la gestion d'une médiathèque.
"""


class TvShow:
    """
    Représente une série et permet de gérer les saisons associées ainsi que les
    informations générales de la série.

    La gestion des saisons se fait ici à l'aide d'une liste triée à l'ajout de
    chaque nouvelle saison.
    """
    def __init__(self, name):
        """
        Crée une nouvelle série

        :param name: Nom de la série (non modifiable)
        """
        self._name = name
        self._seasons = []

    def _add_season(self, season):
        """
        On ne gère pas de saison directement, cette méthode est donc privée. Il
        est préférable de passer par cette méthode qui s'assure le tri.

        :param season:
        :return: None
        """
        if season not in self:
            self._seasons.append(season)
            self._sort()
        else:
            raise ValueError('Season exists')

    def add_episode(self, title, ep_number, season_number=None):
        for season in self._seasons:
            if season.number == season_number:
                season.add(Episode(title, ep_number, season_number))
                break
        else:
            season = Season(season_number)
            season.add(Episode(title, ep_number, season_number))
            self._add_season(season)

    @property
    def name(self):
        return self._name

    @property
    def seasons(self):
        """return a copy of this object's seasons list"""
        return list(self._seasons)

    def season(self, number):
        for season in self._seasons:
            if season.number == number:
                import copy
                return copy.deepcopy(season)

    def get_episodes(self, season_number=None):

        if season_number:
            for season in self._seasons:
                if season.number == season_number:
                    return season.episodes
            else:
                return []

        else:
            return sum([season.episodes
                        for season
                        in self._seasons], [])

    def _sort(self):
        """
        Tri les saisons par ordre *naturel* (numéro de saison).

        La méthode est privée car la collection en elle même est privée en
        conséquence, le tri de la liste appatient à l'objet.
        """
        self._seasons.sort(key=lambda x: x.number)

    def __len__(self):
        """
        Un TvShow peut être considéré comme un conteneur de saisons. Cette
        méthode spéciale permet donc d'obtenir la *taille* d'un TvShow qui sera
        donc le nombre de saisons grâce à la fonction len :
        `len(show)`
        :return: un entier correspondant au nombre de saisons.
        """
        return len(self._seasons)

    def __contains__(self, item):
        """
        Un TvShow peut être considéré comme un conteneur de saisons. Cette
        méthode spéciale permet donc d'interroger un TvShow à la manière
        `saison in show`

        :param item: Un élément qui doit être une saison mais qui doit surtout
        posséder une propriété `number`
        :return: Vrai si la collection de saisons possède un élément du même numéro.
        """
        if hasattr(item, "number"):
            cmp_value = item.number
        else:
            cmp_value = item

        for element in self._seasons:
            if element.number == cmp_value:
                return True

        return False

    def __str__(self):
        return "{} <{}>".format(self.name, len(self._seasons))


class Season:
    """
    Définit une saison caractérisée par son *numéro* et la liste des épisodes.
    """
    def __init__(self, number):

        self._number = int(number) if number else None
        if self._number and  self._number < 0:
            raise ValueError('Season number cannot be negative')

        self._episodes = []

    def add(self, episode):
        if episode not in self:
            self._episodes.append(episode)
            self.sort()
        else:
            raise ValueError("Episode exists")

    def episode(self, number):
        """
        Retourne un épisode en fonction de son numéro. Une exception est levée si aucun épisode ne correspond.

        :param number: Numéro de l'épisode.
        :return: Un épisode si la saison contient un épisode avec ce numéro ou None.
        :raises ValueError: If there is no episode with the given number.
        """
        for element in self._episodes:
            if element.number == int(number):
                return element

        raise ValueError('Episode {} does not exist'.format(number))

    @property
    def number(self):
        return self._number

    @property
    def episodes(self):
        """
        Cet *accesseur* retourne une copie de la liste des épisodes, évitant ainsi une modification accidentelle.
        :return: La liste des épisodes
        """
        return list(self._episodes)

    def sort(self):
        self._episodes.sort(key=lambda x: x.number)

    def __lt__(self, other):
        return self.number < other.number

    def __len__(self):
        return len(self._episodes)

    def __contains__(self, item):
        """
        Fonction *avancée* permétant d'interroger un objet Season pour savoir il possède un objet de
        type Episode avec l'instruction *episode in season*
        
        :param item: un objet de type Episode ou du moins qui contient un attribut *number* 
        :return: vrai si un élément de la collection contient un attribut *number* égal à l'attribut
        *number* de l'objet.
        """
        for element in self._episodes:
            if element.number == item.number:
                return True

        return False

    def __iter__(self):
        """
        Fonction *avancée*, permet de retourner un itérateur sous la forme d'un générateur qui sera
        utilisé pour la fonction for et permet de d'itérer sur les épisodes.

        :return: un générateur sur les épisodes
        """
        for episode in self._episodes:
            yield episode

    def __str__(self):
        return "Season {} <{}>".format(self.number, len(self._episodes))


class Media:
    def __init__(self, title, duration=None, year=None):

        try:
            if not title or title.isspace():
                raise ValueError("Title must have characters")
        except AttributeError:
            raise ValueError("Title must be a String")

        self._title = title
        self._duration = int(duration) if duration else None
        self.year = int(year) if year else None

    @property
    def duration(self):
        """Duration of the episode."""
        if self._duration == 0:
            raise ValueError("Duration not set")
        else:
            return self._duration

    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("Duration must be a positive value"
                             )
        self._duration = int(value)

    @duration.deleter
    def duration(self):
        self._duration = None

    @property
    def title(self):
        return self._title

    def hm_duration(self):
        """
        Returns the duration in a hour/minute format
        :return: a tuple representing the duration where the first element is
        the duration in hours and the second is the remaining duration in
        minutes
        """
        return divmod(self.duration, 60) if self.duration else None


class Episode(Media):
    """
    Définit un épisode qui est un objet de type média.

    Le titre et le numéro sont considérés comme pouvant être modifés.

    :param title: Titre de l'épisode
    :param number: Numéro de l'épisode, doit être un entier positif ou nul.
    :param season: Saison à laquelle appartient l'épisode. Soit être un entier positif ou nul ou None si la saison n'est pas connue.
    :param duration: Durée en minutes. Doit être un entier positif ou None si la durée est inconnue.
    :param year: Année de l'épisode, doit être un entier positif suppérieur à 1900 ou None si inconnu.
    """

    def __init__(self, title, number, season=None, duration=None, year=None):
        Media.__init__(self, title, duration, year)
        self._number = int(number)
        self._season = int(season) if season else None

    @property
    def number(self):
        """
        Le numérod e l'épisode, ne peut être modifié.
        """
        return self._number

    @property
    def season(self):
        """
        La saison à laquelle appartient l'épisode. Ne peut être modifiée.
        """
        return self._season

    def __str__(self):
        return "ep.{} - {}".format(self.number, self.title)


class Movie(Media):
    def __init__(self, title, duration=None, year=None, director=None):
        Media.__init__(self, title, duration, year)
        self.director = str(director) if director else None


if __name__ == '__main__':
    pass
