import os
from abc import abstractmethod


class Clothes:


    @abstractmethod
    def myName(cls):
        pass


class Coat(Clothes):

    def __init__(self, s):
        self.size_c = s

    @property
    def size(self):
        return self.size_c/6.5 + 0.5

    @classmethod
    def myName(cls):
        return cls.__name__


class Costume(Clothes):

    def __init__(self, h):
        self.height = h

    @property
    def size(self):
        return 2*self.height + 0.3

    @classmethod
    def myName(cls):
        return cls.__name__


my_coat = Coat(40)
print(my_coat.size)
print(my_coat.myName())

my_costume = Costume(176)
print(my_costume.size)
print(my_costume.myName())


