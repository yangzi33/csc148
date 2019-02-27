from typing import *

def palindrome(s: str) -> bool:
    """
    >>> palindrome('moon')
    False
    >>> palindrome('noon')
    True
    """
    if not s:
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])

def reverse_words(s):
    """
    >>> reverse_words('qwertyuiop')
    'poiuytrewq'
    """
    if len(s) == 1:
        return s
    else:
        return reverse_words(s[1:]) + s[0]


def length(s) -> int:
    """
    >>> length('abc')
    3
    """
    if len(s) == 1:
        return 1
    else:
        return len(s[1:]) + 1


def sum_of_digit(x: int) -> int:
    """
    Return the sum of the s by adding up every single digit.

    Precondition: s is num in str type.
    >>> sum_of_digit(123)
    6
    >>> sum_of_digit(145)
    10
    """
    if x == 1:
        return x
    else:
        return sum_of_digit(int(x / 10)) + x % 10


def sum_n(n: int) -> int:
    """ Return the sum of integer from 1 to n.
    >>> sum_n(3)
    6
    >>> sum_n(5)
    15
    """
    if n == 1:
        return 1
    else:
        return sum_n(n - 1) + n


def product_n(n: int) -> int:
    """ Return the production of integer from 1 to n.
    >>> product_n(4)
    24
    >>> product_n(2)
    2
    """
    if n == 1:
        return 1
    else:
        return product_n(n - 1) * n


def count_zero(list_: list) -> int:
    """ Return the numbers of zeros in l.
    >>> count_zero([1, 2, 3])
    0
    >>> count_zero([0, 0, 0, 0])
    4
    >>> count_zero([0, 1, 2, 3])
    1
    """
    # c = 0
    # for i in list_:
    #     if i == 0:
    #         c += 1
    # return c






def find_min(l) -> int:
    """ Return the minimum element in l.
    >>> find_min([1, 2, 3])
    1
    >>> find_min([2, 3, 4])
    2
    """
    if len(l) == 1:
        return l[0]
    else:
        return min(l[0], find_min(l[1:]))


def count_lists(l: list) -> int:
    """ Return the number of lists in l.
    >>> count_lists([5, [2, 1], []])
    3
    """
    if isinstance(l[0], list):
        return 1
    else:
        c = 0
        for sublist in l:
            c += count_lists(l[1:])

        return c

def count_odd(obj) -> int:
    """ Return number of odd element in obj.
    >>> count_odd([1, [2, 3], [4, 5]])
    3
    """
    if isinstance(obj, int):
        return obj % 2
    else:
        c = 0
        for sublist in obj:
            c += count_odd(sublist)

        return c


def depth(obj) -> int:
    """ Return 0 if obj is a non_list, or 1 + maximum depth
    of element of obj, a possibly nested list of objects.
    >>> depth([1, [2, 3], [2, 3, [4]]])
    3
    """
    pass

def gather_items(obj) -> list:
    """ Return one list that contains all elements in the nested list object
    >>> gather_items([1, 2, [3, 4]])
    [1, 2, 3, 4]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        r = []
        for sublist in obj:
            r += gather_items(sublist)
        return r


def gather_odds(obj) -> list:
    """ Return one list that contains all odd elements in the nested list
    >>> gather_odds([1, [2, 3, [5]]])
    [1, 3, 5]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        r = []
        for sublist in obj:
            if gather_odds(sublist)[0] % 2 == 1:
                r += gather_odds(sublist)
        return r


def convert_to_str(obj) -> None:
    """Convert all element in nested list obj into string.
    >>> list_ = [1, 2, [3, 4]]
    >>> convert_to_str(list_)
    >>> list_ == ['1', '2', ['3', '4']]
    True
    """


def get_depth_d(obj, d: int) -> list:
    """Return a list contains the item in the depth d.
    >>> get_depth_d([1, [2, 3, [4, 5]]], 3)
    [4, 5]
    """
    pass

def count_above_depth(obj, d) -> int:
    """Return the number of obj above the depth d.
    >>> count_above_depth([1, [2, 3, [4, [5]]]], 2)
    1
    """
    pass

def count_below_depth(obj, d) -> int:
    """Return the number of obj below the depth d.
    >>> count_below_depth([1, [2, 3, [4, [5]]]], 2)
    4
    """
    pass

def is_prime(n, k=2):
    if n == 1:
        return False
    if n == 2 or k == n:
        return True
    return n % k != 0 and is_prime(n, k + 1)


def my_sum(n):
    def f(acc, n0):
        if n0 == 0:
            return acc
        return f(acc + n0, n0 - 1)

    return f(0, n)


def f(TL, i):
    stack = [TL]
    while stack:
        p = stack.pop()
        if not p:
            continue
        p[0] = i
        i += 1
        stack.append(p[2])
        stack.append(p[1])
    return i


def all_permutation(s):
    """Return all possible permutations/
    >>> all_permutation('123')
    ['123', '132', '213', '231', '312', '321']
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
