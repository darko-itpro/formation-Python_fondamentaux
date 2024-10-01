# test_confort.py

from demos.myhome import confort

def test_hot_temp():
    assert confort(30) == "chaud"

def test_cold_temp():
    assert confort(10) == "foid"

def test_warm_temp():
    assert confort(20) == "bon"

