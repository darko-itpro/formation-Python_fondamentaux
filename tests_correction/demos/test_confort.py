# test_confort.py

from demos.myhome import confort

def test_hot_temp():
    assert confort(30) == "chaud"

def test_cold_temp():
    assert confort(10) == "froid"

def test_warm_temp():
    assert confort(20) == "bon"

def test_warm_temp_as_str():
    assert confort('20') == "bon"

def test_limit_hot():
    assert confort(26) == "bon"

def test_limit_cold():
    assert confort(18) == "bon"
