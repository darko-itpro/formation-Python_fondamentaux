import pytest
from pyflix.media_utils import get_first_unseen_episode, get_playlist_from

@pytest.fixture
def episode_not_viewed():
    return {'title': 'The Consummation Deviation', 'duration': 22}

@pytest.fixture
def season(episode_not_viewed):
    
    episodes = [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
              {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
              {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
              {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': True},
              {'title': 'The Planetarium Collision', 'duration': 19, 'viewed': False},
              {'title': 'The Imitation Perturbation', 'duration': 19},
              {'title': 'The Grant Allocation Derivation', 'duration': 19, 'viewed': False},
              ]
    episodes.append(episode_not_viewed)
    return episodes

@pytest.fixture
def all_episodes_viewed(season):
    for episode in season:
        episode['viewed'] = True

def test_get_first_unseen_when_all_viewed(season, all_episodes_viewed):
    position = get_first_unseen_episode(season)
    assert position == 7    

def test_get_first_unseen(season):
    position = get_first_unseen_episode(season)
    assert position == 4

def test_get_playlist_from(season):
    playlist = get_playlist_from(season)
    assert len(playlist) == 4
    assert playlist[0]["title"] == "The Planetarium Collision"
