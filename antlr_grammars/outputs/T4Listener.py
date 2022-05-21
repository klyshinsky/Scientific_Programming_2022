# Generated from T4.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .T4Parser import T4Parser
else:
    from T4Parser import T4Parser

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


# This class defines a complete listener for a parse tree produced by T4Parser.
class T4Listener(ParseTreeListener):

    # Enter a parse tree produced by T4Parser#start.
    def enterStart(self, ctx:T4Parser.StartContext):
        pass

    # Exit a parse tree produced by T4Parser#start.
    def exitStart(self, ctx:T4Parser.StartContext):
        pass


    # Enter a parse tree produced by T4Parser#decl.
    def enterDecl(self, ctx:T4Parser.DeclContext):
        pass

    # Exit a parse tree produced by T4Parser#decl.
    def exitDecl(self, ctx:T4Parser.DeclContext):
        pass


    # Enter a parse tree produced by T4Parser#Return.
    def enterReturn(self, ctx:T4Parser.ReturnContext):
        pass

    # Exit a parse tree produced by T4Parser#Return.
    def exitReturn(self, ctx:T4Parser.ReturnContext):
        pass


    # Enter a parse tree produced by T4Parser#Break.
    def enterBreak(self, ctx:T4Parser.BreakContext):
        pass

    # Exit a parse tree produced by T4Parser#Break.
    def exitBreak(self, ctx:T4Parser.BreakContext):
        pass


    # Enter a parse tree produced by T4Parser#Add.
    def enterAdd(self, ctx:T4Parser.AddContext):
        pass

    # Exit a parse tree produced by T4Parser#Add.
    def exitAdd(self, ctx:T4Parser.AddContext):
        pass


    # Enter a parse tree produced by T4Parser#Braced.
    def enterBraced(self, ctx:T4Parser.BracedContext):
        pass

    # Exit a parse tree produced by T4Parser#Braced.
    def exitBraced(self, ctx:T4Parser.BracedContext):
        pass


    # Enter a parse tree produced by T4Parser#Mult.
    def enterMult(self, ctx:T4Parser.MultContext):
        pass

    # Exit a parse tree produced by T4Parser#Mult.
    def exitMult(self, ctx:T4Parser.MultContext):
        pass


    # Enter a parse tree produced by T4Parser#Pow.
    def enterPow(self, ctx:T4Parser.PowContext):
        pass

    # Exit a parse tree produced by T4Parser#Pow.
    def exitPow(self, ctx:T4Parser.PowContext):
        pass


    # Enter a parse tree produced by T4Parser#Id.
    def enterId(self, ctx:T4Parser.IdContext):
        pass

    # Exit a parse tree produced by T4Parser#Id.
    def exitId(self, ctx:T4Parser.IdContext):
        pass


    # Enter a parse tree produced by T4Parser#Int.
    def enterInt(self, ctx:T4Parser.IntContext):
        pass

    # Exit a parse tree produced by T4Parser#Int.
    def exitInt(self, ctx:T4Parser.IntContext):
        pass



del T4Parser