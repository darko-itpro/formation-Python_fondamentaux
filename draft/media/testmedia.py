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


if __name__ == '__main__':
    unittest.main()
