import pytest
from demos.episodes_utils_lists import is_viewed

test_data = [
    (['Installing the softwares', 2, 42, False], False),
    (['Installing the softwares', 2, 42, True], True),
    (['Installing the softwares', 2, 42, 0], False),
    (['Installing the softwares', 2, 42, 5], True),
    (['Installing the softwares', 2, 42], False),
]

@pytest.mark.parametrize("episode, expected", test_data)
def test_episode_not_viewed(episode, expected):
    assert is_viewed(episode) is expected
