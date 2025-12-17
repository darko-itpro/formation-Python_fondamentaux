from exos.base.exo_loops import get_first_unseen_episode

def test_find_first_unseen_element():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
             {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True},
             {'duration': 20, 'title': 'The Procreation Calculation', "viewed": False},
             {'duration': 19, 'title': 'The Tam Turbulence'},]

    assert get_first_unseen_episode(season) == 2