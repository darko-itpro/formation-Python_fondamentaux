"""
Module de contrôle du confort à la maison… Ou plutôt, qui va le simuler.
"""

def confort(temperature:int):
    if temperature > 26:
        return "Chaud"
    elif temperature < 18:
        return "froid"
    else:
        return "bon"

