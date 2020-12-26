from .BaseToken import BaseToken

class DivideToken(BaseToken):
    def __init__(self):
        super().__init__("/")
