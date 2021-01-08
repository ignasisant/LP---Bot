# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\3\6\3$\n\3\r\3\16\3%\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\6\13\67\n\13\r\13\16\138\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\6\17B\n\17\r\17\16\17C\3\17\3\17\2\2\20\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\3\2\5\4\2C\\c|\3\2\62;\4\2\f\f\"\"\2I\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2")
        buf.write("\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2\2\2\23\63")
        buf.write("\3\2\2\2\25\66\3\2\2\2\27:\3\2\2\2\31<\3\2\2\2\33>\3\2")
        buf.write("\2\2\35A\3\2\2\2\37 \7<\2\2 !\7?\2\2!\4\3\2\2\2\"$\t\2")
        buf.write("\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\6\3\2\2")
        buf.write("\2\'(\7.\2\2(\b\3\2\2\2)*\7*\2\2*\n\3\2\2\2+,\7+\2\2,")
        buf.write("\f\3\2\2\2-.\7]\2\2.\16\3\2\2\2/\60\7_\2\2\60\20\3\2\2")
        buf.write("\2\61\62\7}\2\2\62\22\3\2\2\2\63\64\7\177\2\2\64\24\3")
        buf.write("\2\2\2\65\67\t\3\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2")
        buf.write("\2\289\3\2\2\29\26\3\2\2\2:;\7-\2\2;\30\3\2\2\2<=\7/\2")
        buf.write("\2=\32\3\2\2\2>?\7,\2\2?\34\3\2\2\2@B\t\4\2\2A@\3\2\2")
        buf.write("\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\17\2\2")
        buf.write("F\36\3\2\2\2\6\2%8C\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IGUAL = 1
    VAR = 2
    COMA = 3
    PARO = 4
    PARC = 5
    CORO = 6
    CORC = 7
    CLAUDO = 8
    CLAUDC = 9
    NUM = 10
    MES = 11
    MINUS = 12
    MUL = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "','", "'('", "')'", "'['", "']'", "'{'", "'}'", "'+'", 
            "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "IGUAL", "VAR", "COMA", "PARO", "PARC", "CORO", "CORC", "CLAUDO", 
            "CLAUDC", "NUM", "MES", "MINUS", "MUL", "WS" ]

    ruleNames = [ "IGUAL", "VAR", "COMA", "PARO", "PARC", "CORO", "CORC", 
                  "CLAUDO", "CLAUDC", "NUM", "MES", "MINUS", "MUL", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


