import pytest
from exos_correction.pyflix.episode_utils import is_viewed

test_data = [
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": True}, True),
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 3}, True),
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": False}, False),
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}, False),
    ({"title": "The Conjugal Configuration", "duration": 20}, False),
]

@pytest.mark.parametrize("episode, expected", test_data)
def test_episode_not_viewed_without_viewed(episode, expected):
    assert is_viewed(episode) is expected
