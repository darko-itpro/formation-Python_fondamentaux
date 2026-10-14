def is_viewed(episode:list) -> bool:
    try:
        return bool(episode[3])
    except IndexError:
        return False


if __name__ == "__main__":
    print("in is_viewed")

