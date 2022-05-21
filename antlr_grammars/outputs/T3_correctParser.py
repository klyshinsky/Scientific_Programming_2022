# Generated from T3_correct.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


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

def serializedATN():
    return [
        4,1,12,47,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,12,8,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,30,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,42,8,1,10,
        1,12,1,45,9,1,1,1,0,1,2,2,0,2,0,0,50,0,11,1,0,0,0,2,29,1,0,0,0,4,
        5,5,1,0,0,5,6,3,2,1,0,6,7,5,2,0,0,7,8,6,0,-1,0,8,12,1,0,0,0,9,10,
        5,3,0,0,10,12,5,2,0,0,11,4,1,0,0,0,11,9,1,0,0,0,12,1,1,0,0,0,13,
        14,6,1,-1,0,14,15,5,4,0,0,15,16,5,8,0,0,16,17,6,1,-1,0,17,18,5,5,
        0,0,18,19,5,8,0,0,19,20,6,1,-1,0,20,21,5,6,0,0,21,30,6,1,-1,0,22,
        23,5,8,0,0,23,30,6,1,-1,0,24,30,5,9,0,0,25,26,5,7,0,0,26,27,3,2,
        1,0,27,28,5,6,0,0,28,30,1,0,0,0,29,13,1,0,0,0,29,22,1,0,0,0,29,24,
        1,0,0,0,29,25,1,0,0,0,30,43,1,0,0,0,31,32,10,6,0,0,32,33,5,12,0,
        0,33,34,3,2,1,7,34,35,6,1,-1,0,35,42,1,0,0,0,36,37,10,5,0,0,37,38,
        5,11,0,0,38,39,3,2,1,6,39,40,6,1,-1,0,40,42,1,0,0,0,41,31,1,0,0,
        0,41,36,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,3,1,
        0,0,0,45,43,1,0,0,0,4,11,29,41,43
    ]

class T3_correctParser ( Parser ):

    grammarFileName = "T3_correct.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return '", "';'", "'break'", "'pow('", 
                     "','", "')'", "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "ID", "WS", "OP_ADD", "OP_MUL" ]

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
    INT=8
    ID=9
    WS=10
    OP_ADD=11
    OP_MUL=12

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
            return T3_correctParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.stack = ctx.stack



    class ReturnContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(T3_correctParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)


    class BreakContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)



    def stat(self):

        localctx = T3_correctParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        try:
            self.state = 11
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [T3_correctParser.T__0]:
                localctx = T3_correctParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(T3_correctParser.T__0)
                self.state = 5
                self.e(0)
                self.state = 6
                self.match(T3_correctParser.T__1)
                print("calculated:", localctx.stack)
                pass
            elif token in [T3_correctParser.T__2]:
                localctx = T3_correctParser.BreakContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(T3_correctParser.T__2)
                self.state = 10
                self.match(T3_correctParser.T__1)
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
            return T3_correctParser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.EContext
            super().__init__(parser)
            self._OP_ADD = None # Token
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T3_correctParser.EContext)
            else:
                return self.getTypedRuleContext(T3_correctParser.EContext,i)

        def OP_ADD(self):
            return self.getToken(T3_correctParser.OP_ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class BracedContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(T3_correctParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBraced" ):
                listener.enterBraced(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBraced" ):
                listener.exitBraced(self)


    class MultContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.EContext
            super().__init__(parser)
            self._OP_MUL = None # Token
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T3_correctParser.EContext)
            else:
                return self.getTypedRuleContext(T3_correctParser.EContext,i)

        def OP_MUL(self):
            return self.getToken(T3_correctParser.OP_MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)


    class PowContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.EContext
            super().__init__(parser)
            self._INT = None # Token
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(T3_correctParser.INT)
            else:
                return self.getToken(T3_correctParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)


    class IdContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(T3_correctParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T3_correctParser.EContext
            super().__init__(parser)
            self._INT = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(T3_correctParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = T3_correctParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [T3_correctParser.T__3]:
                localctx = T3_correctParser.PowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.match(T3_correctParser.T__3)
                self.state = 15
                localctx._INT = self.match(T3_correctParser.INT)
                a=int((None if localctx._INT is None else localctx._INT.text))
                self.state = 17
                self.match(T3_correctParser.T__4)
                self.state = 18
                localctx._INT = self.match(T3_correctParser.INT)
                b=int((None if localctx._INT is None else localctx._INT.text))
                self.state = 20
                self.match(T3_correctParser.T__5)

                self.getInvokingContext(0).stack.append(math.pow(a,b)); print("pow"); 
                      
                pass
            elif token in [T3_correctParser.INT]:
                localctx = T3_correctParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                localctx._INT = self.match(T3_correctParser.INT)

                self.res+=self._input.getText(localctx.start, self._input.LT(-1)); 
                self.getInvokingContext(0).stack.append(int(self._input.getText(localctx.start, self._input.LT(-1)))); 
                print("->", self.getInvokingContext(0).stack)
                      
                pass
            elif token in [T3_correctParser.ID]:
                localctx = T3_correctParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(T3_correctParser.ID)
                pass
            elif token in [T3_correctParser.T__6]:
                localctx = T3_correctParser.BracedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(T3_correctParser.T__6)
                self.state = 26
                self.e(0)
                self.state = 27
                self.match(T3_correctParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = T3_correctParser.MultContext(self, T3_correctParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        localctx._OP_MUL = self.match(T3_correctParser.OP_MUL)
                        self.state = 33
                        self.e(7)
                        make_op(self.getInvokingContext(0).stack, (None if localctx._OP_MUL is None else localctx._OP_MUL.text))
                                        
                        pass

                    elif la_ == 2:
                        localctx = T3_correctParser.AddContext(self, T3_correctParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 36
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 37
                        localctx._OP_ADD = self.match(T3_correctParser.OP_ADD)
                        self.state = 38
                        self.e(6)
                        make_op(self.getInvokingContext(0).stack, (None if localctx._OP_ADD is None else localctx._OP_ADD.text))
                                        
                        pass

             
                self.state = 45
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




