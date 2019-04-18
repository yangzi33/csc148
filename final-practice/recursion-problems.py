"""Demonstration of various ways that recursion can go wrong.
"""

from typing import List


# ===== Example 1 =====
def nested_sum(obj) -> int:
    """Return the sum of all integers in obj.

    >>> nested_sum([1, 2, [3, 4, 5], [[6]], 7])
    28
    """
    if isinstance(obj, int):
        return obj
    else:
        r = 0
        for sublist in obj:
            r += nested_sum(sublist)

        return r


# ===== Example 2 =====
def factorial(n):
    """Return n factorial.

    >>> factorial(5)
    120
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# ===== Example 3 =====
def f(n: int) -> int:
    """Just a recursion demo.

    >>> f(4)
    6
    >>> f(5)
    6
    """
    if n == 0:
        return 1
    else:
        return n + f(n - 2)


# ===== Example 4 =====
def factorial_1(n):
    """Return n factorial.

    >>> factorial_1(5)
    120
    """
    if n < 2:
        return 1
    return n * factorial(n - 1)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(bsearch(lst, 0, len(lst), 5))
