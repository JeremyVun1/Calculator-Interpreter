from .BaseToken import BaseToken

class SubtractToken(BaseToken):
    def __init__(self):
        super().__init__("-")
