
class Lexer:

    def __init__(self, rulebook):
        self.rulebook = rulebook
        self.rulebook.reset()

    def get_token(self, rulebook):
        rule = self.rulebook.last_valid_rule()
            if rule:
                return token = rule.create_token()
            else raise Exception("cannot parse line")

    def add_token(self, rulebook):
        token = self.get_token(self.rulebook)
            if token:
                tokens.push(token)
                self.rulebook.reset()

    def parse(line):
        tokens = []

        for c in line:
            self.rulebook.parse(c)

            # get longest living token
            if self.rulebook.is_exhausted():
                self.add_token(self.rulebook)

        # get any remaining token
        if not self.rulebook.is_exhausted():
            self.add_token(self.rulebook)

        return tokens

    def lex(tokens):
        # create AST
        pass
