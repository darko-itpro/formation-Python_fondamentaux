import pytest
from demos.demo_except import tout_sauf_42

def test_raise():
    value = 42
    with pytest.raises(ValueError):
        tout_sauf_42(value)