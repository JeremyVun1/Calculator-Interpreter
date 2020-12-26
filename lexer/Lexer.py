from tokens import BreakToken

class Lexer:
    def __init__(self, rulebook):
        self.rulebook = rulebook
        self.rulebook.reset()
        self.tokens = []


    def lex(self, line):
        i = 0

        # SCAN
        while i < len(line):
            c = line[i]
            self.rulebook.parse(c)

            # get longest living token
            if self.rulebook.is_exhausted():
                # rewind index one step if the rule exhaustion resulted in a token being created
                if self.add_token(self.rulebook):
                    i -= 1
                else:
                    raise Exception(f"cannot parse '{c}' at pos {i}")
            i += 1

        # get any remaining token
        if not self.rulebook.is_exhausted():
            self.add_token(self.rulebook)

        # remove break tokens
        for i in reversed(range(0, len(self.tokens))):
            if type(self.tokens[i]) == BreakToken:
                self.tokens.pop(i)

        return self.tokens


    def get_token(self, rulebook):
        rule = self.rulebook.last_valid_rule

        if rule:
            return rule.get_token()
        return None


    def add_token(self, rulebook):
        token = self.get_token(self.rulebook)
        self.rulebook.reset()

        if token:
            self.tokens.append(token)
            return True
        return False


    def reset(self):
        self.tokens = []
