import pytest
from exos_corrections.exo_loops import get_playlist_from

@pytest.fixture
def season_8_ep_3v():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
              {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
              {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': False},
              {'duration': 19, 'title': 'The Planetarium Collision'},
              {'duration': 19, 'title': 'The Imitation Perturbation', 'viewed': False},
              {'duration': 19, 'title': 'The Grant Allocation Derivation'},
              {'duration': 22, 'title': 'The Consummation Deviation', 'viewed': False}]
    return season

@pytest.fixture
def playlist_all_viewed(season_8_ep_3v):
    for episode in season_8_ep_3v:
        episode["viewed"] = True
    return season_8_ep_3v

@pytest.fixture
def playlist_of_5(season_8_ep_3v):
    return season_8_ep_3v[3:]

def test_first_episode(season_8_ep_3v):
    assert len(get_playlist_from(season_8_ep_3v)) == 5

def test_all_viewed(playlist_all_viewed):
    assert get_playlist_from(playlist_all_viewed) == []