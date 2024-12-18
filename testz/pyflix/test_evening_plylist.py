from exos_correction.base.exo_lists import get_playlist

def test_somethin():
    episodes = ["titre1", "titre2", "titre2"]
    available_time = 30
    episode_duration = 14
    playlist = get_playlist(episodes, available_time, episode_duration)
    assert len(playlist) == 2
