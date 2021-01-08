// Generated from Skyline.g by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IGUAL=1, VAR=2, COMA=3, PARO=4, PARC=5, CORO=6, CORC=7, CLAUDO=8, CLAUDC=9, 
		NUM=10, MES=11, MINUS=12, MUL=13, WS=14;
	public static final int
		RULE_root = 0, RULE_skyline = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "skyline"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':='", null, "','", "'('", "')'", "'['", "']'", "'{'", "'}'", 
			null, "'+'", "'-'", "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IGUAL", "VAR", "COMA", "PARO", "PARC", "CORO", "CORC", "CLAUDO", 
			"CLAUDC", "NUM", "MES", "MINUS", "MUL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Skyline.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SkylineParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public SkylineContext skyline() {
			return getRuleContext(SkylineContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SkylineParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SkylineListener ) ((SkylineListener)listener).enterRoot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SkylineListener ) ((SkylineListener)listener).exitRoot(this);
		}
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(4);
			skyline(0);
			setState(5);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SkylineContext extends ParserRuleContext {
		public TerminalNode PARO() { return getToken(SkylineParser.PARO, 0); }
		public List<SkylineContext> skyline() {
			return getRuleContexts(SkylineContext.class);
		}
		public SkylineContext skyline(int i) {
			return getRuleContext(SkylineContext.class,i);
		}
		public TerminalNode PARC() { return getToken(SkylineParser.PARC, 0); }
		public TerminalNode MINUS() { return getToken(SkylineParser.MINUS, 0); }
		public TerminalNode VAR() { return getToken(SkylineParser.VAR, 0); }
		public TerminalNode IGUAL() { return getToken(SkylineParser.IGUAL, 0); }
		public TerminalNode CORO() { return getToken(SkylineParser.CORO, 0); }
		public TerminalNode CORC() { return getToken(SkylineParser.CORC, 0); }
		public List<TerminalNode> COMA() { return getTokens(SkylineParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(SkylineParser.COMA, i);
		}
		public List<TerminalNode> NUM() { return getTokens(SkylineParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(SkylineParser.NUM, i);
		}
		public TerminalNode CLAUDO() { return getToken(SkylineParser.CLAUDO, 0); }
		public TerminalNode CLAUDC() { return getToken(SkylineParser.CLAUDC, 0); }
		public TerminalNode MUL() { return getToken(SkylineParser.MUL, 0); }
		public TerminalNode MES() { return getToken(SkylineParser.MES, 0); }
		public SkylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_skyline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SkylineListener ) ((SkylineListener)listener).enterSkyline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SkylineListener ) ((SkylineListener)listener).exitSkyline(this);
		}
	}

	public final SkylineContext skyline() throws RecognitionException {
		return skyline(0);
	}

	private SkylineContext skyline(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		SkylineContext _localctx = new SkylineContext(_ctx, _parentState);
		SkylineContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_skyline, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(8);
				match(PARO);
				setState(9);
				skyline(0);
				setState(10);
				match(PARC);
				}
				break;
			case 2:
				{
				setState(12);
				match(MINUS);
				setState(13);
				skyline(17);
				}
				break;
			case 3:
				{
				setState(14);
				match(VAR);
				setState(15);
				match(IGUAL);
				setState(16);
				skyline(10);
				}
				break;
			case 4:
				{
				setState(17);
				match(CORO);
				setState(18);
				skyline(0);
				setState(19);
				skyline(0);
				setState(20);
				match(CORC);
				}
				break;
			case 5:
				{
				setState(22);
				match(COMA);
				setState(23);
				match(PARO);
				setState(24);
				match(NUM);
				setState(25);
				match(COMA);
				setState(26);
				match(NUM);
				setState(27);
				match(COMA);
				setState(28);
				match(NUM);
				setState(29);
				match(PARC);
				setState(30);
				skyline(8);
				}
				break;
			case 6:
				{
				setState(31);
				match(PARO);
				setState(32);
				match(NUM);
				setState(33);
				match(COMA);
				setState(34);
				match(NUM);
				setState(35);
				match(COMA);
				setState(36);
				match(NUM);
				setState(37);
				match(PARC);
				}
				break;
			case 7:
				{
				setState(38);
				match(CLAUDO);
				setState(39);
				match(NUM);
				setState(40);
				match(COMA);
				setState(41);
				match(NUM);
				setState(42);
				match(COMA);
				setState(43);
				match(NUM);
				setState(44);
				match(COMA);
				setState(45);
				match(NUM);
				setState(46);
				match(COMA);
				setState(47);
				match(NUM);
				setState(48);
				match(CLAUDC);
				}
				break;
			case 8:
				{
				setState(49);
				match(MINUS);
				setState(50);
				match(VAR);
				}
				break;
			case 9:
				{
				setState(51);
				match(VAR);
				setState(52);
				match(MUL);
				setState(53);
				match(NUM);
				}
				break;
			case 10:
				{
				setState(54);
				match(VAR);
				setState(55);
				match(MES);
				setState(56);
				skyline(3);
				}
				break;
			case 11:
				{
				setState(57);
				match(VAR);
				}
				break;
			case 12:
				{
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(81);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(79);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(61);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(62);
						match(MUL);
						setState(63);
						skyline(17);
						}
						break;
					case 2:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(64);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(65);
						match(MES);
						setState(66);
						skyline(15);
						}
						break;
					case 3:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(67);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(68);
						match(MUL);
						setState(69);
						match(NUM);
						}
						break;
					case 4:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(70);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(71);
						match(MES);
						setState(72);
						match(NUM);
						}
						break;
					case 5:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(73);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(74);
						match(MES);
						setState(75);
						match(VAR);
						}
						break;
					case 6:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(76);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(77);
						match(MINUS);
						setState(78);
						match(NUM);
						}
						break;
					}
					} 
				}
				setState(83);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return skyline_sempred((SkylineContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean skyline_sempred(SkylineContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 16);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 15);
		case 3:
			return precpred(_ctx, 13);
		case 4:
			return precpred(_ctx, 12);
		case 5:
			return precpred(_ctx, 11);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20W\4\2\t\2\4\3\t"+
		"\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\5\3>\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\7\3R\n\3\f\3\16\3U\13\3\3\3\2\3\4\4\2\4\2\2\2"+
		"e\2\6\3\2\2\2\4=\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\b\3\1"+
		"\2\n\13\7\6\2\2\13\f\5\4\3\2\f\r\7\7\2\2\r>\3\2\2\2\16\17\7\16\2\2\17"+
		">\5\4\3\23\20\21\7\4\2\2\21\22\7\3\2\2\22>\5\4\3\f\23\24\7\b\2\2\24\25"+
		"\5\4\3\2\25\26\5\4\3\2\26\27\7\t\2\2\27>\3\2\2\2\30\31\7\5\2\2\31\32\7"+
		"\6\2\2\32\33\7\f\2\2\33\34\7\5\2\2\34\35\7\f\2\2\35\36\7\5\2\2\36\37\7"+
		"\f\2\2\37 \7\7\2\2 >\5\4\3\n!\"\7\6\2\2\"#\7\f\2\2#$\7\5\2\2$%\7\f\2\2"+
		"%&\7\5\2\2&\'\7\f\2\2\'>\7\7\2\2()\7\n\2\2)*\7\f\2\2*+\7\5\2\2+,\7\f\2"+
		"\2,-\7\5\2\2-.\7\f\2\2./\7\5\2\2/\60\7\f\2\2\60\61\7\5\2\2\61\62\7\f\2"+
		"\2\62>\7\13\2\2\63\64\7\16\2\2\64>\7\4\2\2\65\66\7\4\2\2\66\67\7\17\2"+
		"\2\67>\7\f\2\289\7\4\2\29:\7\r\2\2:>\5\4\3\5;>\7\4\2\2<>\3\2\2\2=\t\3"+
		"\2\2\2=\16\3\2\2\2=\20\3\2\2\2=\23\3\2\2\2=\30\3\2\2\2=!\3\2\2\2=(\3\2"+
		"\2\2=\63\3\2\2\2=\65\3\2\2\2=8\3\2\2\2=;\3\2\2\2=<\3\2\2\2>S\3\2\2\2?"+
		"@\f\22\2\2@A\7\17\2\2AR\5\4\3\23BC\f\20\2\2CD\7\r\2\2DR\5\4\3\21EF\f\21"+
		"\2\2FG\7\17\2\2GR\7\f\2\2HI\f\17\2\2IJ\7\r\2\2JR\7\f\2\2KL\f\16\2\2LM"+
		"\7\r\2\2MR\7\4\2\2NO\f\r\2\2OP\7\16\2\2PR\7\f\2\2Q?\3\2\2\2QB\3\2\2\2"+
		"QE\3\2\2\2QH\3\2\2\2QK\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2"+
		"T\5\3\2\2\2US\3\2\2\2\5=QS";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}