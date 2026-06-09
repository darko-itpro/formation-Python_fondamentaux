def is_viewed(episode:dict):
    return "viewed" in episode and bool(episode["viewed"])