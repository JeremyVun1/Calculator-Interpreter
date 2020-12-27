from typing import AbstractSet
from tokens import *
from abc import abstractmethod

class BaseVisitor:

    def __init__(self):
        pass

    @abstractmethod
    def visit(self, token):
        print(token.value)

    @abstractmethod
    def reset(self):
        raise NotImplementedError("Visitor Reset not implemented")
