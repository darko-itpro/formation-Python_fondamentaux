from exos.pyflix.mediatheque import Episode

def test_episodes_are_equal():
    ep1 = Episode("Rose", 1, 1, 54, 2006)
    ep2 = Episode("Rose", 1, 1, 54, 2006)
    assert ep1 == ep2
