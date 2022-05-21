# Generated from T3_incorrect.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import math

def serializedATN():
    return [
        4,1,14,57,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,12,8,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,30,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,55,9,1,1,1,0,1,2,
        2,0,2,0,0,62,0,11,1,0,0,0,2,29,1,0,0,0,4,5,5,1,0,0,5,6,3,2,1,0,6,
        7,5,2,0,0,7,8,6,0,-1,0,8,12,1,0,0,0,9,10,5,3,0,0,10,12,5,2,0,0,11,
        4,1,0,0,0,11,9,1,0,0,0,12,1,1,0,0,0,13,14,6,1,-1,0,14,15,5,8,0,0,
        15,16,5,12,0,0,16,17,6,1,-1,0,17,18,5,9,0,0,18,19,5,12,0,0,19,20,
        6,1,-1,0,20,21,5,10,0,0,21,30,6,1,-1,0,22,23,5,12,0,0,23,30,6,1,
        -1,0,24,30,5,13,0,0,25,26,5,11,0,0,26,27,3,2,1,0,27,28,5,10,0,0,
        28,30,1,0,0,0,29,13,1,0,0,0,29,22,1,0,0,0,29,24,1,0,0,0,29,25,1,
        0,0,0,30,53,1,0,0,0,31,32,10,8,0,0,32,33,5,4,0,0,33,34,3,2,1,9,34,
        35,6,1,-1,0,35,52,1,0,0,0,36,37,10,7,0,0,37,38,5,5,0,0,38,39,3,2,
        1,8,39,40,6,1,-1,0,40,52,1,0,0,0,41,42,10,6,0,0,42,43,5,6,0,0,43,
        44,3,2,1,7,44,45,6,1,-1,0,45,52,1,0,0,0,46,47,10,5,0,0,47,48,5,7,
        0,0,48,49,3,2,1,6,49,50,6,1,-1,0,50,52,1,0,0,0,51,31,1,0,0,0,51,
        36,1,0,0,0,51,41,1,0,0,0,51,46,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,
        0,53,54,1,0,0,0,54,3,1,0,0,0,55,53,1,0,0,0,4,11,29,51,53
    ]

class T3_incorrectParser ( Parser ):

    grammarFileName = "T3_incorrect.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return '", "';'", "'break'", "'*'", 
                     "'/'", "'+'", "'-'", "'pow('", "','", "')'", "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "ID", "WS" ]

    RULE_stat = 0
    RULE_e = 1

    ruleNames =  [ "stat", "e" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    INT=12
    ID=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    res = ""



    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.stack = []


        def getRuleIndex(self):
            return T3_incorrectParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.stack = ctx.stack



    class ReturnContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(T3_incorrectParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)


    class BreakContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)



    def stat(self):

        localctx = T3_incorrectParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        try:
            self.state = 11
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [T3_incorrectParser.T__0]:
                localctx = T3_incorrectParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(T3_incorrectParser.T__0)
                self.state = 5
                self.e(0)
                self.state = 6
                self.match(T3_incorrectParser.T__1)
                print("calculated:", localctx.stack)
                pass
            elif token in [T3_incorrectParser.T__2]:
                localctx = T3_incorrectParser.BreakContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(T3_incorrectParser.T__2)
                self.state = 10
                self.match(T3_incorrectParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return T3_incorrectParser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T3_incorrectParser.EContext)
            else:
                return self.getTypedRuleContext(T3_incorrectParser.EContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)


    class AddContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T3_incorrectParser.EContext)
            else:
                return self.getTypedRuleContext(T3_incorrectParser.EContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class SubContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T3_incorrectParser.EContext)
            else:
                return self.getTypedRuleContext(T3_incorrectParser.EContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)


    class BracedContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(T3_incorrectParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBraced" ):
                listener.enterBraced(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBraced" ):
                listener.exitBraced(self)


    class MultContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T3_incorrectParser.EContext)
            else:
                return self.getTypedRuleContext(T3_incorrectParser.EContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)


    class PowContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self._INT = None # Token
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(T3_incorrectParser.INT)
            else:
                return self.getToken(T3_incorrectParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)


    class IdContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(T3_incorrectParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_incorrectParser.EContext
            super().__init__(parser)
            self._INT = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(T3_incorrectParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = T3_incorrectParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [T3_incorrectParser.T__7]:
                localctx = T3_incorrectParser.PowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.match(T3_incorrectParser.T__7)
                self.state = 15
                localctx._INT = self.match(T3_incorrectParser.INT)
                a=int((None if localctx._INT is None else localctx._INT.text))
                self.state = 17
                self.match(T3_incorrectParser.T__8)
                self.state = 18
                localctx._INT = self.match(T3_incorrectParser.INT)
                b=int((None if localctx._INT is None else localctx._INT.text))
                self.state = 20
                self.match(T3_incorrectParser.T__9)

                self.getInvokingContext(0).stack.append(math.pow(a,b)); print("pow"); 
                      
                pass
            elif token in [T3_incorrectParser.INT]:
                localctx = T3_incorrectParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                localctx._INT = self.match(T3_incorrectParser.INT)

                self.res+=self._input.getText(localctx.start, self._input.LT(-1)); 
                self.getInvokingContext(0).stack.append(int(self._input.getText(localctx.start, self._input.LT(-1)))); 
                print("->", self.getInvokingContext(0).stack)
                      
                pass
            elif token in [T3_incorrectParser.ID]:
                localctx = T3_incorrectParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(T3_incorrectParser.ID)
                pass
            elif token in [T3_incorrectParser.T__10]:
                localctx = T3_incorrectParser.BracedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(T3_incorrectParser.T__10)
                self.state = 26
                self.e(0)
                self.state = 27
                self.match(T3_incorrectParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = T3_incorrectParser.MultContext(self, T3_incorrectParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 31
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 32
                        self.match(T3_incorrectParser.T__3)
                        self.state = 33
                        self.e(9)
                        self.getInvokingContext(0).stack[-2]*=self.getInvokingContext(0).stack[-1]; self.getInvokingContext(0).stack.pop(); print("*"); 
                                        
                        pass

                    elif la_ == 2:
                        localctx = T3_incorrectParser.DivContext(self, T3_incorrectParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 36
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 37
                        self.match(T3_incorrectParser.T__4)
                        self.state = 38
                        self.e(8)
                        self.getInvokingContext(0).stack[-2]/=self.getInvokingContext(0).stack[-1]; self.getInvokingContext(0).stack.pop(); print("/"); 
                                        
                        pass

                    elif la_ == 3:
                        localctx = T3_incorrectParser.AddContext(self, T3_incorrectParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 41
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 42
                        self.match(T3_incorrectParser.T__5)
                        self.state = 43
                        self.e(7)
                        self.getInvokingContext(0).stack[-2]+=self.getInvokingContext(0).stack[-1]; self.getInvokingContext(0).stack.pop(); print("+"); 
                                        
                        pass

                    elif la_ == 4:
                        localctx = T3_incorrectParser.SubContext(self, T3_incorrectParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 46
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 47
                        self.match(T3_incorrectParser.T__6)
                        self.state = 48
                        self.e(6)
                        self.getInvokingContext(0).stack[-2]-=self.getInvokingContext(0).stack[-1]; self.getInvokingContext(0).stack.pop(); print("-|"); 
                                        
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self._ctx.stop = self._input.LT(-1)
            print("processed", self.getInvokingContext(0).stack);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.e_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




