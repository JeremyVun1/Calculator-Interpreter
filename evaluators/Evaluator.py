class Evaluator():
    def __init__(self, visitor):
        self.visitor = visitor

    def evaluate(self, tokens):
        for token in tokens:
            token.accept(self.visitor)

        return self.visitor.evaluate()
