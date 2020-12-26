import BaseRule

class NumberRule(BaseRule):

    # validate that token is still a number
    def validate(self, new_state):
        if new_state.is_numeric():
            self.state = new_state
        else self.is_alive = False
