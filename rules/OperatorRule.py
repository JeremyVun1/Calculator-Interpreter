import BaseRule

class OperatorRule(BaseRule):

    valid_symbols = ["+", "-", "/", "*"]

    # validate that token is still a number
    def validate(self, new_state):
        if self.valid_symbols.contains(new_state):
            self.state = new_state
        else self.is_alive = False
