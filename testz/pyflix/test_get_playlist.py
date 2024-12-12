import pytest
from exos.base.pyflix.evening_manager import get_playlist_from

@pytest.fixture
def show_7ep_3viewed():
    return [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
            {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
            {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
            {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': False},
            {'title': 'The Planetarium Collision', 'duration': 19},
            {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
            {'title': 'The Grant Allocation Derivation', 'duration': 19},
            ]


@pytest.fixture
def show_7ep_non_viewed(show_7ep_3viewed):
    show= show_7ep_3viewed
    for ep in show:
        if ep.get("viewed"):
            ep["viewed"] = False
    return show

@pytest.fixture
def show_all_viewed(show_7ep_3viewed):
    show = show_7ep_3viewed
    for ep in show:
        ep["viewed"] = True
    return show



def test_basic_extraction_from_show(show_7ep_3viewed):
    show = show_7ep_3viewed
    playlist = get_playlist_from(show)
    assert len(playlist) == 4

def test_all_viewed(show_all_viewed):
    show = show_all_viewed
    playlist = get_playlist_from(show)
    assert len(playlist) == 0