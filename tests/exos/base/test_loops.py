import pytest
from exos.base.exo_loops import get_first_unseen_episode, get_playlist_from

@pytest.fixture
def episodes():
    return [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
            {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
            {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
            {'title': 'The Tam Turbulence', 'duration': 19},
            {'title': 'The Planetarium Collision', 'duration': 19, 'viewed': False},
            {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
            {'title': 'The Grant Allocation Derivation', 'duration': 19, 'viewed': True},
            ]

@pytest.fixture
def episodes_all_viewed(episodes):
    for episode in episodes:
        episode['viewed'] = True

    return episodes

def test_get_first_unseen_episode_all_viewed(episodes_all_viewed):
    assert get_first_unseen_episode(episodes_all_viewed) is None

def test_get_first_unseen_episode(episodes):
    _, episode = get_first_unseen_episode(episodes)
    assert episode == {'title': 'The Tam Turbulence', 'duration': 19}

def test_get_first_unseen_episode_index(episodes):
    index, _ = get_first_unseen_episode(episodes)
    assert index == 3

def test_get_playlist(episodes):
    playlist = get_playlist_from(episodes)
    assert len(playlist) == 4
    assert playlist[0]['title'] == 'The Tam Turbulence'
