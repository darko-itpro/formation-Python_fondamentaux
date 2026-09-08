from exos.episodes_utils import is_viewed

def test_episode_viewed_as_bool():
    episode = ["The new Project", 1, 98, True]
    assert is_viewed(episode) is True


def test_episode_not_viewed_as_count():
    episode = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode) is False


def test_episode_viewed_as_int():
    episode = ["The new Project", 1, 98, 4]
    assert is_viewed(episode) is True
    
def test_episode_not_viewed_as_int():
    episode = ["The new Project", 1, 98, 0]
    assert is_viewed(episode) is False

def test_episode_not_viewed_without_vieed():
    episode = ["The new Project", 1, 98, ]
    assert is_viewed(episode) is False
