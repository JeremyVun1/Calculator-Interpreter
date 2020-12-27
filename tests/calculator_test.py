import pytest
from .fixtures import lexer, calculator

def test_calculator_valid(lexer, calculator):
    tests = {
        "100 + 100": 200,
        "5+5 * 5": 30,
        "2^2*2": 8,
        "2^(2*2)": 16,
        "1+(2+3)*4": 21,
        "1    +    1": 2
    }
    for test_line in tests:
        expected_answer = tests[test_line]

        tokens = lexer.lex(test_line)
        actual_answer = calculator.evaluate(tokens)
        assert actual_answer == expected_answer


def test_calculator_invalid(lexer):
    tests = [
        "100++100",
        "+",
        "**",
        None,
        "*100+100",
        "",
        ")"
        "100+100)"
    ]
    for test_line in tests:
        with pytest.raises(Exception):
            tokens = lexer.lex(test_line)
            calculator.evaluate(tokens)