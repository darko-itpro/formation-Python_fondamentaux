from exos.base.exo_lists import get_duration

def test_duration_empty_list():
    episodes = []
    duration = 10
    assert get_duration(episodes, duration) == 0

def test_duration_one_episode():
    episodes = ["first"]
    duration = 10
    assert get_duration(episodes, duration) == 10

def test_duration_some_episode():
    episodes = ["first", "second", "third"]
    duration = 10
    assert get_duration(episodes, duration) == 30