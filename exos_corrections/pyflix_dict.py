# Cette fonction est la même que dans exo_dict
def is_viewed(episode:dict):
    return bool(episode["viewed"]) if "viewed" in episode else False
