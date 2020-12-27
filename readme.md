# Calculator Interpreter
Tokenize arithmetic strings into AST using extensible rulesets and evaluate using a custom visitor
```
python main.py
: 1+1
: 2
```

## Lexer
parse text string into an AST according to custom syntax rules. Longest standing rule match applies, conflicts resolve to the rule that is added last in the rule list
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
Inject custom visitor to walk through AST and evaluate it
```
tokens = lexer.lex("100 + 100")
calculator = Evaluator(CalculatorVisitor())

result = calculator.evaluate(tokens)
```
