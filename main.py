from lexer import Lexer
from rules import *

def main():
    rules = [
        NumberRule(),
        OperatorRule(),
        BreakRule([" "])
    ]
    rulebook = Rulebook(rules)
    lexer = Lexer(rulebook)

    try:
        tokens = lexer.lex("100-----")
        print(tokens)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()