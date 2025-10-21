import pytest
from exos.base.episode_utils import is_viewed

test_data = [
    (["The new Project", 1, 98, True], True),
    (["The new Project", 1, 98, False], False),
    (["The new Project", 1, 98, 2], True),
    (["The new Project", 1, 98, 0], False),
    (["The new Project", 1, 98], False),
]

@pytest.mark.parametrize("episode, expected", test_data)
def test_episode_viewed(episode, expected):
    assert is_viewed(episode) is expected
