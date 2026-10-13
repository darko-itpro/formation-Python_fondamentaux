from exos.episode_utils import is_viewed

def test_episode_is_viewed():
    episode = ["The new Project", 1, 98, True]
    assert is_viewed(episode) is True

def test_episode_is_not_viewed():
    episode = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode) is False
    
def test_episode_is_viewed_as_count():
    episode = ["The new Project", 1, 98, 5]
    assert is_viewed(episode) is True

def test_episode_is_not_viewed_as_count():
    episode = ['Installing the softwares', 2, 42, 0]
    assert is_viewed(episode) is False

def test_episode_without_viewed():
    episode = ['Installing the softwares', 2, 42]
    assert is_viewed(episode) is False
