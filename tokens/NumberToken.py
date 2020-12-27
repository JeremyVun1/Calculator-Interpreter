from .BaseToken import BaseToken

class NumberToken(BaseToken):
    def __init__(self, value):
        super().__init__(float(value))
