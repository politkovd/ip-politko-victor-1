# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(3) == 5

def third(x):
    """
    >>> third(12)
    4
    >>>
    """
    return x / 3


if __name__ == '__main__':
    import doctest
    doctest.testmod()