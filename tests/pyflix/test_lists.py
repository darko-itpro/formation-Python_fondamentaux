from pyflix.media_utils import episodes_duration, get_time_limited_playlist

def test_episodes_duration():
    episodes = ['The Conjugal Configuration',
                'The Wedding Gift Wormhole',
                'The Procreation Calculation',
                'The Tam Turbulence',
                'The Planetarium Collision',
                'The Imitation Perturbation', ]

    episode_duration = 20

    assert episodes_duration(episodes, episode_duration ) == 120

def test_empty_episodes_duration():
    episodes = []

    episode_duration = 20

    assert episodes_duration(episodes, episode_duration ) == 0

def test_evening_playlist():
    episodes = ['The Conjugal Configuration',
                'The Wedding Gift Wormhole',
                'The Procreation Calculation',
                'The Tam Turbulence',
                'The Planetarium Collision',
                'The Imitation Perturbation', ]

    episode_duration = 20
    max_duration = 72

    playlist = get_time_limited_playlist(episodes, episode_duration, max_duration)

    assert len(playlist) == 3
    assert playlist[0] == 'The Conjugal Configuration'
