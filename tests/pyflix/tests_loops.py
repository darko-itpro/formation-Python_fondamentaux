from pyflix.media_utils import get_index_first_unseen_episode, get_playlist_from


def test_get_index_first_unseen():
    episodes = [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
                {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
                {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False},
                {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': False},
                {'title': 'The Planetarium Collision', 'duration': 19},
                {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
                ]

    assert get_index_first_unseen_episode(episodes) == 2


def test_get_4_episodes_playlist():
    episodes = [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': True},
                {'title': 'The Wedding Gift Wormhole', 'duration': 21, 'viewed': True},
                {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False},
                {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': False},
                {'title': 'The Planetarium Collision', 'duration': 19},
                {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
                ]

    playlist = get_playlist_from(episodes)
    assert len(playlist) == 4
    assert playlist[0]['title'] == 'The Procreation Calculation'
