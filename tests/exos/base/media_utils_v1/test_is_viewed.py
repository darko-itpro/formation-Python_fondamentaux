from exos.base.media_utils_v1 import is_viewed

def test_episode_viewed():
    episode = ["The new Project", 1, 98, True] # Arrange

    result = is_viewed(episode) # Act

    assert result is True # Assert

def test_episode_not_viewed():
    episode = ['Installing the softwares', 2, 42, False]

    assert is_viewed(episode) is False
