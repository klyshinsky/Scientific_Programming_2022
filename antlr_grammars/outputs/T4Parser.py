# Generated from T4.g4 by ANTLR 4.10.1
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
        4,1,13,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,4,0,11,8,0,11,
        0,12,0,12,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,
        1,1,1,5,1,28,8,1,10,1,12,1,31,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,5,2,41,8,2,10,2,12,2,44,9,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        69,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,8,3,10,3,12,
        3,84,9,3,1,3,0,1,6,4,0,2,4,6,0,0,92,0,10,1,0,0,0,2,14,1,0,0,0,4,
        49,1,0,0,0,6,68,1,0,0,0,8,11,3,2,1,0,9,11,3,4,2,0,10,8,1,0,0,0,10,
        9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,1,1,0,0,0,
        14,15,5,1,0,0,15,16,5,10,0,0,16,22,6,1,-1,0,17,18,5,2,0,0,18,19,
        5,10,0,0,19,21,6,1,-1,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,
        0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,29,5,3,0,0,26,28,
        5,11,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,
        30,32,1,0,0,0,31,29,1,0,0,0,32,33,6,1,-1,0,33,3,1,0,0,0,34,35,5,
        10,0,0,35,36,6,2,-1,0,36,37,5,4,0,0,37,38,3,6,3,0,38,42,5,3,0,0,
        39,41,5,11,0,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,
        0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,6,2,-1,0,46,50,1,0,0,0,47,
        48,5,5,0,0,48,50,5,3,0,0,49,34,1,0,0,0,49,47,1,0,0,0,50,5,1,0,0,
        0,51,52,6,3,-1,0,52,53,5,6,0,0,53,54,5,9,0,0,54,55,6,3,-1,0,55,56,
        5,2,0,0,56,57,5,9,0,0,57,58,6,3,-1,0,58,59,5,7,0,0,59,69,6,3,-1,
        0,60,61,5,9,0,0,61,69,6,3,-1,0,62,63,5,10,0,0,63,69,6,3,-1,0,64,
        65,5,8,0,0,65,66,3,6,3,0,66,67,5,7,0,0,67,69,1,0,0,0,68,51,1,0,0,
        0,68,60,1,0,0,0,68,62,1,0,0,0,68,64,1,0,0,0,69,82,1,0,0,0,70,71,
        10,6,0,0,71,72,5,13,0,0,72,73,3,6,3,7,73,74,6,3,-1,0,74,81,1,0,0,
        0,75,76,10,5,0,0,76,77,5,12,0,0,77,78,3,6,3,6,78,79,6,3,-1,0,79,
        81,1,0,0,0,80,70,1,0,0,0,80,75,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,
        0,82,83,1,0,0,0,83,7,1,0,0,0,84,82,1,0,0,0,9,10,12,22,29,42,49,68,
        80,82
    ]

