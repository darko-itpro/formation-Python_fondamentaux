import pytest
from exos.base.episode_utils import find_first_unseen_episode

def test_raises_exept():
    with pytest.raises(TypeError):
        find_first_unseen_episode(None)