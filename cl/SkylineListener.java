// Generated from Skyline.g by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SkylineParser}.
 */
public interface SkylineListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SkylineParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(SkylineParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link SkylineParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(SkylineParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link SkylineParser#skyline}.
	 * @param ctx the parse tree
	 */
	void enterSkyline(SkylineParser.SkylineContext ctx);
	/**
	 * Exit a parse tree produced by {@link SkylineParser#skyline}.
	 * @param ctx the parse tree
	 */
	void exitSkyline(SkylineParser.SkylineContext ctx);
}