from .BaseVisitor import BaseVisitor
from tokens import *


class CalculatorVisitor(BaseVisitor):

    def __init__(self):
        self.last_token_is_num = False
        self.stack = []
        self.rpn_ast = []

        self.precedence = {
            OpenBracketToken: 0,
            CloseBracketToken: 0,
            AddToken: 1,
            SubtractToken: 1,
            MultiplyToken: 2,
            DivideToken: 2,
            PowerToken: 3
        }

        self.pos = 0

    def valid_token(self, token):
        if self.last_token_is_num:
            return isinstance(token, OperatorToken)
        else:
            return isinstance(token, NumberToken) or isinstance(token, BracketToken)

    # construct the AST in RPN notation
    def visit(self, token):
        self.pos += 1
        # Ensure tokens are alternating between NumberToken and Operator Token
        if not self.valid_token(token):
            raise Exception(f"Invalid syntax. Unexpected symbol '{token.value}' at pos {self.pos}")

        #####
        # Number token goes to AST
        #####
        if isinstance(token, NumberToken):
            self.rpn_ast.append(token)
            self.last_token_is_num = True

        elif isinstance(token, OperatorToken):
            #####
            # Just put open brackets on the stack
            #####
            if isinstance(token, OpenBracketToken):
                self.stack.append(token)
            
            elif len(self.stack):
                top = self.stack[-1]
                
                #####
                # Close bracket, flush stack till open bracket
                #####
                if isinstance(token, CloseBracketToken):
                    while len(self.stack) and not isinstance(top, OpenBracketToken):
                        self.rpn_ast.append(self.stack.pop())
                        top = self.stack[-1]
                    if isinstance(top, OpenBracketToken):
                        self.stack.pop()
                    else:
                        raise Exception("Invalid syntax, matching '(' could not be found")
                
                #####
                # clear the stack to the AST if token is lower precedence
                #####
                else:
                    while len(self.stack) and self.precedence[type(token)] < self.precedence[type(top)]:
                        self.rpn_ast.append(self.stack.pop())
                        if len(self.stack):
                            top = self.stack[-1]

                    self.stack.append(token)
                    self.last_token_is_num = False
            else:
                self.last_token_is_num = False
                self.stack.append(token)

    
    def evaluate(self):
        while (len(self.stack)):
            self.rpn_ast.append(self.stack.pop())

        eval_stack = []
        if len(self.rpn_ast):
            for token in self.rpn_ast:
                if isinstance(token, NumberToken):
                    eval_stack.append(token)
                elif isinstance(token, OperatorToken):
                    b_val = eval_stack.pop()
                    a_val = eval_stack.pop()
                    eval_stack.append(token.evaluate(a_val, b_val))
            
            return eval_stack.pop().value
        else:
            return 0