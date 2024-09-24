from demos.myhome import confort

def test_too_hot():
    assert confort(30) == "chaud"

def test_too_cold():
    assert confort(10) == "froid"

def test_is_cool():
    assert confort(20) == "bon"

def test_limit_cold():
    assert confort(18) == "bon"

def test_limit_hot():
    assert confort(26) == "chaud"
