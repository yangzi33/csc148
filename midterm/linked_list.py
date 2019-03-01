"""Linked List

=== CSC148 Winter 2019 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list that we worked on and with
in class.  I've added some further commentary.

This implementation of LinkedList has a fancier initializer
and a __str__ method.

Code template we can use:

    curr = self._first
    while curr is not None:
        # ... curr.item ...
        curr = curr.next

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

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == []:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList([1, 2, 3])
        >>> len(lst)
        3
        """
        curr = self._first
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next
        return size

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

        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst2 = LinkedList([])
        >>> lst1.__eq__(lst2)
        False
        >>> lst2.append(1)
        >>> lst2.append(2)
        >>> lst2.append(3)
        >>> lst1.__eq__(lst2)
        True
        """
        # We need to keep track of our current position in *each* list, hence
        # these two variables.
        curr1 = self._first
        curr2 = other._first

        # Go through both linked lists, checking for equivalence along the way.
        # Stop if:
        #       either one is None.
        # In other words if:
        #       (curr1 is None) or (curr2 is None)
        # Negate this to get the condition under which to continue:
        #       not[ (curr1 is None) or (curr2 is None) ]
        # In other words, continue if
        #       [ (curr1 is not None) and (curr2 is not None) ]
        while (curr1 is not None) and (curr2 is not None):
            if curr1.item != curr2.item:
                return False
            else:
                curr1 = curr1.next
                curr2 = curr2.next

        # The only way the loop can stop and land us at this line is if
        # the following is true.
        assert (curr1 is None) or (curr2 is None)  # or both!!

        if (curr1 is None) and (curr2 is None):
            # The two lists must have the same length.
            # Plus, we never encountered two nodes with items that were not
            # equivalent.
            # This means that the two lists are equivalent!
            return True
        else:
            # One is none but not the other.
            # Therefore, one linked list is shorter than other.
            # Therefore, they are not equivalent.
            return False

        # Instead of the if-statement, we could have written:
        #       return (curr1 is None) and (curr2 is None)

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        >>> linky = LinkedList([100, 4, -50, 13])
        >>> linky[0]          # Equivalent to linky.__getitem__(0)
        100
        >>> linky[2]
        -50
        >>> linky[100]
        Traceback (most recent call last):
        IndexError
        """
        curr = self._first
        curr_index = 0

        # Iterate to (index)-th node.
        # Note: the two STOPPING conditions are
        # (1) curr is None (gone past the end of the list)
        # (2) curr_index == index (reached the correct node)
        # The loops stops when (1) or (2) is true,
        # so it *continues* when both are false.
        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        assert curr is None or curr_index == index

        if curr is None:
            raise IndexError
        else:
            return curr.item

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        >>> lst.insert(100, 2)
        Traceback (most recent call last):
        IndexError
        """
        # Create new node containing the item
        new_node = _Node(item)

        if index == 0:
            self._first, new_node.next = new_node, self._first
            # This double assignment is equivalent to:
            #   temp = self._first      # Hang on to this for use in line 3
            #   self._first = new_node
            #   new_node.next = temp
        else:
            # Iterate to (index-1)-th node.  We have to stop there because it
            # is the node whose next has to change.
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1

            assert curr is None or curr_index == index - 1

            if curr is None:
                raise IndexError
            else:
                # Update links to insert new node.
                # Again, we use the double-assignment trick to avoid a temp.
                curr.next, new_node.next = new_node, curr.next

    # def pop(self, index: int) -> Any:
    #     """Remove and return the item at position <index>.
    #
    #     Raise IndexError if index >= len(self) or index < 0.
    #
    #     >>> lst = LinkedList([1, 2, 10, 200])
    #     >>> lst.pop(1)
    #     2
    #     >>> lst.pop(2)
    #     200
    #     >>> lst.pop(148)
    #     Traceback (most recent call last):
    #     IndexError
    #     >>> lst.pop(0)
    #     1
    #     """
    #     pass

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
        # initialization.
        curr = self._first
        prev = None

        # Stop if:
        #       curr.item == item or curr is None
        # Negate that to get the condition under which to continue:
        #       not(curr.item == item or curr is None)
        # In other words, continue if:
        #       (curr.item != item) and (curr is not None)
        while (curr is not None) and (curr.item != item):
            # Our first version advanced prev based on its own current value:
            #       prev = prev.next
            # But that would crash on the first iteration, when prev is None.
            prev = curr
            curr = curr.next

        assert curr is None or curr.item == item

        if curr is None:
            # We looked in every node and never found item, so
            # ittem was not in the linked list.  There is nothing to do!
            pass
        else:
            # Since the assert was true and the if-condition was false,
            # curr.item must be item -- we found it!  Unlink the node that
            # curr references.
            if prev is None:
                # We must have found item in the very first node.  curr
                # references that node, and prev is still None.
                # We left the RHS of this expression for you to figure out.
                # Here is the solution:
                self._first = self._first.next
            else:
                prev.next = curr.next
