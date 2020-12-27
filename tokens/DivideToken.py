from .OperatorToken import OperatorToken
from .NumberToken import NumberToken

class DivideToken(OperatorToken):
    def __init__(self):
        super().__init__("/")

    def evaluate(self, x, y):
        return NumberToken(x.value / y.value)
