from lexer import Lexer
from rules.Rulebook import Rulebook
from rules import NumberRule, OperatorRule

def main():
    rules = [NumberRule.NumberRule(), OperatorRule.OperatorRule()]
    rulebook = Rulebook(rules)
    lexer = Lexer(rulebook)

    try:
        tokens = lexer.lex("100+100")
        print(tokens)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()