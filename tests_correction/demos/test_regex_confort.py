import pytest
from exos_correction.base.exo_regex import temp_to_natural

test_data = [("Le 18 novembre, il a fait 12°c.", "Le 18 novembre, il a fait froid."),
             ("À 12h39, il a fait 9°c au nord du village.", "À 12h39, il a fait froid au nord du village."),
             ("Cet été du 12 au 20 juillet, il a fait 24°c quand nous étions tous les 4 à la plage.", "Cet été du 12 au 20 juillet, il a fait bon quand nous étions tous les 4 à la plage."),
             ]

@pytest.mark.parametrize('data_in, data_out', test_data)
def test_sentence_converter(data_in, data_out):
    assert temp_to_natural(data_in) == data_out
