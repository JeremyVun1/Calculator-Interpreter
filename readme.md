# Calculator Interpreter
Tokenize arithmetic strings into AST using extensible rulesets and evaluate using a custom visitor
```
python main.py
: 1+1
```

## Lexer
parse text string into an AST. Longest standing rule match applies, conflicts resolve to the rule that is added last
```
rules = [
    NumberRule(),
    OperatorRule(),
    BreakRule([" "])
]
rulebook = Rulebook(rules)
lexer = Lexer(rulebook)

tokens = lexer.lex("100 + 100")
```

## Evaluator
AST syntax validated and evaluated using custom rules via visitor pattern.
```
tokens = lexer.lex("100 + 100")
calculator = Evaluator(CalculatorVisitor())

result = calculator.evaluate(tokens)
```
