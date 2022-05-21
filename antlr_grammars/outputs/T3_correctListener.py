# Generated from T3_correct.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .T3_correctParser import T3_correctParser
else:
    from T3_correctParser import T3_correctParser

import math

def make_op(stack, op):
    if op == '*': 
        stack[-2] *= stack[-1] 
    elif op == '/':
        stack[-2] /= stack[-1]
    elif op == '+':
        stack[-2] += stack[-1]
    elif op == '-':
        stack[-2] -= stack[-1]

    stack.pop()
    print(op)


# This class defines a complete listener for a parse tree produced by T3_correctParser.
class T3_correctListener(ParseTreeListener):

    # Enter a parse tree produced by T3_correctParser#Return.
    def enterReturn(self, ctx:T3_correctParser.ReturnContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Return.
    def exitReturn(self, ctx:T3_correctParser.ReturnContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Break.
    def enterBreak(self, ctx:T3_correctParser.BreakContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Break.
    def exitBreak(self, ctx:T3_correctParser.BreakContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Add.
    def enterAdd(self, ctx:T3_correctParser.AddContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Add.
    def exitAdd(self, ctx:T3_correctParser.AddContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Braced.
    def enterBraced(self, ctx:T3_correctParser.BracedContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Braced.
    def exitBraced(self, ctx:T3_correctParser.BracedContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Mult.
    def enterMult(self, ctx:T3_correctParser.MultContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Mult.
    def exitMult(self, ctx:T3_correctParser.MultContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Pow.
    def enterPow(self, ctx:T3_correctParser.PowContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Pow.
    def exitPow(self, ctx:T3_correctParser.PowContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Id.
    def enterId(self, ctx:T3_correctParser.IdContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Id.
    def exitId(self, ctx:T3_correctParser.IdContext):
        pass


    # Enter a parse tree produced by T3_correctParser#Int.
    def enterInt(self, ctx:T3_correctParser.IntContext):
        pass

    # Exit a parse tree produced by T3_correctParser#Int.
    def exitInt(self, ctx:T3_correctParser.IntContext):
        pass



del T3_correctParser