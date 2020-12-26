import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

import pytest
from rules import *
from lexer import Lexer

@pytest.fixture
def lexer():
    rules = [
        NumberRule(),
        OperatorRule(),
        BreakRule([" "])
    ]
    rulebook = Rulebook(rules)
    return Lexer(rulebook)

def test_lexer_valid(lexer):
    tests = {
        "100 + 100": 3,
        "100 100 100": 3,
        "100-----": 6,
        "- +  *": 3,
        "0 0 00 + * 0": 6 
    }
    for test_line in tests:
        expected_num_tokens = tests[test_line]
        tokens = lexer.lex(test_line)
        assert len(tokens) == expected_num_tokens
        lexer.reset()


def test_lexer_invalid(lexer):
    tests = [
        "a",
        "100 + 100 a",
        "=",
        "a * a",
        None
    ]
    for test_line in tests:
        with pytest.raises(Exception):
            lexer.lex(test_line)
            lexer.reset()