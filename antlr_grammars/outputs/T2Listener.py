# Generated from T2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .T2Parser import T2Parser
else:
    from T2Parser import T2Parser

import math


# This class defines a complete listener for a parse tree produced by T2Parser.
class T2Listener(ParseTreeListener):

    # Enter a parse tree produced by T2Parser#Return.
    def enterReturn(self, ctx:T2Parser.ReturnContext):
        pass

    # Exit a parse tree produced by T2Parser#Return.
    def exitReturn(self, ctx:T2Parser.ReturnContext):
        pass


    # Enter a parse tree produced by T2Parser#Break.
    def enterBreak(self, ctx:T2Parser.BreakContext):
        pass

    # Exit a parse tree produced by T2Parser#Break.
    def exitBreak(self, ctx:T2Parser.BreakContext):
        pass


    # Enter a parse tree produced by T2Parser#Add.
    def enterAdd(self, ctx:T2Parser.AddContext):
        pass

    # Exit a parse tree produced by T2Parser#Add.
    def exitAdd(self, ctx:T2Parser.AddContext):
        pass


    # Enter a parse tree produced by T2Parser#Mult.
    def enterMult(self, ctx:T2Parser.MultContext):
        pass

    # Exit a parse tree produced by T2Parser#Mult.
    def exitMult(self, ctx:T2Parser.MultContext):
        pass


    # Enter a parse tree produced by T2Parser#Pow.
    def enterPow(self, ctx:T2Parser.PowContext):
        pass

    # Exit a parse tree produced by T2Parser#Pow.
    def exitPow(self, ctx:T2Parser.PowContext):
        pass


    # Enter a parse tree produced by T2Parser#Id.
    def enterId(self, ctx:T2Parser.IdContext):
        pass

    # Exit a parse tree produced by T2Parser#Id.
    def exitId(self, ctx:T2Parser.IdContext):
        pass


    # Enter a parse tree produced by T2Parser#Int.
    def enterInt(self, ctx:T2Parser.IntContext):
        pass

    # Exit a parse tree produced by T2Parser#Int.
    def exitInt(self, ctx:T2Parser.IntContext):
        pass



del T2Parser