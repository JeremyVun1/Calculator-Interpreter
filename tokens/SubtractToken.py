from .OperatorToken import OperatorToken
from .NumberToken import NumberToken

class SubtractToken(OperatorToken):
    def __init__(self):
        super().__init__("-")

    def evaluate(self, x, y):
        return NumberToken(x.value - y.value)
