def is_viewed(episode:dict) -> bool:
    return "viewed" in episode and bool(episode["viewed"])