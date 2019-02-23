"""A small test suite for our LinkedList implementation from lecture."""

from lecture_linked_list import LinkedList
from typing import List


def setup_linked_list(items: List[object]) -> LinkedList:
    """Create a linked list containing the values in items."""
    ll = LinkedList()
    for item in items:
        ll.append(item)
    return ll


def test_eq_two_lists_same() -> None:
    """Test equality for two lists with the same elements"""
    ll1 = setup_linked_list([108, 148, 165])
    ll2 = setup_linked_list([108, 148, 165])

    assert ll1 == ll2


def test_eq_two_lists_same_length() -> None:
    """Test equality for two lists with the same length but
    different elements."""
    ll1 = setup_linked_list([108, 148, 165])
    ll2 = setup_linked_list([108, 148, 207])

    assert not (ll1 == ll2)


def test_eq_two_lists_different_length() -> None:
    """Test equality for two lists with different lengths."""
    ll1 = setup_linked_list([108, 148, 165])
    ll2 = setup_linked_list([108, 148, 165, 207])

    assert not (ll1 == ll2)


def test_getitem_at_start() -> None:
    """Test getting the first item in the list."""
    ll1 = setup_linked_list([108, 148, 165])
    assert ll1[0] == 108


def test_getitem_at_end() -> None:
    """Test getting the last item in the list"""
    ll1 = setup_linked_list([108, 148, 165])
    assert ll1[2] == 165


def test_getitem_out_of_bounds() -> None:
    """Test getting an index that is out of bounds"""
    ll1 = setup_linked_list([108, 148, 165])
    # One way to test this, there are likely other (perhaps better) ways,
    # but this will do given what we know so far.
    try:
        ll1[3]
        assert False
    except IndexError:
        assert True
    except:
        assert False


def test_insert_empty() -> None:
    """Test inserting into an empty linked list"""
    ll = LinkedList()
    ll.insert(0, 'cat')
    expected = setup_linked_list(['cat'])
    assert ll == expected


def test_insert_len_one_front() -> None:
    """Test inserting at the front of a single element linked list"""
    ll = setup_linked_list(['cat'])
    ll.insert(0, 'dog')
    expected = setup_linked_list(['dog', 'cat'])
    assert ll == expected


def test_insert_len_one_end() -> None:
    """Test inserting at the end of a single element linked list"""
    ll = setup_linked_list(['cat'])
    ll.insert(1, 'dog')
    expected = setup_linked_list(['cat', 'dog'])
    assert ll == expected


def test_insert_middle() -> None:
    """Test inserting into the middle of a linked list"""
    ll = setup_linked_list(['cat', 'dog', 'emu', 'fox'])
    ll.insert(2, 'wombat')
    expected = setup_linked_list(['cat', 'dog', 'wombat', 'emu', 'fox'])
    assert ll == expected


def test_insert_invalid_index() -> None:
    """Test that an IndexError is raised when inserting out of bounds."""
    ll = setup_linked_list(['cat', 'dog', 'emu', 'fox'])
    try:
        ll.insert(99, 'wombat')
        assert False
    except IndexError:
        assert True
    except:
        assert False
    try:
        ll.insert(-2, 'wombat')
        assert False
    except IndexError:
        assert True
    except:
        assert False

if __name__ == '__main__':
    import pytest
    pytest.main(['test_lecture_linked_list.py'])
