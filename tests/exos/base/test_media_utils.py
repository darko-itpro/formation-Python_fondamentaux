from exos.base.media_utils import is_viewed

def test_is_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    assert is_viewed(episode) is True

#{"title": "The Conjugal Configuration", "duration": 20, "viewed": 3}
#{"title": "The Conjugal Configuration", "duration": 20, "viewed": 3, "year": 2019}

def test_is_not_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    assert is_viewed(episode) is False
#{"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}
#{"title": "The Conjugal Configuration", "duration": 20}
#{"title": "The Conjugal Configuration", "duration": 20, "year":2018}