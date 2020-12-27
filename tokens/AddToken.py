from tokens.OperatorToken import OperatorToken
from .OperatorToken import OperatorToken
from .NumberToken import NumberToken

class AddToken(OperatorToken):
    def __init__(self):
        super().__init__("+")

    def evaluate(self, x, y):
        return NumberToken(x.value + y.value)