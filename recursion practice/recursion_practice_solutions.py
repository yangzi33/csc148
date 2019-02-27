def palindrome(s: str) -> bool:
    """
    >>> palindrome('moon')
    False
    >>> palindrome('noon')
    True
    """
    # for i in range(len(s)):
    #     if s[i] == s[len(s) - 1 - i]:
    #         pass
    #     else:
    #         return False
    # return True
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
    return reverse_words(s[1:]) + s[0]


def length(s) -> int:
    """
    >>> length('abc')
    3
    """
    if len(s) == 1:
        return 1
    return 1 + length(s[1:])


def sum_of_digit(x: int) -> int:
    """
    Return the sum of the s by adding up every single digit.

    Precondition: s is num in str type.
    >>> sum_of_digit(123)
    6
    >>> sum_of_digit(145)
    10
    """
    # count = 0
    # for n in s:
    #     count += int(n)
    # return count
    if x == 1:
        return 1
    return x % 10 + sum_of_digit(int(x / 10))


def sum_n(n: int) -> int:
    """ Return the sum of integer from 1 to n.
    >>> sum_n(3)
    6
    >>> sum_n(5)
    15
    """
    if n == 1:
        return 1
    return n + sum_n(n - 1)


def product_n(n: int) -> int:
    """ Return the production of integer from 1 to n.
    >>> product_n(4)
    24
    >>> product_n(2)
    2
    """
    if n <= 1:
        return 1
    return n * product_n(n - 1)


def count_zero(list_: list) -> int:
    """ Return the numbers of zeros in l.
    >>> count_zero([1, 2, 3])
    0
    >>> count_zero([0, 0, 0, 0])
    4
    >>> count_zero([0, 1, 2, 3])
    1
    """
    if not isinstance(list_, list):
        if list_ == 0:
            return 1
        else:
            return 0
    else:
        acc = 0
        for item in list_:
            acc += count_zero(item)
        return acc


def find_min(l: list) -> list:
    """ Return the minimum element in l.
    >>> find_min([1, 2, 3])
    1
    >>> find_min([2, 3, 4])
    2
    """
    if len(l) == 1:
        return l[0]
    return min(l[0], find_min(l[1:]))


def count_lists(l: list) -> int:
    """ Return the number of lists in l.
    >>> count_lists([5, [2, 1], []])
    3
    """
    if not isinstance(l, list):
        return 0
    else:
        acc = 0
        for sub in l:
            acc += count_lists(sub)
        return acc + 1


def count_odd(obj) -> int:
    """ Return number of odd element in obj.
    >>> count_odd([1, [2, 3], [4, 5]])
    3
    """
    if isinstance(obj, int):
        return obj % 2
    else:
        acc = 0
        for sub in obj:
            acc += count_odd(sub)
        return acc


def depth(obj) -> int:
    """ Return 0 if obj is a non_list, or 1 + maximum depth
    of element of obj, a possibly nested list of objects.
    >>> depth([1, [2, 3], [2, 3, [4]]])
    3
    """
    if not isinstance(obj, list):
        return 0
    if not obj:
        return 1
    else:
        acc = []
        for sub in obj:
            acc.append(depth(sub))
        return max(acc) + 1


def gather_items(obj) -> list:
    """ Return one list that contains all elements in the nested list object
    >>> gather_items([1, 2, [3, 4]])
    [1, 2, 3, 4]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        acc = []
        for sub in obj:
            acc.extend(gather_items(sub))
        return acc


def gather_odds(obj) -> list:
    """ Return one list that contains all odd elements in the nested list
    >>> gather_odds([1, [2, 3, [5]]])
    [1, 3, 5]
    """
    if isinstance(obj, int):
        if obj % 2 == 1:
            return [obj]
        else:
            return []
    else:
        acc = []
        for sub in obj:
            acc.extend(gather_odds(sub))
        return acc


def convert_to_str(obj) -> None:
    """Convert all element in nested list obj into string.
    >>> list_ = [1, 2, [3, 4]]
    >>> convert_to_str(list_)
    >>> list_ == ['1', '2', ['3', '4']]
    True
    """
    if isinstance(obj, list):
        for i in range(len(obj)):
            if isinstance(obj[i], list):
                convert_to_str(obj[i])
            else:
                obj[i] = str(obj[i])


def get_depth_d(obj, d: int) -> list:
    """Return a list contains the item in the depth d.
    >>> get_depth_d([1, [2, 3, [4, 5]]], 3)
    [4, 5]
    """
    if not isinstance(obj, list):
        if d == 0:
            return [obj]
        else:
            return []
    else:
        acc = []
        if d == 0:
            return []
        for sub in obj:
            acc.extend(get_depth_d(sub, d - 1))
        return acc


def count_above_depth(obj, d) -> int:
    """Return the number of obj above the depth d.
    >>> count_above_depth([1, [2, 3, [4, [5]]]], 2)
    1
    """
    if not isinstance(obj, list):
        if d > 0:
            return 1
        else:
            return 0
    else:
        acc = 0
        for sub in obj:
            acc += count_above_depth(sub, d - 1)
        return acc


def count_below_depth(obj, d) -> int:
    """Return the number of obj below the depth d.
    >>> count_below_depth([1, [2, 3, [4, [5]]]], 2)
    4
    """
    if not isinstance(obj, list):
        if d <= 0:
            return 1
        else:
            return 0
    else:
        acc = 0
        for sub in obj:
            acc += count_below_depth(sub, d - 1)
        return acc


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
    if not s:
        return ['']
    ans = []
    for i in range(len(s)):
        rest = ''
        for j in range(len(s)):
            if i != j:
                rest += s[j]
        perm = all_permutation(rest)
        for sub in perm:
            ans.append(s[i] + sub)
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()
