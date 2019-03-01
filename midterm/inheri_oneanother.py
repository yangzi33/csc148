from typing import *

class A:
    '''
    fff
    '''
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(A):

    def __str__(self):
        return '{} + {} is 69'.format(self.a, self.b)

