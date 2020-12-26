class Lexer:

    def __init__(self, rulebook):
        self.rulebook = rulebook
        self.rulebook.reset()
        self.tokens = []

    def get_token(self, rulebook):
        rule = self.rulebook.last_valid_rule
        if rule:
            return rule.get_token()
        else:
            return None

    def add_token(self, rulebook):
        token = self.get_token(self.rulebook)
        self.rulebook.reset()
        if token:
            self.tokens.append(token)
            return True
        else:
            return False

    def parse(self, line):
        i = 0

        while i < len(line):
            c = line[i]
            self.rulebook.parse(c)

            # get longest living token
            if self.rulebook.is_exhausted():
                if self.add_token(self.rulebook):
                    i -= 1
                else:
                    raise Exception(f"cannot parse '{c}' at pos {i}")

            i += 1
                

        # get any remaining token
        if not self.rulebook.is_exhausted():
            self.add_token(self.rulebook)

        return self.tokens

    def lex(self, line):
        tokens = self.parse(line)
        return tokens
        
        # create AST from tokens
        # do not apply RPN or anything here. RPN is the responsibility of the evaluator module

    def reset(self):
        self.tokens = []
