from demos.episodes_utils import is_viewed

def test_episode_not_viewed():
    episode = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode) is False

def test_episode_viewed():
    episode = ['Installing the softwares', 2, 42, True]
    assert is_viewed(episode) is True

def test_episode_as_count_viewed():
    episode = ['Installing the softwares', 2, 42, 5]
    assert is_viewed(episode) is True

def test_episode_as_count_not_viewed():
    episode = ['Installing the softwares', 2, 42, 0]
    assert is_viewed(episode) is False
