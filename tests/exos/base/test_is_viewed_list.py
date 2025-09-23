from exos.base.episodes_utils import is_viewed

def test_is_viewed_as_bool():
    episode = ["The new Project", 1, 98, True] # setup
    result = is_viewed(episode) # act
    assert result is True # assert
    # No cleanup, not needed

def test_is_not_viewed_as_bool():
    episode = ["The new Project", 1, 98, False]
    assert is_viewed(episode) is False

def test_is_viewed_as_count():
    episode = ["The new Project", 1, 98, 4]
    assert is_viewed(episode) is True

def test_is_not_viewed_as_count():
    episode = ["The new Project", 1, 98, 0]
    assert is_viewed(episode) is False
