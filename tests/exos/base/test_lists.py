import pytest
from exos.base.exo_list import collection_duration, evening_playlist

@pytest.fixture
def episodes():
    return ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

@pytest.fixture
def short_playlist_4_episodes(episodes):
    return episodes[:4]

def test_sleep_time(episodes):
    remaining_time = 30
    episode_duration = 12
    assert evening_playlist(episodes, remaining_time, episode_duration) == ["one", "two"]

def test_sleep_time_empty_lit():
    remaining_time = 30
    episode_duration = 12
    assert evening_playlist([], remaining_time, episode_duration) == []



def test_empty_collection_duration():
    episodes = []
    episode_duration = 12
    assert collection_duration(episodes, episode_duration) == 0

def test_collection_duration_with_elements(short_playlist_4_episodes):
    episode_duration = 12
    assert collection_duration(short_playlist_4_episodes, episode_duration) == 48