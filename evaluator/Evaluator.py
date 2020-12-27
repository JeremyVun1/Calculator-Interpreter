class Evaluator():
    def __init__(self, visitor):
        self.visitor = visitor

    def evaluate(self, tokens):
        for token in tokens:
            token.accept(self.visitor)

        result = self.visitor.evaluate()
        self.visitor.reset()
        return result
