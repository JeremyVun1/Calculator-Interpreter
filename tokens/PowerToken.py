from .OperatorToken import OperatorToken
from .NumberToken import NumberToken

class PowerToken(OperatorToken):
    def __init__(self):
        super().__init__("^")

    def evaluate(self, x, y):
        return NumberToken(pow(x.value, y.value))
