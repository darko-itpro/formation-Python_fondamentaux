from exos.base.media_utils import add_to_playlist

def test_add_episode_to_empty_playlist():
    episode = {"title": "my title"}
    plaulist = []

    add_to_playlist(episode, plaulist)

    assert len(plaulist) == 1