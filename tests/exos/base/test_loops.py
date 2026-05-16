import pytest
from exos.base.exo_loops import find_first_unseen_episode, get_playlist_from

@pytest.fixture
def episodes():
    return [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
            {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
            {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
            {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': False},
            {'title': 'The Planetarium Collision', 'duration': 19},
            {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
            {'title': 'The Grant Allocation Derivation', 'duration': 19}, ]

def test_find_first_unseen_episode(episodes):
        index, _ = find_first_unseen_episode(episodes)
        assert index == 3

def test_get_playlist_from(episodes):
        playlist = get_playlist_from(episodes)
        assert len(playlist) == 4
        assert playlist[0]['title'] == 'The Tam Turbulence'
