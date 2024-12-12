from exos.base.pyflix.basic_evening_manager import season_duration


def test_empty_show_len():
    episodes = []
    episode_len = 23
    assert season_duration(episodes, episode_len) == 0

def test_show_with_episodes_len():
    episodes = ["one", "two", "three"]
    episode_len = 20
    assert season_duration(episodes, episode_len) == 60
