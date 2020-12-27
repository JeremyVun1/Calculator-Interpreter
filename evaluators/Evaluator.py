class Evaluator():
    def __init__(self, visitor):
        self.visitor = visitor

    def evaluate(self, tokens):
        query_string = ""
        for token in tokens:
            query_string += f"{token.value}"
            token.accept(self.visitor)

        return f"{query_string} = {self.visitor.evaluate()}"
