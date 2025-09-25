import pytest
from exos.base.exo_loops import get_playlist, find_first_unseen_episode


@pytest.fixture
def season():
    episodes = [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
                {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
                {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False},
                {'title': 'The Tam Turbulence', 'duration': 19},
                {'title': 'The Planetarium Collision', 'duration': 19, 'viewed': False},
                {'title': 'The Imitation Perturbation', 'duration': 19},
                {'title': 'The Grant Allocation Derivation', 'duration': 19, 'viewed': False},
                {'title': 'The Consummation Deviation', 'duration': 22},
                ]
    return episodes

@pytest.fixture
def set_episodes_as_viewed(season):
    for episode in season:
        episode['viewed'] = True


@pytest.fixture
def set_episodes_as_not_viewed(season):
    for episode in season:
        episode['viewed'] = False

def test_find_first_unseen_episode_all_viewed(season, set_episodes_as_viewed):
    assert find_first_unseen_episode(season) == tuple()


def test_find_first_unseen_episode_none_viewed(season, set_episodes_as_not_viewed):
    assert find_first_unseen_episode(season) == (0, {'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': False})

def test_find_first_unseen_episode(season):
    assert find_first_unseen_episode(season) == (2, {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False})

def test_playlist_creation(season):
    playlist = get_playlist(season)
    assert len(playlist) == 6
    assert playlist[0]['title'] == 'The Procreation Calculation'
