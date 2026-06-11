
def tout_sauf_42(value):
    if value == 42:
        raise ValueError(f"J'ai dit pas {value}")
    return value
