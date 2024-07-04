import pytest
from exos_correction.media_utils import is_viewed

test_data =[
    ({'title': 'The new Project', 'duration': 98, 'number': 2, 'viewed': 3}, True),
    ({'title': 'The new Project',
      'duration': 98,
      'number': 2,
      'viewed': 0}, False),
    ({'title': 'The new Project',
      'duration': 98,
      'number': 2}, False),
    ({'title': 'The new Project',
      'duration': 98,
      'number': 2,
      'year': 2000}, False),
]

@pytest.mark.parametrize('episode,expected_status', test_data)
def test_episode_is_viewed(episode, expected_status):
    assert is_viewed(episode) is expected_status
