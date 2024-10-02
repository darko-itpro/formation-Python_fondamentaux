import pytest
from exos_correction.base.exo_loops import get_playlist_from

@pytest.fixture
def season_7ep_3_viewed():
    return [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
            {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
            {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
            {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': False},
            {'title': 'The Planetarium Collision', 'duration': 19},
            {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
            {'title': 'The Grant Allocation Derivation', 'duration': 19, 'viewed': False},
            ]


@pytest.fixture
def season_7ep_all_viewed(season_7ep_3_viewed):
    for ep in season_7ep_3_viewed:
        ep["viewed"] = True
    return season_7ep_3_viewed


@pytest.fixture
def season_7ep_last_not_viewed(season_7ep_all_viewed):
    season_7ep_all_viewed[-1]["viewed"] = False
    return season_7ep_all_viewed


def test_extract_from_season(season_7ep_3_viewed):
    assert len(get_playlist_from(season_7ep_3_viewed)) == 4

def test_extract_where_1_episode_left(season_7ep_last_not_viewed):
    assert len(get_playlist_from(season_7ep_last_not_viewed)) == 1

def test_extract_from_all_viewed(season_7ep_all_viewed):
    assert len(get_playlist_from(season_7ep_all_viewed)) == 0

def test_extract_from_empty_list():
    assert len(get_playlist_from([])) == 0
