from .BaseRule import BaseRule
from tokens import *

class OperatorRule(BaseRule):

    valid_symbols = {
        "+": AddToken,
        "-": SubtractToken,
        "/": DivideToken,
        "*": MultiplyToken,
        "(": OpenBracketToken,
        ")": CloseBracketToken,
        "^": PowerToken
    }

    # validate that token is still a number
    def validate(self, new_state):
        return new_state in self.valid_symbols

    def get_token(self):
        return self.valid_symbols[self.state]()