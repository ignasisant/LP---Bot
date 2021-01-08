# Generated from Skyline.g by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("W\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3>\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write("R\n\3\f\3\16\3U\13\3\3\3\2\3\4\4\2\4\2\2\2e\2\6\3\2\2")
        buf.write("\2\4=\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n")
        buf.write("\b\3\1\2\n\13\7\6\2\2\13\f\5\4\3\2\f\r\7\7\2\2\r>\3\2")
        buf.write("\2\2\16\17\7\16\2\2\17>\5\4\3\23\20\21\7\4\2\2\21\22\7")
        buf.write("\3\2\2\22>\5\4\3\f\23\24\7\b\2\2\24\25\5\4\3\2\25\26\5")
        buf.write("\4\3\2\26\27\7\t\2\2\27>\3\2\2\2\30\31\7\5\2\2\31\32\7")
        buf.write("\6\2\2\32\33\7\f\2\2\33\34\7\5\2\2\34\35\7\f\2\2\35\36")
        buf.write("\7\5\2\2\36\37\7\f\2\2\37 \7\7\2\2 >\5\4\3\n!\"\7\6\2")
        buf.write("\2\"#\7\f\2\2#$\7\5\2\2$%\7\f\2\2%&\7\5\2\2&\'\7\f\2\2")
        buf.write("\'>\7\7\2\2()\7\n\2\2)*\7\f\2\2*+\7\5\2\2+,\7\f\2\2,-")
        buf.write("\7\5\2\2-.\7\f\2\2./\7\5\2\2/\60\7\f\2\2\60\61\7\5\2\2")
        buf.write("\61\62\7\f\2\2\62>\7\13\2\2\63\64\7\16\2\2\64>\7\4\2\2")
        buf.write("\65\66\7\4\2\2\66\67\7\17\2\2\67>\7\f\2\289\7\4\2\29:")
        buf.write("\7\r\2\2:>\5\4\3\5;>\7\4\2\2<>\3\2\2\2=\t\3\2\2\2=\16")
        buf.write("\3\2\2\2=\20\3\2\2\2=\23\3\2\2\2=\30\3\2\2\2=!\3\2\2\2")
        buf.write("=(\3\2\2\2=\63\3\2\2\2=\65\3\2\2\2=8\3\2\2\2=;\3\2\2\2")
        buf.write("=<\3\2\2\2>S\3\2\2\2?@\f\22\2\2@A\7\17\2\2AR\5\4\3\23")
        buf.write("BC\f\20\2\2CD\7\r\2\2DR\5\4\3\21EF\f\21\2\2FG\7\17\2\2")
        buf.write("GR\7\f\2\2HI\f\17\2\2IJ\7\r\2\2JR\7\f\2\2KL\f\16\2\2L")
        buf.write("M\7\r\2\2MR\7\4\2\2NO\f\r\2\2OP\7\16\2\2PR\7\f\2\2Q?\3")
        buf.write("\2\2\2QB\3\2\2\2QE\3\2\2\2QH\3\2\2\2QK\3\2\2\2QN\3\2\2")
        buf.write("\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\5\3\2\2\2US\3\2\2\2")
        buf.write("\5=QS")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "<INVALID>", "','", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "<INVALID>", "'+'", "'-'", 
                     "'*'" ]

    symbolicNames = [ "<INVALID>", "IGUAL", "VAR", "COMA", "PARO", "PARC", 
                      "CORO", "CORC", "CLAUDO", "CLAUDC", "NUM", "MES", 
                      "MINUS", "MUL", "WS" ]

    RULE_root = 0
    RULE_skyline = 1

    ruleNames =  [ "root", "skyline" ]

    EOF = Token.EOF
    IGUAL=1
    VAR=2
    COMA=3
    PARO=4
    PARC=5
    CORO=6
    CORC=7
    CLAUDO=8
    CLAUDC=9
    NUM=10
    MES=11
    MINUS=12
    MUL=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.skyline(0)
            self.state = 5
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARO(self):
            return self.getToken(SkylineParser.PARO, 0)

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)


        def PARC(self):
            return self.getToken(SkylineParser.PARC, 0)

        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)

        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def IGUAL(self):
            return self.getToken(SkylineParser.IGUAL, 0)

        def CORO(self):
            return self.getToken(SkylineParser.CORO, 0)

        def CORC(self):
            return self.getToken(SkylineParser.CORC, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMA)
            else:
                return self.getToken(SkylineParser.COMA, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def CLAUDO(self):
            return self.getToken(SkylineParser.CLAUDO, 0)

        def CLAUDC(self):
            return self.getToken(SkylineParser.CLAUDC, 0)

        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline" ):
                return visitor.visitSkyline(self)
            else:
                return visitor.visitChildren(self)



    def skyline(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SkylineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_skyline, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                self.match(SkylineParser.PARO)
                self.state = 9
                self.skyline(0)
                self.state = 10
                self.match(SkylineParser.PARC)
                pass

            elif la_ == 2:
                self.state = 12
                self.match(SkylineParser.MINUS)
                self.state = 13
                self.skyline(17)
                pass

            elif la_ == 3:
                self.state = 14
                self.match(SkylineParser.VAR)
                self.state = 15
                self.match(SkylineParser.IGUAL)
                self.state = 16
                self.skyline(10)
                pass

            elif la_ == 4:
                self.state = 17
                self.match(SkylineParser.CORO)
                self.state = 18
                self.skyline(0)
                self.state = 19
                self.skyline(0)
                self.state = 20
                self.match(SkylineParser.CORC)
                pass

            elif la_ == 5:
                self.state = 22
                self.match(SkylineParser.COMA)
                self.state = 23
                self.match(SkylineParser.PARO)
                self.state = 24
                self.match(SkylineParser.NUM)
                self.state = 25
                self.match(SkylineParser.COMA)
                self.state = 26
                self.match(SkylineParser.NUM)
                self.state = 27
                self.match(SkylineParser.COMA)
                self.state = 28
                self.match(SkylineParser.NUM)
                self.state = 29
                self.match(SkylineParser.PARC)
                self.state = 30
                self.skyline(8)
                pass

            elif la_ == 6:
                self.state = 31
                self.match(SkylineParser.PARO)
                self.state = 32
                self.match(SkylineParser.NUM)
                self.state = 33
                self.match(SkylineParser.COMA)
                self.state = 34
                self.match(SkylineParser.NUM)
                self.state = 35
                self.match(SkylineParser.COMA)
                self.state = 36
                self.match(SkylineParser.NUM)
                self.state = 37
                self.match(SkylineParser.PARC)
                pass

            elif la_ == 7:
                self.state = 38
                self.match(SkylineParser.CLAUDO)
                self.state = 39
                self.match(SkylineParser.NUM)
                self.state = 40
                self.match(SkylineParser.COMA)
                self.state = 41
                self.match(SkylineParser.NUM)
                self.state = 42
                self.match(SkylineParser.COMA)
                self.state = 43
                self.match(SkylineParser.NUM)
                self.state = 44
                self.match(SkylineParser.COMA)
                self.state = 45
                self.match(SkylineParser.NUM)
                self.state = 46
                self.match(SkylineParser.COMA)
                self.state = 47
                self.match(SkylineParser.NUM)
                self.state = 48
                self.match(SkylineParser.CLAUDC)
                pass

            elif la_ == 8:
                self.state = 49
                self.match(SkylineParser.MINUS)
                self.state = 50
                self.match(SkylineParser.VAR)
                pass

            elif la_ == 9:
                self.state = 51
                self.match(SkylineParser.VAR)
                self.state = 52
                self.match(SkylineParser.MUL)
                self.state = 53
                self.match(SkylineParser.NUM)
                pass

            elif la_ == 10:
                self.state = 54
                self.match(SkylineParser.VAR)
                self.state = 55
                self.match(SkylineParser.MES)
                self.state = 56
                self.skyline(3)
                pass

            elif la_ == 11:
                self.state = 57
                self.match(SkylineParser.VAR)
                pass

            elif la_ == 12:
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 61
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 62
                        self.match(SkylineParser.MUL)
                        self.state = 63
                        self.skyline(17)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 64
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 65
                        self.match(SkylineParser.MES)
                        self.state = 66
                        self.skyline(15)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 67
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 68
                        self.match(SkylineParser.MUL)
                        self.state = 69
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 70
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 71
                        self.match(SkylineParser.MES)
                        self.state = 72
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 73
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 74
                        self.match(SkylineParser.MES)
                        self.state = 75
                        self.match(SkylineParser.VAR)
                        pass

                    elif la_ == 6:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 76
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 77
                        self.match(SkylineParser.MINUS)
                        self.state = 78
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self._predicates[1] = self.skyline_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def skyline_sempred(self, localctx:SkylineContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         




