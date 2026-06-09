from exos.base.media_utils_v1 import is_viewed

def test_episode_viewed():
    episode = ["The new Project", 1, 98, True] # Arrange

    result = is_viewed(episode) # Act

    assert result is True # Assert

def test_episode_not_viewed():
    episode = ['Installing the softwares', 2, 42, False]

    assert is_viewed(episode) is False

def test_episode_viewed_as_count():
    episode = ['Installing the softwares', 2, 42, 3]

    assert is_viewed(episode) is True

def test_episode_not_viewed_as_count():
    episode = ['Installing the softwares', 2, 42, 0]
    assert is_viewed(episode) is False

def test_episode_not_viewed_without_viewed():
    episode = ['Installing the softwares', 2, 42]
    assert is_viewed(episode) is False
