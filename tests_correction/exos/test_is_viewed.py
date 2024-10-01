import pytest
from exos_correction.base.episodes_utils import is_viewed

test_data = [(["The new Project", 1, 98, True], True),
             (['Installing the softwares', 2, 42, False], False),
             (["The new Project", 1, 98, 2], True),
             (['Installing the softwares', 2, 42, 0], False),
             (['Installing the softwares', 2, 42], False)
             ]

@pytest.mark.parametrize("episode, expected", test_data)
def test_episode_not_viewed_without_viewed(episode, expected):
    assert is_viewed(episode) is expected
