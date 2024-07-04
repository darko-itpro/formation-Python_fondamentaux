from exos_correction.media_utils_list import is_viewed

def test_episode_is_viewed():
    episode = ["The new Project", 1, 98, True]
    assert is_viewed(episode) is True

def test_episode_is_not_viewed():
    episode = ["The other Project", 2, 54, False]
    assert is_viewed(episode) is False


def test_episode_is_viewed_as_count():
    episode = ["The new Project", 1, 98, 3]
    assert is_viewed(episode) is True


def test_episode_is_not_viewed_as_count():
    episode = ["The other Project", 2, 54, 0]
    assert is_viewed(episode) is False

def test_episode_without_viewed():
    episode = ["The new Project", 1, 98]
    assert is_viewed(episode) is False
