def add(a, b):
    """
        Illustration d'un Doctest

        :Example:

        >>> add(1, 2)
        2
        >>> add(2.1, 3.4)
        5.5

    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()