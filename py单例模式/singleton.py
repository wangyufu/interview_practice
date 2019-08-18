#!/usr/bin/env python

class SingleTon(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        # if not cls._instance:
        cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Test1(SingleTon):
    def __init__(self, n):
        self.n = n

t1 = Test1(2)

t2 = Test1(3)
print(t1.n)
print(t2.n)


