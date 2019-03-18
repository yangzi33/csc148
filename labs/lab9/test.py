import unittest
from bst import *

root = BinarySearchTree(10)

class ClosestTest(unittest.TestCase):
    def setUp(self):
        l1 = BinarySearchTree(5)
        l2 = BinarySearchTree(9)
        l3 = BinarySearchTree(15)
        l4 = BinarySearchTree(21)
        in1 = BinarySearchTree(7)
        in2 = BinarySearchTree(17)
        root._right = in2
        root._left = in1
        in1._left = l1
        in1._right = l2
        in2._left = l3
        in2._right = l4

    def test1(self):
        expected = 21
        actual = root.closest(20)
        self.assertEqual(expected, actual)

    def test2(self):
        expected =

unittest.main(exit=False)
