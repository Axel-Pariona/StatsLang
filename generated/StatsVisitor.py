# Generated from grammar/Stats.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .StatsParser import StatsParser
else:
    from StatsParser import StatsParser

# This class defines a complete generic visitor for a parse tree produced by StatsParser.

class StatsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StatsParser#prog.
    def visitProg(self, ctx:StatsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#stmt.
    def visitStmt(self, ctx:StatsParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#loadStmt.
    def visitLoadStmt(self, ctx:StatsParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#queryStmt.
    def visitQueryStmt(self, ctx:StatsParser.QueryStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#aggList.
    def visitAggList(self, ctx:StatsParser.AggListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#aggExpr.
    def visitAggExpr(self, ctx:StatsParser.AggExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#aggFunc.
    def visitAggFunc(self, ctx:StatsParser.AggFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#histogramStmt.
    def visitHistogramStmt(self, ctx:StatsParser.HistogramStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#boolExpr.
    def visitBoolExpr(self, ctx:StatsParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#comparison.
    def visitComparison(self, ctx:StatsParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#comparator.
    def visitComparator(self, ctx:StatsParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatsParser#value.
    def visitValue(self, ctx:StatsParser.ValueContext):
        return self.visitChildren(ctx)



del StatsParser