import pytest
from exos_correction.exo_loops import get_playlist_from

@pytest.fixture
def season_6ep_3viewed():
    return [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
            {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
            {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
            {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': False},
            {'duration': 19, 'title': 'The Planetarium Collision'},
            {'duration': 19, 'title': 'The Imitation Perturbation', 'viewed': False}]

@pytest.fixture
def season_all_viewed(season_6ep_3viewed):
    return season_6ep_3viewed[:3]

@pytest.fixture
def season_none_viewed(season_6ep_3viewed):
    return season_6ep_3viewed[3:]


def test_playlist(season_6ep_3viewed):
    playlist = get_playlist_from(season_6ep_3viewed)
    assert len(playlist) == 3
