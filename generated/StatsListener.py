# Generated from grammar/Stats.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .StatsParser import StatsParser
else:
    from StatsParser import StatsParser

# This class defines a complete listener for a parse tree produced by StatsParser.
class StatsListener(ParseTreeListener):

    # Enter a parse tree produced by StatsParser#prog.
    def enterProg(self, ctx:StatsParser.ProgContext):
        pass

    # Exit a parse tree produced by StatsParser#prog.
    def exitProg(self, ctx:StatsParser.ProgContext):
        pass


    # Enter a parse tree produced by StatsParser#stmt.
    def enterStmt(self, ctx:StatsParser.StmtContext):
        pass

    # Exit a parse tree produced by StatsParser#stmt.
    def exitStmt(self, ctx:StatsParser.StmtContext):
        pass


    # Enter a parse tree produced by StatsParser#loadStmt.
    def enterLoadStmt(self, ctx:StatsParser.LoadStmtContext):
        pass

    # Exit a parse tree produced by StatsParser#loadStmt.
    def exitLoadStmt(self, ctx:StatsParser.LoadStmtContext):
        pass


    # Enter a parse tree produced by StatsParser#queryStmt.
    def enterQueryStmt(self, ctx:StatsParser.QueryStmtContext):
        pass

    # Exit a parse tree produced by StatsParser#queryStmt.
    def exitQueryStmt(self, ctx:StatsParser.QueryStmtContext):
        pass


    # Enter a parse tree produced by StatsParser#aggList.
    def enterAggList(self, ctx:StatsParser.AggListContext):
        pass

    # Exit a parse tree produced by StatsParser#aggList.
    def exitAggList(self, ctx:StatsParser.AggListContext):
        pass


    # Enter a parse tree produced by StatsParser#aggExpr.
    def enterAggExpr(self, ctx:StatsParser.AggExprContext):
        pass

    # Exit a parse tree produced by StatsParser#aggExpr.
    def exitAggExpr(self, ctx:StatsParser.AggExprContext):
        pass


    # Enter a parse tree produced by StatsParser#aggFunc.
    def enterAggFunc(self, ctx:StatsParser.AggFuncContext):
        pass

    # Exit a parse tree produced by StatsParser#aggFunc.
    def exitAggFunc(self, ctx:StatsParser.AggFuncContext):
        pass


    # Enter a parse tree produced by StatsParser#histogramStmt.
    def enterHistogramStmt(self, ctx:StatsParser.HistogramStmtContext):
        pass

    # Exit a parse tree produced by StatsParser#histogramStmt.
    def exitHistogramStmt(self, ctx:StatsParser.HistogramStmtContext):
        pass


    # Enter a parse tree produced by StatsParser#boolExpr.
    def enterBoolExpr(self, ctx:StatsParser.BoolExprContext):
        pass

    # Exit a parse tree produced by StatsParser#boolExpr.
    def exitBoolExpr(self, ctx:StatsParser.BoolExprContext):
        pass


    # Enter a parse tree produced by StatsParser#comparison.
    def enterComparison(self, ctx:StatsParser.ComparisonContext):
        pass

    # Exit a parse tree produced by StatsParser#comparison.
    def exitComparison(self, ctx:StatsParser.ComparisonContext):
        pass


    # Enter a parse tree produced by StatsParser#comparator.
    def enterComparator(self, ctx:StatsParser.ComparatorContext):
        pass

    # Exit a parse tree produced by StatsParser#comparator.
    def exitComparator(self, ctx:StatsParser.ComparatorContext):
        pass


    # Enter a parse tree produced by StatsParser#value.
    def enterValue(self, ctx:StatsParser.ValueContext):
        pass

    # Exit a parse tree produced by StatsParser#value.
    def exitValue(self, ctx:StatsParser.ValueContext):
        pass



del StatsParser