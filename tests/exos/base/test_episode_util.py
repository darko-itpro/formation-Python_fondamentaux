from exos.base.exo_04 import is_viewed

def test_is_viewed_as_bool():
    episode = ["The new Project", 1, 98, True]
    assert is_viewed(episode) is True

def test_episode_not_viewed_as_bool():
    episode = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode) is False

def test_is_viewed_as_int():
    episode = ["The new Project", 1, 98, 4]
    assert is_viewed(episode) is True

def test_is_not_viewed_as_int():
    episode = ["The new Project", 1, 98, 0]
    assert is_viewed(episode) is False

def test_is_not_viewed_without_view():
    episode = ['Installing the softwares', 2, 42]
    assert is_viewed(episode) is False
