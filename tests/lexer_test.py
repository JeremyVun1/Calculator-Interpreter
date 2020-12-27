import pytest
from .fixtures import lexer

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
