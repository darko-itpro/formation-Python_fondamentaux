import pytest
from exos.base.media_utils import add_to_playlist

def test_data_not_episode_must_raise():
    episode = {"duration": 89}

    with pytest.raises(ValueError):
        add_to_playlist(episode)
