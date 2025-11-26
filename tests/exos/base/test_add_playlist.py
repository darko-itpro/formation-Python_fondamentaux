from exos.base.media_utils import add_to_playlist


def test_without_playlist():
    episode = {"title": "my title"}

    playlist = add_to_playlist(episode)

    assert len(playlist) == 1

def test_add_episode_to_empty_playlist():
    episode = {"title": "my title"}
    playlist = []

    new_playlist = add_to_playlist(episode, playlist)

    assert len(playlist) == 0
    assert len(new_playlist) == 1

def test_two_calls():
    episode1= {"title": "my title"}
    episode2= {"title": "my other title"}

    playlist1 = add_to_playlist(episode1)
    assert len(playlist1) == 1

    playlist2 = add_to_playlist(episode2)
    assert len(playlist2) == 1