from exos.base.media_utils_lists import is_viewed

def test_is_viewed_with_bool():
    episode = ["The new Project", 1, 98, True]
    assert is_viewed(episode) is True

def test_is_not_viewed_with_bool():
    episode = ["The new Project", 1, 98, False]
    assert is_viewed(episode) is False

def test_is_viewed_with_count():
    episode = ["The new Project", 1, 98, 3]
    assert is_viewed(episode) is True

def test_is_not_viewed_with_count():
    episode = ["The new Project", 1, 98, 0]
    assert is_viewed(episode) is False

def test_is_not_viewed_without_viewed():
    episode = ["The new Project", 1, 98]
    assert is_viewed(episode) is False
