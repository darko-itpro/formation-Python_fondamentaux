#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest

from draft.media import base_mediamodel as mediamodel


class CreateEpisode(unittest.TestCase):

    def test_create_episode_without_season(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertIsNotNone(episode)

    def test_create_episode_with_season(self):
        episode = mediamodel.Episode("Title", 1, 1)
        self.assertIsNotNone(episode)

    def test_title_accessible(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertEqual(episode.title, "Title")

    def test_should_not_assign_title(self):
        episode = mediamodel.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.title = 'Other title'

    def test_number_accessible(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertEqual(episode.number, 1)

    def test_should_not_assign_number(self):
        episode = mediamodel.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.number = 2

    def test_season_accessible(self):
        episode = mediamodel.Episode("Title", 1, 2)
        self.assertEqual(episode.season, 2)

    def test_shouldnt_assign_season(self):
        episode = mediamodel.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.season = 2

    def test_without_season_should_be_none(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertIsNone(episode.season)

    def test_number_must_be_integer_compatible(self):
        episode = mediamodel.Episode('Title', 1)
        self.assertEqual(episode.number, 1)
        episode = mediamodel.Episode('Title', "1")
        self.assertEqual(episode.number, 1)
        with self.assertRaises(ValueError):
            mediamodel.Episode('Title', "un")

    def test_season_must_be_integer_compatible(self):
        episode = mediamodel.Episode('Title', 1, 2)
        self.assertEqual(episode.season, 2)
        episode = mediamodel.Episode('Title', 1, "2")
        self.assertEqual(episode.season, 2)
        with self.assertRaises(ValueError):
            mediamodel.Episode('Title', 1, "un")

    def test_title_should_be_string_or_raise_error(self):
        with self.assertRaises(ValueError):
            mediamodel.Episode(10, 1)

    def test_title_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            mediamodel.Episode('', 1)


class CreateShow(unittest.TestCase):

    def test_create_new_show(self):
        show = mediamodel.TvShow('Mr. Robot')
        self.assertIsNotNone(show)

    def test_show_name_accessible(self):
        show = mediamodel.TvShow('Mr. Robot')
        self.assertEqual(show.name, 'Mr. Robot')

    def test_shouldnt_assign_name(self):
        show = mediamodel.TvShow('Mr. Robot')
        with self.assertRaises(AttributeError):
            show.name = 'Dr. Who'


class AccessEpisodes(unittest.TestCase):

    def setUp(self):
        self.show = mediamodel.TvShow('Game of Thrones')

    def tearDown(self):
        del self.show

    def test_has_episodes_attr(self):
        self.assertTrue(hasattr(self.show, 'get_episodes'))

    def test_has_add_episode_attr(self):
        self.assertTrue(hasattr(self.show, 'add_episode'))

    def test_empty_show(self):
        self.assertEqual(len(self.show.get_episodes()), 0)

    def test_add_episode_with_season_number(self):
        self.show.add_episode("Into the North", 1, 1)
        self.assertEqual(len(self.show.get_episodes()), 1)

    def test_add_episode_without_season_number(self):
        self.show.add_episode("Into the North", 1)
        self.assertEqual(len(self.show.get_episodes()), 1)

    def test_should_not_alter_episodes(self):
        episodes = self.show.get_episodes()
        episodes.append(mediamodel.Episode('Intruder', 2))
        self.assertEqual(len(self.show.get_episodes()), 0)

    def test_should_not_add_same_episode(self):
        self.show.add_episode("Into the North", 1, 1)
        with self.assertRaises(ValueError):
            self.show.add_episode('Kingslayer', 1, 1)

class SeasonClassEvolution(unittest.TestCase):
    """
    Tests de l'objet Season

    Les tests de cette classe ne passent pas. Vous devez enlever les skip l'un
    après l'autre avec une approche TDD : ne levez qu'un skip et ajoutez le code
    qui fait passer le test.

    Les tests suivants sont commentés pour expliquer la démarche *TDD* dans leur
    mise en œuvre.

    """

    @unittest.skip("Season new class 1")
    def test_create_new_season(self):
        """
        Test simplement l'existence d'une classe Season qui doit attendre un
        paramètre.
        """
        season = mediamodel.Season(1)
        self.assertIsNotNone(season)

    @unittest.skip("Season new class 2")
    def test_season_number_must_be_positive_value(self):
        """
        Test que le numéro de saison doit être positif
        """
        with self.assertRaises(ValueError):
            mediamodel.Season(-1)

    @unittest.skip("Season new class 3")
    def test_has_number_attribute(self):
        """
        Test que la classe Season a bien un attribut *number*.
        """
        season = mediamodel.Season(1)
        self.assertTrue(hasattr(season, 'number'))

    @unittest.skip("Season new class 4")
    def test_number_is_the_season_number(self):
        """
        Test que l'attribut *number* correspond bien au paramètre passé à
        l'initialisation.
        """
        season = mediamodel.Season(2)
        self.assertEqual(season.number, 2)
        season = mediamodel.Season(1)
        self.assertEqual(season.number, 1)

    @unittest.skip("Season new class 5")
    def test_number_must_be_int(self):
        """
        Test que number doit être un entier.
        """
        season = mediamodel.Season(2)
        self.assertTrue(isinstance(season.number, int))

        season = mediamodel.Season("2")
        self.assertTrue(isinstance(season.number, int))
        self.assertEqual(season.number, 2)

        with self.assertRaises(ValueError):
            mediamodel.Season("deux")

    @unittest.skip("Season new class 6")
    def test_has_episodes_attribute(self):
        """
        Test que la classe Season a bien un attribut *episodes*
        """
        season = mediamodel.Season(1)
        self.assertTrue(hasattr(season, 'episodes'))

    @unittest.skip("Season new class 7")
    def test_episodes_attribute_is_collection(self):
        """
        Test que l'atribut episodes soit bien une collection.
        """
        season = mediamodel.Season(1)
        self.assertEqual(len(season.episodes), 0)

    @unittest.skip("Season new class 8")
    def test_has_add_attribute(self):
        """
        Test que la classe Season a un attribut *add*.
        """
        season = mediamodel.Season(1)
        self.assertTrue(hasattr(season, 'add'))

    @unittest.skip("Season new class 9")
    def test_can_add_value_to_episodes(self):
        """
        Test simplement que la méthode add prends un paramètre. Dans une
        approche *TDD*, nous allons d'abord nous assurer qu'un élément ajouté à
        la saison est bien ajouté à la liste encapsulée. Dans un premier temps,
        cet élément n'a pas à être un *Episode*.
        """
        season = mediamodel.Season(1)
        season.add("value")
        self.assertEqual(len(season.episodes), 1)

    @unittest.skip("Season new class 10")
    def test_added_episodes_cannot_be_duplicates(self):
        """
        Il ne doit pas être possible d'ajouter deux même épisodes, c'est à dire
        qu'ils ont le même numéro.

        Faire passer ce test va provoquer une erreur dans le test
        *test_can_add_value_to_episodes* puisque pour l'écriture de ce dernier,
        nous ajoutions juste une chaine de caractères. Dans une approche *TDD*,
        il est courant de devoir revenir sur un test qui doit évoluer en
        fonction d'autres. Corrigez donc le test précédent.
        """
        season = mediamodel.Season(1)
        season.add(mediamodel.Episode("Rose", 1, 1))

        with self.assertRaises(ValueError): # Doit échouer car même épisode
            season.add(mediamodel.Episode("Rose", 1, 1))

        with self.assertRaises(ValueError): # Doit échouer car seul le numéro compte
            season.add(mediamodel.Episode("Daleks", 1, 1))

        with self.assertRaises(ValueError): # Doit échouer car seul le numéro compte
            season.add(mediamodel.Episode("Cybermen", 1))

        with self.assertRaises(ValueError): # Doit échouer car seul le numéro compte
            season.add(mediamodel.Episode("The Next Doctor", 1, 5))


class SeasonEvolution(unittest.TestCase):
    """
    Tests de la gestion des épisodes par des objets Season.

    Les tests de cette classe ne passent pas. Vous devez enlever les skip l'un
    après l'autre avec une approche TDD : ne levez qu'un skip et ajoutez le code
    qui fait passer le test.
    """

    def setUp(self):
        self.show = mediamodel.TvShow('Game of Thrones')
        self.show.add_episode("Into the North", 1, 1)

    def tearDown(self):
        del self.show

    @unittest.skip("Season Evolution 1")
    def test_have_method_season(self):
        self.assertTrue(hasattr(self.show, 'season'))

    @unittest.skip("Season Evolution 2")
    def test_have_method_seasons(self):
        self.assertTrue(hasattr(self.show, 'seasons'))

    @unittest.skip("Season Evolution 3")
    def test_season_returns_elements(self):
        self.assertEqual(len(self.show.seasons), 1)

    @unittest.skip("Season Evolution 4")
    def test_access_season(self):
        self.assertIsNotNone(self.show.season(1))

    @unittest.skip("Season Evolution 5")
    def test_season_is_object_with_episodes_attr(self):
        self.assertTrue(hasattr(self.show.season(1), 'episodes'))

    @unittest.skip("Season Evolution 6")
    def test_existing_season_has_one_element(self):
        self.assertEqual(len(self.show.season(1).episodes), 1)

    @unittest.skip("Season Evolution 7")
    def test_successful_creation_of_second_season(self):
        self.show.add_episode('Stormborn', 1, 2)
        self.assertEqual(len(self.show.seasons), 2)

    @unittest.skip("Season Evolution 7")
    def test_new_season_has_two_elements(self):
        self.show.add_episode('Stormborn', 1, 2)
        self.show.add_episode('valar morghulis', 2, 2)
        self.assertEqual(len(self.show.season(2).episodes), 2)
        self.assertEqual(len(self.show.season(1).episodes), 1)


if __name__ == '__main__':
    unittest.main()
