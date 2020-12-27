from .BaseToken import BaseToken
from abc import abstractmethod

class OperatorToken(BaseToken):
    def __init__(self, value):
        super().__init__(value)

    @abstractmethod
    def evaluate(self, x, y):
        pass