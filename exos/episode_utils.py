def is_viewed(episode:list) -> bool:
    return len(episode) > 3 and bool(episode[3])


if __name__ == "__main__":
    print("in is_viewed")
