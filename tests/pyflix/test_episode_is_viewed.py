from demos.episodes_utils import is_viewed

def test_episode_is_viewed():
    episode_viewed = ["The new Project", 1, 98, True]
    assert is_viewed(episode_viewed) is True

def test_episode_is_not_viewed():
    episode_not_viewed = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode_not_viewed) is False

def test_episode_is_viewed_as_count():
    episode_viewed = ["The new Project", 1, 98, 2]
    assert is_viewed(episode_viewed) is True

def test_episode_is_not_viewed_as_count():
    episode_viewed = ["The new Project", 1, 98, 0]
    assert is_viewed(episode_viewed) is False
