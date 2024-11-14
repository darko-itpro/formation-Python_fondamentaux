from exos_correction.base.episode_utils_legacy import is_viewed

def test_episode_as_count_viewed():
    episode = ["The new Project", 1, 98, 5]
    assert is_viewed(episode) is True

def test_episode_as_count_not_viewed():
    episode = ['Installing the softwares', 2, 42, 0]
    assert is_viewed(episode) is False

def test_episode_without_viewed_not_viewed():
    episode = ['Installing the softwares', 2, 42]
    assert is_viewed(episode) is False