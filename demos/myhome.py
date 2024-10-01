"""
Module de contrôle du confort à la maison… Ou plutôt, qui va le simuler.
"""

def confort(temperature:int|str) -> str:
    temperature = int(temperature)

    value = "bon"
    if temperature > 26:
        value = "chaud"
    elif temperature < 18:
        value = "froid"

    return value
