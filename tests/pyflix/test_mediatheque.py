from pyflix.mediatheque import TvShow

def test_create_tvshow():
    tvshow = TvShow("Breaking Bad")
    assert tvshow.name == "Breaking Bad"
    assert len(tvshow.episodes) == 0

def test_add_first_episode():
    tvshow = TvShow("Breaking Bad")

    tvshow.add_episode("titre", 2, 3, 90, 2014)

    assert len(tvshow.episodes) == 1
