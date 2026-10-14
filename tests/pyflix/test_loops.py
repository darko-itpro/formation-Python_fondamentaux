from pyflix.media_utils import get_first_unseen_episode, get_playlist_from


def test_get_first_unseen():
    season = [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
              {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
              {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
              {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': True},
              {'title': 'The Planetarium Collision', 'duration': 19, 'viewed': False},
              {'title': 'The Imitation Perturbation', 'duration': 19},
              {'title': 'The Grant Allocation Derivation', 'duration': 19, 'viewed': False},
              {'title': 'The Consummation Deviation', 'duration': 22},
              ]

    position = get_first_unseen_episode(season)
    assert position == 4

def test_get_playlist_from():
    season = [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
              {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
              {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': True},
              {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': True},
              {'title': 'The Planetarium Collision', 'duration': 19, 'viewed': False},
              {'title': 'The Imitation Perturbation', 'duration': 19},
              {'title': 'The Grant Allocation Derivation', 'duration': 19, 'viewed': False},
              {'title': 'The Consummation Deviation', 'duration': 22},
              ]

    playlist = get_playlist_from(season)
    assert len(playlist) == 4
    assert playlist[0]["title"] == "The Planetarium Collision"
