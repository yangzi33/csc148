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
        cur1 = self._first
        cur2 = other._first

        # stop when: cur1 is None or cur2 is None
        while (cur1 is not None) and (cur2 is not None):
            if cur1.item != cur2.item:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        # if we leave the loop and end up here
        assert cur1 is None or cur2 is None

        #if cur1 is None and cur2 is None:
        #    # the lists are the same
        #    return True
        #else:
        #    # either self is longer than other, or other is longer than self
        #    return False
        return cur1 is None and cur2 is None


    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.
        """
        cur = self._first
        i = 0
        while (cur is not None) and (i < index):
            cur = cur.next
            i += 1

        assert cur is None or i == index

        if cur is None:
            raise IndexError
        else:
            return cur.item # dangerous if we don't know that cur is not None

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.
        """
        new_node = _Node(item)
        # the case where we need to update self._first
        # because are inserting at the beginning of the list
        if index == 0:
            # first we set the next, so we have two references to
            # the node that is the original self._first
            # order of these two lines matters
            # exercise: draw both ways, convince yourself the order matters
            new_node.next = self._first
            self._first = new_node
        else:
            cur = self._first
            i = 0
            # stop before the index we want to insert at
            while (cur is not None) and (i != index - 1):
                cur = cur.next
                i += 1
            assert cur is None or (i == index - 1)
            if cur is None:
                # if we get here, then we are trying to insert at an
                # out of bounds index
                raise IndexError
            else:
                # again, the order of these matters!
                new_node.next = cur.next
                cur.next = new_node


    def pop(self, index: int) -> Any:
        """Remove and return the item at position <index>.

        Raise IndexError if index >= len(self) or index < 0.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(148)
        Traceback (most recent call last):
        IndexError
        >>> lst.pop(0)
        1
        """
        pass

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


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    import doctest
    doctest.testmod()
