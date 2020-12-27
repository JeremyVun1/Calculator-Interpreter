import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

import pytest
from rules import *
from lexer import Lexer
from evaluator import *

@pytest.fixture
def lexer():
    rules = [
        NumberRule(),
        OperatorRule(),
        BreakRule([" "])
    ]
    rulebook = Rulebook(rules)
    return Lexer(rulebook)

@pytest.fixture
def calculator():
    return Evaluator(CalculatorVisitor())