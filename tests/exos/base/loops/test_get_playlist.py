from exos.base.exo_loops import get_first_unseen_episode, get_playlist_from

def test_find_first_unseen_episode():
    show = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
            {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
            {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
            {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': False},
            {'duration': 19, 'title': 'The Planetarium Collision'},
            {'duration': 19, 'title': 'The Imitation Perturbation', 'viewed': False},
            ]

    assert get_first_unseen_episode(show) == (3, {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': False})


def test_get_playlist_from():
    show = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
            {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
            {'duration': 20, 'title': 'The Procreation Calculation', 'viewed': True},
            {'duration': 19, 'title': 'The Tam Turbulence', 'viewed': False},
            {'duration': 19, 'title': 'The Planetarium Collision'},
            {'duration': 19, 'title': 'The Imitation Perturbation', 'viewed': False},
            ]
    playlist = get_playlist_from(show)
    assert len(playlist) == 3
    assert playlist[0]['title'] == 'The Tam Turbulence'