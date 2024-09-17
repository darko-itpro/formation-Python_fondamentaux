
def confort(temperature:int):
    value = "froid"

    if temperature >= 24:
        value = "chaud"
    elif temperature >= 18:
        value = "bon"

    return value

