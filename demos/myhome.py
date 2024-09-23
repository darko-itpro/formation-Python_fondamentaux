"""
Module de contrôle du confort à la maison… Ou plutôt, qui va le simuler.
"""

def confort(temperature:int):
    value = "bon"
    if temperature > 26:
        value = "Chaud"
    elif temperature < 18:
        value = "froid"

    return value

