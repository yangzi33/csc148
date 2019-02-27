"""Linked List

=== CSC148 Winter 2019 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.
"""
from __future__ import annotations

from typing import Any, Callable, Optional, Union


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        self._first = None

    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.
        """
        if self._first is None:
            self._first = _Node(item)
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = _Node(item)

    def print_items(self) -> None:
        """Print the items in this linked list.
        """
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def __len__(self):
        r = 0
        curr = self._first

        while curr is not None:
            curr = curr.next
            r += 1
        return r

    def __eq__(self, other: LinkedList) -> bool:
        """Return whether this list and the other list are equal.

        >>> lst1 = LinkedList()
        >>> lst1.append(1)
        >>> lst1.append(2)
        >>> lst1.append(3)
        >>> lst2 = LinkedList()
        >>> lst1.__eq__(lst2)
        False
        >>> lst2.append(1)
        >>> lst2.append(2)
        >>> lst2.append(3)
        >>> lst1.__eq__(lst2)
        True
        """
        curr1 = self._first
        curr2 = other._first

        while not (curr1 is None or curr2 is None):
            if curr1.item == curr2.item:
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                return False
        return curr1 is curr2


    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.
        Raise IndexError if <index> is >= the length of this list.
        >>> lst1 = LinkedList()
        >>> lst1.append(1)
        >>> lst1.append(2)
        >>> lst1.append(3)
        >>> lst1[0]
        1
        >>> lst1[1]
        2
        >>> lst1[2]
        3
        >>> lst1[3]
        Traceback (most recent call last):
        IndexError
        """
        # i = 0
        # curr = self._first
        # while curr is not None:
        #     if i == index:
        #         return curr.item
        #     i += 1
        #     curr = curr.next
        # raise IndexError

        # i = index
        # curr = self._first
        # while curr is not None and i != 0:
        #     i -= 1
        #     curr = curr.next
        # if i == 0:
        #     if curr is not None:
        #         return curr.item
        # raise IndexError

        i = index
        curr = self._first
        while curr is not None and i != 0:
            i -= 1
            curr = curr.next
        if curr is None:
            if i >= 0:
                raise IndexError
        return curr.item

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.
        """
        n = _Node(item)
        if len(self) == index:
            self.append(n)
        elif index == 0:
            n.next = self._first
            self._first.next = n
        else:
            curr = self._first
            i = index
            while curr is not None and i != 0:
                i -= 1
                curr = curr.next
            if i == 0:
                n = curr.next
                curr.next = n
                curr.next.next = n
            else:
                raise IndexError

    def pop(self, index: int) -> Any:
        """Remove and return the item at position <index>.

        Raise IndexError if index >= len(self) or index < 0.

        >>> lst = LinkedList()
        >>> lst.append(1)
        >>> lst.append(2)
        >>> lst.append(10)
        >>> lst.append(200)
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(0)
        1
        >>> lst.pop()
        10
        """
        if index > len(self):
            raise IndexError
        else:
            curr = self._first
            i = index - 1
            while curr is not None and i != 0:
                curr = curr.next
                i -= 1
            if i == 0 and curr is not None:
                r = curr.next
                curr.next = r.next
                return r.item
            else:
                raise IndexError

    def remove(self, item: Any) -> None:
        """Remove the FIRST occurrence of <item> in this list.

        Do nothing if this list does not contain <item>.
        (Note: Python lists actually raise a ValueError.)

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(3)
        >>> str(lst)
        '[1]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        """
        pass

    def __str__(self):
        a = ' -> '.join(str(self[i]) for i in range(len(self)))
        return '[' + a + ']'


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()

    import doctest
    doctest.testmod()
