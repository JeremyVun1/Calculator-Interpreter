from .BaseRule import BaseRule
from tokens import NumberToken

class NumberRule(BaseRule):

    # validate that token is still a number
    def validate(self, new_state):
        return new_state.isnumeric()

    def get_token(self):
        return NumberToken(self.state)
