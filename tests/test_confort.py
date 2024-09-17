from exos_corrections.myhome import confort

def test_is_cold():
    assert confort(10) == "froid"

def test_is_good():
    assert confort(20) == "bon"

def test_is_hot():
    assert confort(30) == "chaud"

def test_is_good_at_24():
    assert confort(24) == "chaud"

def test_is_good_at_18():
    assert confort(18) == "bon"
