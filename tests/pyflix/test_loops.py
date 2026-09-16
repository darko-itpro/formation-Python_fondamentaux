from pyflix.media_utils import find_first_unseen_episode, get_playlist_from


def test_find_first_unseen_episode():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
              {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
              {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': True},
              {'duration': 19, 'title': 'The Planetarium Collision', 'viewed': False},
              {'duration': 19, 'title': 'The Imitation Perturbation'},
              {'duration': 19, 'title': 'The Grant Allocation Derivation', 'viewed': True},
              ]

    assert find_first_unseen_episode(season) == 4

def test_find_first_unseen_episode_all_viewed():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
              {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
              {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': True},
              ]

    assert find_first_unseen_episode(season) == 4

def test_get_playlist_from():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
              {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
              {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': True},
              {'duration': 19, 'title': 'The Planetarium Collision', 'viewed': False},
              {'duration': 19, 'title': 'The Imitation Perturbation'},
              {'duration': 19, 'title': 'The Grant Allocation Derivation', 'viewed': True},
              ]

    assert len(get_playlist_from(season)) == 3

def test_get_playlist_from_all_viewed():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
              {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
              {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': True},
              ]

    assert len(get_playlist_from(season)) == 0
