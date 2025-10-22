import pytest
from exos.base.episode_utils import find_first_unseen_episode, get_playlist_from

@pytest.fixture
def episodes():
    return [
        {'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
        {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
        {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False},
        {'title': 'The Tam Turbulence', 'duration': 19},
        {'title': 'The Planetarium Collision', 'duration': 19, 'viewed': False},
        {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
        {'title': 'The Grant Allocation Derivation', 'duration': 19},
    ]

@pytest.fixture
def set_all_episodes_as_viewed(episodes):
    for episode in episodes:
        episode["viewed"] = True

@pytest.fixture
def with_empty_list(episodes):
    episodes.clear()

def test_get_first_unseen_episode(episodes):
    assert find_first_unseen_episode(episodes) == (2, {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False})

def test_get_first_unseen_episode_with_all_viewed(episodes, set_all_episodes_as_viewed):
    assert find_first_unseen_episode(episodes) == None

def test_get_first_unseen_episode_on_empty_list(episodes, with_empty_list):
    assert find_first_unseen_episode(episodes) == None

def test_get_playlist_from_with_some_unseen_episodes(episodes):
    playlist = get_playlist_from(episodes)
    assert len(playlist) == 5
    assert playlist[0]['title'] == 'The Procreation Calculation'
    assert playlist[-1]['title'] == 'The Grant Allocation Derivation'

def test_get_playlist_from_with_all_viewed_episodes(episodes, set_all_episodes_as_viewed):
    playlist = get_playlist_from(episodes)
    assert playlist == []