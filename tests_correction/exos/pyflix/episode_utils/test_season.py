import pytest

@pytest.fixture
def list_without_episode():
    return []

@pytest.fixture
def list_3_episodes(list_without_episode):
    list_without_episode.append('ep1')
    list_without_episode.append('ep2')
    list_without_episode.append('ep3')
    return list_without_episode


def test_something(list_3_episodes):
    assert len(list_3_episodes) == 3
