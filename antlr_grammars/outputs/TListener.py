# Generated from T.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TParser import TParser
else:
    from TParser import TParser

# This class defines a complete listener for a parse tree produced by TParser.
class TListener(ParseTreeListener):

    # Enter a parse tree produced by TParser#Return.
    def enterReturn(self, ctx:TParser.ReturnContext):
        pass

    # Exit a parse tree produced by TParser#Return.
    def exitReturn(self, ctx:TParser.ReturnContext):
        pass


    # Enter a parse tree produced by TParser#Break.
    def enterBreak(self, ctx:TParser.BreakContext):
        pass

    # Exit a parse tree produced by TParser#Break.
    def exitBreak(self, ctx:TParser.BreakContext):
        pass


    # Enter a parse tree produced by TParser#Add.
    def enterAdd(self, ctx:TParser.AddContext):
        pass

    # Exit a parse tree produced by TParser#Add.
    def exitAdd(self, ctx:TParser.AddContext):
        pass


    # Enter a parse tree produced by TParser#Mult.
    def enterMult(self, ctx:TParser.MultContext):
        pass

    # Exit a parse tree produced by TParser#Mult.
    def exitMult(self, ctx:TParser.MultContext):
        pass


    # Enter a parse tree produced by TParser#Id.
    def enterId(self, ctx:TParser.IdContext):
        pass

    # Exit a parse tree produced by TParser#Id.
    def exitId(self, ctx:TParser.IdContext):
        pass


    # Enter a parse tree produced by TParser#Int.
    def enterInt(self, ctx:TParser.IntContext):
        pass

    # Exit a parse tree produced by TParser#Int.
    def exitInt(self, ctx:TParser.IntContext):
        pass



del TParser