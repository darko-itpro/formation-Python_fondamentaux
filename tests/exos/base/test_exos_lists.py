import pytest
from exos.base.exo_lists import episodes_duration

@pytest.fixture
def episodes():
    return ['The Conjugal Configuration',
            'The Wedding Gift Wormhole',
            'The Procreation Calculation',
            'The Tam Turbulence',
            'The Planetarium Collision',
            'The Imitation Perturbation',
            ]

def test_duration_empty_list():
    assert episodes_duration([], 23) == 0

def test_duration_for_episodes(episodes):
    assert episodes_duration(episodes, 23) == 138

def test_negative_value_must_raise(episodes):
    with pytest.raises(ValueError):
        episodes_duration(episodes, -23)
