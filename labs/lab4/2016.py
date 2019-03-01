from typing import Callable
from myqueue import *

class DoubleQueue(Queue):

    def __init__(self, is_special: Callable[[Any], bool]):
        Queue.__init__(self)
        self._a = is_special

    def enqueue(self, item):
        if self._a(item):
            self.enqueue(item)
        self.enqueue(item)

if __name__ == '__main__':
    def f(a):
        return a in ['a','b','c']
    a = DoubleQueue(f)
    a.enqueue('a')
    a.enqueue(1)
    a.enqueue(2)
    print(a)