class T4Parser ( Parser ):

    grammarFileName = "T4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "','", "';'", "'='", "'break'", 
                     "'pow('", "')'", "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "ID", "WS", "OP_ADD", "OP_MUL" ]

    RULE_start = 0
    RULE_decl = 1
    RULE_a_expr = 2
    RULE_e = 3

    ruleNames =  [ "start", "decl", "a_expr", "e" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INT=9
    ID=10
    WS=11
    OP_ADD=12
    OP_MUL=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    values = {}



    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T4Parser.DeclContext)
            else:
                return self.getTypedRuleContext(T4Parser.DeclContext,i)


        def a_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T4Parser.A_exprContext)
            else:
                return self.getTypedRuleContext(T4Parser.A_exprContext,i)


        def getRuleIndex(self):
            return T4Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = T4Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [T4Parser.T__0]:
                    self.state = 8
                    self.decl()
                    pass
                elif token in [T4Parser.T__4, T4Parser.ID]:
                    self.state = 9
                    self.a_expr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << T4Parser.T__0) | (1 << T4Parser.T__4) | (1 << T4Parser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(T4Parser.ID)
            else:
                return self.getToken(T4Parser.ID, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(T4Parser.WS)
            else:
                return self.getToken(T4Parser.WS, i)

        def getRuleIndex(self):
            return T4Parser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = T4Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(T4Parser.T__0)
            self.state = 15
            localctx._ID = self.match(T4Parser.ID)
            self.values[(None if localctx._ID is None else localctx._ID.text)]=0
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==T4Parser.T__1:
                self.state = 17
                self.match(T4Parser.T__1)
                self.state = 18
                localctx._ID = self.match(T4Parser.ID)
                self.values[(None if localctx._ID is None else localctx._ID.text)]=0
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(T4Parser.T__2)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==T4Parser.WS:
                self.state = 26
                self.match(T4Parser.WS)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            print('delcared', self._input.getText(localctx.start, self._input.LT(-1)))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.stack = []


        def getRuleIndex(self):
            return T4Parser.RULE_a_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.stack = ctx.stack



    class ReturnContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.A_exprContext
            super().__init__(parser)
            self._ID = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(T4Parser.ID, 0)
        def e(self):
            return self.getTypedRuleContext(T4Parser.EContext,0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(T4Parser.WS)
            else:
                return self.getToken(T4Parser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)


    class BreakContext(A_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.A_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)



    def a_expr(self):

        localctx = T4Parser.A_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_a_expr)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [T4Parser.ID]:
                localctx = T4Parser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx._ID = self.match(T4Parser.ID)
                if (None if localctx._ID is None else localctx._ID.text) not in self.values.keys(): print(f"wasn't declared:{(None if localctx._ID is None else localctx._ID.text)}")
                self.state = 36
                self.match(T4Parser.T__3)
                self.state = 37
                self.e(0)
                self.state = 38
                self.match(T4Parser.T__2)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==T4Parser.WS:
                    self.state = 39
                    self.match(T4Parser.WS)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                print("calculated:", localctx.stack);self.values[(None if localctx._ID is None else localctx._ID.text)]=localctx.stack[-1];
                pass
            elif token in [T4Parser.T__4]:
                localctx = T4Parser.BreakContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(T4Parser.T__4)
                self.state = 48
                self.match(T4Parser.T__2)
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
            return T4Parser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.EContext
            super().__init__(parser)
            self._OP_ADD = None # Token
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T4Parser.EContext)
            else:
                return self.getTypedRuleContext(T4Parser.EContext,i)

        def OP_ADD(self):
            return self.getToken(T4Parser.OP_ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class BracedContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(T4Parser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBraced" ):
                listener.enterBraced(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBraced" ):
                listener.exitBraced(self)


    class MultContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.EContext
            super().__init__(parser)
            self._OP_MUL = None # Token
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(T4Parser.EContext)
            else:
                return self.getTypedRuleContext(T4Parser.EContext,i)

        def OP_MUL(self):
            return self.getToken(T4Parser.OP_MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)


    class PowContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.EContext
            super().__init__(parser)
            self._INT = None # Token
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(T4Parser.INT)
            else:
                return self.getToken(T4Parser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)


    class IdContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.EContext
            super().__init__(parser)
            self._ID = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(T4Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a T4Parser.EContext
            super().__init__(parser)
            self._INT = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(T4Parser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = T4Parser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [T4Parser.T__5]:
                localctx = T4Parser.PowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self.match(T4Parser.T__5)
                self.state = 53
                localctx._INT = self.match(T4Parser.INT)
                a=int((None if localctx._INT is None else localctx._INT.text))
                self.state = 55
                self.match(T4Parser.T__1)
                self.state = 56
                localctx._INT = self.match(T4Parser.INT)
                b=int((None if localctx._INT is None else localctx._INT.text))
                self.state = 58
                self.match(T4Parser.T__6)

                self.getInvokingContext(2).stack.append(math.pow(a,b)); print("pow"); 
                      
                pass
            elif token in [T4Parser.INT]:
                localctx = T4Parser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                localctx._INT = self.match(T4Parser.INT)

                self.getInvokingContext(2).stack.append(int(self._input.getText(localctx.start, self._input.LT(-1)))); 
                print("->", self.getInvokingContext(2).stack)
                      
                pass
            elif token in [T4Parser.ID]:
                localctx = T4Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                localctx._ID = self.match(T4Parser.ID)

                if (None if localctx._ID is None else localctx._ID.text) not in self.values.keys(): print(f"wasn't declared:{(None if localctx._ID is None else localctx._ID.text)}")
                else: self.getInvokingContext(2).stack.append(self.values[self._input.getText(localctx.start, self._input.LT(-1))]); 
                       
                pass
            elif token in [T4Parser.T__7]:
                localctx = T4Parser.BracedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(T4Parser.T__7)
                self.state = 65
                self.e(0)
                self.state = 66
                self.match(T4Parser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = T4Parser.MultContext(self, T4Parser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 70
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 71
                        localctx._OP_MUL = self.match(T4Parser.OP_MUL)
                        self.state = 72
                        self.e(7)
                        make_op(self.getInvokingContext(2).stack, (None if localctx._OP_MUL is None else localctx._OP_MUL.text))
                                        
                        pass

                    elif la_ == 2:
                        localctx = T4Parser.AddContext(self, T4Parser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        localctx._OP_ADD = self.match(T4Parser.OP_ADD)
                        self.state = 77
                        self.e(6)
                        make_op(self.getInvokingContext(2).stack, (None if localctx._OP_ADD is None else localctx._OP_ADD.text))
                                        
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self._ctx.stop = self._input.LT(-1)
            print("processed", self.getInvokingContext(2).stack);
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
        self._predicates[3] = self.e_sempred
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
         




