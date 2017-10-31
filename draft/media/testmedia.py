#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest

from draft.media import basemedia


class CreateEpisode(unittest.TestCase):

    def test_create_episode_without_season(self):
        episode = basemedia.Episode("Title", 1)
        self.assertIsNotNone(episode)

    def test_create_episode_with_season(self):
        episode = basemedia.Episode("Title", 1, 1)
        self.assertIsNotNone(episode)

    def test_title_accessible(self):
        episode = basemedia.Episode("Title", 1)
        self.assertEqual(episode.title, "Title")

    def test_should_not_assign_title(self):
        episode = basemedia.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.title = 'Other title'

    def test_number_accessible(self):
        episode = basemedia.Episode("Title", 1)
        self.assertEqual(episode.number, 1)

    def test_should_not_assign_number(self):
        episode = basemedia.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.number = 2

    def test_season_accessible(self):
        episode = basemedia.Episode("Title", 1, 2)
        self.assertEqual(episode.season, 2)

    def test_shouldnt_assign_season(self):
        episode = basemedia.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.season = 2

    def test_without_season_should_be_none(self):
        episode = basemedia.Episode("Title", 1)
        self.assertIsNone(episode.season)

    def test_number_must_be_integer_compatible(self):
        episode = basemedia.Episode('Title', 1)
        self.assertEqual(episode.number, 1)
        episode = basemedia.Episode('Title', "1")
        self.assertEqual(episode.number, 1)
        with self.assertRaises(ValueError):
            basemedia.Episode('Title', "un")

    def test_season_must_be_integer_compatible(self):
        episode = basemedia.Episode('Title', 1, 2)
        self.assertEqual(episode.season, 2)
        episode = basemedia.Episode('Title', 1, "2")
        self.assertEqual(episode.season, 2)
        with self.assertRaises(ValueError):
            basemedia.Episode('Title', 1, "un")

    def test_title_should_be_string_or_raise_error(self):
        with self.assertRaises(ValueError):
            basemedia.Episode(10, 1)

    def test_title_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            basemedia.Episode('', 1)


class CreateShow(unittest.TestCase):

    def test_create_new_show(self):
        show = basemedia.TvShow('Mr. Robot')
        self.assertIsNotNone(show)

    def test_show_name_accessible(self):
        show = basemedia.TvShow('Mr. Robot')
        self.assertEqual(show.name, 'Mr. Robot')

    def test_shouldnt_assign_name(self):
        show = basemedia.TvShow('Mr. Robot')
        with self.assertRaises(AttributeError):
            show.name = 'Dr. Who'


class AccessEpisodes(unittest.TestCase):

    def setUp(self):
        self.show = basemedia.TvShow('Game of Thrones')

    def tearDown(self):
        del self.show

    def test_has_episodes_attr(self):
        self.assertTrue(hasattr(self.show, 'episodes'))

    def test_has_add_episode_attr(self):
        self.assertTrue(hasattr(self.show, 'add_episode'))

    def test_empty_show(self):
        self.assertEqual(len(self.show.episodes()), 0)

    def test_add_episode_with_season_number(self):
        self.show.add_episode("Into the North", 1, 1)
        self.assertEqual(len(self.show.episodes()), 1)

    def test_add_episode_without_season_number(self):
        self.show.add_episode("Into the North", 1)
        self.assertEqual(len(self.show.episodes()), 1)

    def test_should_not_alter_episodes(self):
        episodes = self.show.episodes()
        episodes.append(basemedia.Episode('Intruder', 2))
        self.assertEqual(len(self.show.episodes()), 0)

    def test_should_not_add_same_episode(self):
        self.show.add_episode("Into the North", 1, 1)
        with self.assertRaises(ValueError):
            self.show.add_episode('Kingslayer', 1, 1)


class SeasonEvolution(unittest.TestCase):
    """
    Les tests de cette classe ne passent pas. Vous devez enlever les skip l'un
    après l'autre avec une approche TDD : ne levez qu'un skip et ajoutez le code
    qui fait passer le test.
    """

    def setUp(self):
        self.show = basemedia.TvShow('Game of Thrones')
        self.show.add_episode("Into the North", 1, 1)

    def tearDown(self):
        del self.show

    @unittest.skip("Evolution 1")
    def test_have_method_season(self):
        self.assertTrue(hasattr(self.show, 'season'))

    @unittest.skip("Evolution 2")
    def test_have_method_seasons(self):
        self.assertTrue(hasattr(self.show, 'seasons'))

    @unittest.skip("Evolution 3")
    def test_season_returns_elements(self):
        self.assertEqual(len(self.show.seasons), 1)

    @unittest.skip("Evolution 4")
    def test_access_season(self):
        self.assertIsNotNone(self.show.season(1))

    @unittest.skip("Evolution 5")
    def test_season_is_object_with_episodes_attr(self):
        self.assertTrue(hasattr(self.show.season(1)), 'episodes')

    @unittest.skip("Evolution 6")
    def test_existing_season_has_one_element(self):
        self.assertEqual(len(self.show.season(1).episodes), 1)

    @unittest.skip("Evolution 7")
    def test_successful_creation_of_second_season(self):
        self.show.add_episode('Stormborn', 1, 2)
        self.assertEqual(len(self.show.seasons), 2)

    @unittest.skip("Evolution 7")
    def test_new_season_has_two_elements(self):
        self.show.add_episode('Stormborn', 1, 2)
        self.show.add_episode('valar morghulis', 2, 2)
        self.assertEqual(len(self.show.season(2)), 2)
        self.assertEqual(len(self.show.season(1)), 1)


if __name__ == '__main__':
    pass