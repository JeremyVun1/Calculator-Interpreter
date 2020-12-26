# Lexer
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

# Evaluator
AST syntax validated and evaluated using custom rules via visitor pattern.
```
tokens = lexer.lex("100 + 100")

result = CalculatorEvaluator(tokens)
```

# UI
Console wrapper
