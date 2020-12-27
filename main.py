from evaluators.visitors.CalculatorVisitor import CalculatorVisitor
from evaluators.Evaluator import Evaluator
from lexer import Lexer
from rules import *
from evaluators import *

from tokens import *

def main():
    query_string = input(": ")

    rules = [
        NumberRule(),
        OperatorRule(),
        BreakRule([" "])
    ]
    rulebook = Rulebook(rules)

    lexer = Lexer(rulebook)

    calculator = Evaluator(CalculatorVisitor())

    try:
        tokens = lexer.lex(query_string)
        result = calculator.evaluate(tokens)
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()