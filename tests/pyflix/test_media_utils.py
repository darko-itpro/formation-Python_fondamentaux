import pytest
from exos.base.media_utils import is_viewed

test_data = [({"title": "The Conjugal Configuration", "duration": 20, "viewed": True}, True),
             ({"title": "The Conjugal Configuration", "duration": 20, "viewed": False}, False),
             ]

@pytest.mark.parametrize("episode, expected", test_data)
def test_episode_is_viewed(episode, expected):
    assert is_viewed(episode) is expected