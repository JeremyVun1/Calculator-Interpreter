from .BaseRule import BaseRule
from tokens import BreakToken

class BreakRule(BaseRule):
    def __init__(self, break_symbols):
        super().__init__()

        self.break_sybols = break_symbols
        self.state = None

    def validate(self, new_state):
        if new_state in self.break_sybols:
            self.state = new_state
            return True
        return False

    def get_token(self):
        return BreakToken(self.state)
