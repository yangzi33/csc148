"""CSC148 Prep 5: Linked Lists

=== CSC148 Winter 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Prep 5.

WARNING: THIS IS AN EXTREMELY INCOMPLETE SET OF TESTS!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
from typing import List

from hypothesis import given
from hypothesis.strategies import integers, lists

from prep5 import LinkedList, _Node


def test_len_empty() -> None:
    """Test LinkedList.__len__ for an empty linked list."""
    lst = LinkedList()
    assert len(lst) == 0


def test_len_three() -> None:
    """Test LinkedList.__len__ on a linked list of length 3."""
    lst = LinkedList()
    node1 = _Node(10)
    node2 = _Node(20)
    node3 = _Node(30)
    node4 = _Node(40)
    node5 = _Node(50)
    node6 = _Node(60)
    node7 = _Node(70)
    node8 = _Node(80)
    node9 = _Node(90)
    node10 = _Node(100)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    lst._first = node1
    assert len(lst) == 10


def test_contains_doctest() -> None:
    """Test LinkedList.__contains__ on the given doctest."""
    lst = LinkedList()
    node1 = _Node(10)
    node2 = _Node(20)
    node3 = _Node(30)
    node4 = _Node(40)
    node5 = _Node(50)
    node6 = _Node(60)
    node7 = _Node(70)
    node8 = _Node(80)
    node9 = _Node(90)
    node10 = _Node(100)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    lst._first = node1

    assert 20 in lst
    assert 100 in lst
    assert 5 not in lst
    assert not (4 in lst)


def test_append_empty() -> None:
    """Test LinkedList.append on an empty list."""
    lst = LinkedList()
    lst.append(1)
    assert lst._first.item == 1

def test_append_one2() -> None:
    """Test LinkedList.append on an empty list."""
    lst = LinkedList()
    node1 = _Node(10)
    node2 = _Node(20)
    node3 = _Node(30)
    node4 = _Node(40)
    node5 = _Node(50)
    node6 = _Node(60)
    node7 = _Node(70)
    node8 = _Node(80)
    node9 = _Node(90)
    node10 = _Node(100)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    lst._first = node1
    lst.append(1)
    assert node10.next.item == 1
    assert lst._first.next.next.next.next.next.next.next.next.next.next.item == 1


def test_append_one() -> None:
    """Test LinkedList.append on a list of length 1."""
    lst = LinkedList()
    lst._first = _Node(1)
    lst.append(2)
    assert lst._first.next.item == 2


if __name__ == '__main__':
    import pytest
    pytest.main(['prep5_sample_test.py'])
