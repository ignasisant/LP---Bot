// Generated from /home/experimentor/Documents/LP/PracticaPython/cl/Expr.g by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IGUAL=1, VAR=2, COMA=3, PARO=4, PARC=5, CORO=6, CORC=7, CLAUDO=8, CLAUDC=9, 
		NUM=10, MES=11, MINUS=12, MUL=13, WS=14;
	public static final int
		RULE_root = 0, RULE_skyline = 1, RULE_createSkyline = 2, RULE_altreSkyline = 3;
	public static final String[] ruleNames = {
		"root", "skyline", "createSkyline", "altreSkyline"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "':='", null, "','", "'('", "')'", "'['", "']'", "'{'", "'}'", null, 
		"'+'", "'-'", "'*'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "IGUAL", "VAR", "COMA", "PARO", "PARC", "CORO", "CORC", "CLAUDO", 
		"CLAUDC", "NUM", "MES", "MINUS", "MUL", "WS"
	};
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
	public String getGrammarFileName() { return "Expr.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public SkylineContext skyline() {
			return getRuleContext(SkylineContext.class,0);
		}
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			skyline(0);
			setState(9);
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
		public TerminalNode PARO() { return getToken(ExprParser.PARO, 0); }
		public List<SkylineContext> skyline() {
			return getRuleContexts(SkylineContext.class);
		}
		public SkylineContext skyline(int i) {
			return getRuleContext(SkylineContext.class,i);
		}
		public TerminalNode PARC() { return getToken(ExprParser.PARC, 0); }
		public TerminalNode MINUS() { return getToken(ExprParser.MINUS, 0); }
		public CreateSkylineContext createSkyline() {
			return getRuleContext(CreateSkylineContext.class,0);
		}
		public TerminalNode VAR() { return getToken(ExprParser.VAR, 0); }
		public TerminalNode IGUAL() { return getToken(ExprParser.IGUAL, 0); }
		public TerminalNode CLAUDO() { return getToken(ExprParser.CLAUDO, 0); }
		public List<TerminalNode> NUM() { return getTokens(ExprParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(ExprParser.NUM, i);
		}
		public List<TerminalNode> COMA() { return getTokens(ExprParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ExprParser.COMA, i);
		}
		public TerminalNode CLAUDC() { return getToken(ExprParser.CLAUDC, 0); }
		public TerminalNode MUL() { return getToken(ExprParser.MUL, 0); }
		public TerminalNode MES() { return getToken(ExprParser.MES, 0); }
		public SkylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_skyline; }
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
			setState(33);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(12);
				match(PARO);
				setState(13);
				skyline(0);
				setState(14);
				match(PARC);
				}
				break;
			case 2:
				{
				setState(16);
				match(MINUS);
				setState(17);
				skyline(9);
				}
				break;
			case 3:
				{
				setState(18);
				createSkyline();
				}
				break;
			case 4:
				{
				setState(19);
				match(VAR);
				setState(20);
				match(IGUAL);
				setState(21);
				skyline(2);
				}
				break;
			case 5:
				{
				setState(22);
				match(CLAUDO);
				setState(23);
				match(NUM);
				setState(24);
				match(COMA);
				setState(25);
				match(NUM);
				setState(26);
				match(COMA);
				setState(27);
				match(NUM);
				setState(28);
				match(COMA);
				setState(29);
				match(NUM);
				setState(30);
				match(COMA);
				setState(31);
				match(NUM);
				setState(32);
				match(CLAUDC);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(50);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(35);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(36);
						match(MUL);
						setState(37);
						skyline(9);
						}
						break;
					case 2:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(38);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(39);
						match(MES);
						setState(40);
						skyline(7);
						}
						break;
					case 3:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(41);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(42);
						match(MUL);
						setState(43);
						match(NUM);
						}
						break;
					case 4:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(44);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(45);
						match(MES);
						setState(46);
						match(NUM);
						}
						break;
					case 5:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(47);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(48);
						match(MINUS);
						setState(49);
						match(NUM);
						}
						break;
					}
					} 
				}
				setState(54);
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

	public static class CreateSkylineContext extends ParserRuleContext {
		public TerminalNode PARO() { return getToken(ExprParser.PARO, 0); }
		public List<TerminalNode> NUM() { return getTokens(ExprParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(ExprParser.NUM, i);
		}
		public List<TerminalNode> COMA() { return getTokens(ExprParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ExprParser.COMA, i);
		}
		public TerminalNode PARC() { return getToken(ExprParser.PARC, 0); }
		public TerminalNode CORO() { return getToken(ExprParser.CORO, 0); }
		public CreateSkylineContext createSkyline() {
			return getRuleContext(CreateSkylineContext.class,0);
		}
		public AltreSkylineContext altreSkyline() {
			return getRuleContext(AltreSkylineContext.class,0);
		}
		public TerminalNode CORC() { return getToken(ExprParser.CORC, 0); }
		public CreateSkylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSkyline; }
	}

	public final CreateSkylineContext createSkyline() throws RecognitionException {
		CreateSkylineContext _localctx = new CreateSkylineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_createSkyline);
		try {
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				match(PARO);
				setState(56);
				match(NUM);
				setState(57);
				match(COMA);
				setState(58);
				match(NUM);
				setState(59);
				match(COMA);
				setState(60);
				match(NUM);
				setState(61);
				match(PARC);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(62);
				match(CORO);
				setState(63);
				createSkyline();
				setState(64);
				altreSkyline();
				setState(65);
				match(CORC);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
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

	public static class AltreSkylineContext extends ParserRuleContext {
		public List<TerminalNode> COMA() { return getTokens(ExprParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ExprParser.COMA, i);
		}
		public TerminalNode PARO() { return getToken(ExprParser.PARO, 0); }
		public List<TerminalNode> NUM() { return getTokens(ExprParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(ExprParser.NUM, i);
		}
		public TerminalNode PARC() { return getToken(ExprParser.PARC, 0); }
		public AltreSkylineContext altreSkyline() {
			return getRuleContext(AltreSkylineContext.class,0);
		}
		public AltreSkylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_altreSkyline; }
	}

	public final AltreSkylineContext altreSkyline() throws RecognitionException {
		AltreSkylineContext _localctx = new AltreSkylineContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_altreSkyline);
		try {
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				match(COMA);
				setState(71);
				match(PARO);
				setState(72);
				match(NUM);
				setState(73);
				match(COMA);
				setState(74);
				match(NUM);
				setState(75);
				match(COMA);
				setState(76);
				match(NUM);
				setState(77);
				match(PARC);
				setState(78);
				altreSkyline();
				}
				break;
			case CORC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
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
			return precpred(_ctx, 8);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 7);
		case 3:
			return precpred(_ctx, 5);
		case 4:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20U\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\65\n\3\f\3\16\38"+
		"\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4G\n\4\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5S\n\5\3\5\2\3\4\6\2\4\6\b\2\2"+
		"\2\\\2\n\3\2\2\2\4#\3\2\2\2\6F\3\2\2\2\bR\3\2\2\2\n\13\5\4\3\2\13\f\7"+
		"\2\2\3\f\3\3\2\2\2\r\16\b\3\1\2\16\17\7\6\2\2\17\20\5\4\3\2\20\21\7\7"+
		"\2\2\21$\3\2\2\2\22\23\7\16\2\2\23$\5\4\3\13\24$\5\6\4\2\25\26\7\4\2\2"+
		"\26\27\7\3\2\2\27$\5\4\3\4\30\31\7\n\2\2\31\32\7\f\2\2\32\33\7\5\2\2\33"+
		"\34\7\f\2\2\34\35\7\5\2\2\35\36\7\f\2\2\36\37\7\5\2\2\37 \7\f\2\2 !\7"+
		"\5\2\2!\"\7\f\2\2\"$\7\13\2\2#\r\3\2\2\2#\22\3\2\2\2#\24\3\2\2\2#\25\3"+
		"\2\2\2#\30\3\2\2\2$\66\3\2\2\2%&\f\n\2\2&\'\7\17\2\2\'\65\5\4\3\13()\f"+
		"\b\2\2)*\7\r\2\2*\65\5\4\3\t+,\f\t\2\2,-\7\17\2\2-\65\7\f\2\2./\f\7\2"+
		"\2/\60\7\r\2\2\60\65\7\f\2\2\61\62\f\6\2\2\62\63\7\16\2\2\63\65\7\f\2"+
		"\2\64%\3\2\2\2\64(\3\2\2\2\64+\3\2\2\2\64.\3\2\2\2\64\61\3\2\2\2\658\3"+
		"\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\5\3\2\2\28\66\3\2\2\29:\7\6\2\2"+
		":;\7\f\2\2;<\7\5\2\2<=\7\f\2\2=>\7\5\2\2>?\7\f\2\2?G\7\7\2\2@A\7\b\2\2"+
		"AB\5\6\4\2BC\5\b\5\2CD\7\t\2\2DG\3\2\2\2EG\3\2\2\2F9\3\2\2\2F@\3\2\2\2"+
		"FE\3\2\2\2G\7\3\2\2\2HI\7\5\2\2IJ\7\6\2\2JK\7\f\2\2KL\7\5\2\2LM\7\f\2"+
		"\2MN\7\5\2\2NO\7\f\2\2OP\7\7\2\2PS\5\b\5\2QS\3\2\2\2RH\3\2\2\2RQ\3\2\2"+
		"\2S\t\3\2\2\2\7#\64\66FR";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}