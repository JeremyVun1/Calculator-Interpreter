from tokens.OperatorToken import OperatorToken
from .OperatorToken import OperatorToken

class BracketToken(OperatorToken):
    pass

class OpenBracketToken(BracketToken):
    def __init__(self):
        super().__init__("(")

class CloseBracketToken(BracketToken):
    def __init__(self):
        super().__init__(")")
