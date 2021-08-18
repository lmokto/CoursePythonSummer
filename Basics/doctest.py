import doctest


def add(a, b):
    """Adds, two numbers or lists
    >>> add(1, 2)
    3
    >>> add([1,2,3], [3,5,6])
    [1, 2, 3, 4]
    """
    return a + b


if __name__ == '__main__':
    doctest.testmod()

