#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest

from training.projects.mediamanager import mediamodel


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

    def test_has_get_episodes_callable_attr(self):
        self.assertTrue(hasattr(self.show, 'get_episodes'))
        self.assertTrue(callable(self.show.get_episodes))

    def test_has_add_episode_callable_attr(self):
        self.assertTrue(hasattr(self.show, 'add_episode'))
        self.assertTrue(callable(self.show.add_episode))

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


class SeasonEvolution(unittest.TestCase):
    """
    Les tests de cette classe ne passent pas. Vous devez enlever les skip l'un
    après l'autre avec une approche TDD : ne levez qu'un skip et ajoutez le code
    qui fait passer le test.
    """

    def setUp(self):
        self.show = mediamodel.TvShow('Game of Thrones')
        self.show.add_episode("Into the North", 1, 1)

    def tearDown(self):
        del self.show

    def test_have_method_season(self):
        self.assertTrue(hasattr(self.show, 'season'))

    def test_have_method_seasons(self):
        self.assertTrue(hasattr(self.show, 'seasons'))

    def test_season_returns_elements(self):
        self.assertEqual(len(self.show.seasons), 1)

    def test_access_season(self):
        self.assertIsNotNone(self.show.season(1))

    def test_season_is_object_with_episodes_attr(self):
        self.assertTrue(hasattr(self.show.season(1), 'episodes'))

    def test_existing_season_has_one_element(self):
        self.assertEqual(len(self.show.season(1).episodes), 1)

    def test_successful_creation_of_second_season(self):
        self.show.add_episode('Stormborn', 1, 2)
        self.assertEqual(len(self.show.seasons), 2)

    def test_new_season_has_two_elements(self):
        self.show.add_episode('Stormborn', 1, 2)
        self.show.add_episode('valar morghulis', 2, 2)
        self.assertEqual(len(self.show.season(2).episodes), 2)
        self.assertEqual(len(self.show.season(1).episodes), 1)


if __name__ == '__main__':
    unittest.main()
