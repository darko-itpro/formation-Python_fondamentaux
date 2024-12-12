import pytest

@pytest.fixture
def playlist_of_7():
    return [{'title': 'The Conjugal Configuration', 'duration': 20, 'viewed': False},
            {'title': 'The Wedding Gift Wormhole', 'duration': 21},
            {'title': 'The Procreation Calculation', 'duration': 20, 'viewed': False},
            {'title': 'The Tam Turbulence', 'duration': 19, 'viewed': False},
            {'title': 'The Planetarium Collision', 'duration': 19},
            {'title': 'The Imitation Perturbation', 'duration': 19, 'viewed': False},
            {'title': 'The Grant Allocation Derivation', 'duration': 19},
            ]
