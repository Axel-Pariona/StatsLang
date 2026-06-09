# Generated from grammar/Stats.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,
        8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,5,4,56,8,
        4,10,4,12,4,59,9,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,67,8,5,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,3,7,76,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,84,8,8,
        1,8,1,8,1,8,1,8,1,8,1,8,5,8,92,8,8,10,8,12,8,95,9,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,11,1,11,1,11,0,1,16,12,0,2,4,6,8,10,12,14,16,18,
        20,22,0,4,2,0,24,24,27,27,1,0,5,9,1,0,18,23,1,0,25,26,102,0,27,1,
        0,0,0,2,41,1,0,0,0,4,43,1,0,0,0,6,46,1,0,0,0,8,52,1,0,0,0,10,60,
        1,0,0,0,12,68,1,0,0,0,14,70,1,0,0,0,16,83,1,0,0,0,18,96,1,0,0,0,
        20,100,1,0,0,0,22,102,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,
        30,31,5,0,0,1,31,1,1,0,0,0,32,33,3,4,2,0,33,34,5,14,0,0,34,42,1,
        0,0,0,35,36,3,6,3,0,36,37,5,14,0,0,37,42,1,0,0,0,38,39,3,14,7,0,
        39,40,5,14,0,0,40,42,1,0,0,0,41,32,1,0,0,0,41,35,1,0,0,0,41,38,1,
        0,0,0,42,3,1,0,0,0,43,44,5,1,0,0,44,45,5,25,0,0,45,5,1,0,0,0,46,
        47,5,2,0,0,47,50,3,8,4,0,48,49,5,3,0,0,49,51,3,16,8,0,50,48,1,0,
        0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,57,3,10,5,0,53,54,5,15,0,0,54,
        56,3,10,5,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,
        0,0,58,9,1,0,0,0,59,57,1,0,0,0,60,61,3,12,6,0,61,62,5,16,0,0,62,
        63,7,0,0,0,63,66,5,17,0,0,64,65,5,4,0,0,65,67,5,27,0,0,66,64,1,0,
        0,0,66,67,1,0,0,0,67,11,1,0,0,0,68,69,7,1,0,0,69,13,1,0,0,0,70,71,
        5,10,0,0,71,75,5,27,0,0,72,73,5,11,0,0,73,74,5,18,0,0,74,76,5,26,
        0,0,75,72,1,0,0,0,75,76,1,0,0,0,76,15,1,0,0,0,77,78,6,8,-1,0,78,
        79,5,16,0,0,79,80,3,16,8,0,80,81,5,17,0,0,81,84,1,0,0,0,82,84,3,
        18,9,0,83,77,1,0,0,0,83,82,1,0,0,0,84,93,1,0,0,0,85,86,10,4,0,0,
        86,87,5,12,0,0,87,92,3,16,8,5,88,89,10,3,0,0,89,90,5,13,0,0,90,92,
        3,16,8,4,91,85,1,0,0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,
        93,94,1,0,0,0,94,17,1,0,0,0,95,93,1,0,0,0,96,97,5,27,0,0,97,98,3,
        20,10,0,98,99,3,22,11,0,99,19,1,0,0,0,100,101,7,2,0,0,101,21,1,0,
        0,0,102,103,7,3,0,0,103,23,1,0,0,0,9,27,41,50,57,66,75,83,91,93
    ]

class StatsParser ( Parser ):

    grammarFileName = "Stats.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "','", "'('", "')'", 
                     "'='", "'!='", "'>'", "'<'", "'>='", "'<='", "'*'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "SELECT", "WHERE", "AS", "AVG", 
                      "SUM", "COUNT", "MIN", "MAX", "HISTOGRAM", "BINS", 
                      "AND", "OR", "SEMI", "COMMA", "LPAREN", "RPAREN", 
                      "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "STAR", "STRING", 
                      "NUMBER", "IDENT", "LINE_COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_loadStmt = 2
    RULE_queryStmt = 3
    RULE_aggList = 4
    RULE_aggExpr = 5
    RULE_aggFunc = 6
    RULE_histogramStmt = 7
    RULE_boolExpr = 8
    RULE_comparison = 9
    RULE_comparator = 10
    RULE_value = 11

    ruleNames =  [ "prog", "stmt", "loadStmt", "queryStmt", "aggList", "aggExpr", 
                   "aggFunc", "histogramStmt", "boolExpr", "comparison", 
                   "comparator", "value" ]

    EOF = Token.EOF
    LOAD=1
    SELECT=2
    WHERE=3
    AS=4
    AVG=5
    SUM=6
    COUNT=7
    MIN=8
    MAX=9
    HISTOGRAM=10
    BINS=11
    AND=12
    OR=13
    SEMI=14
    COMMA=15
    LPAREN=16
    RPAREN=17
    EQ=18
    NEQ=19
    GT=20
    LT=21
    GTE=22
    LTE=23
    STAR=24
    STRING=25
    NUMBER=26
    IDENT=27
    LINE_COMMENT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(StatsParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatsParser.StmtContext)
            else:
                return self.getTypedRuleContext(StatsParser.StmtContext,i)


        def getRuleIndex(self):
            return StatsParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = StatsParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1030) != 0):
                self.state = 24
                self.stmt()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(StatsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStmt(self):
            return self.getTypedRuleContext(StatsParser.LoadStmtContext,0)


        def SEMI(self):
            return self.getToken(StatsParser.SEMI, 0)

        def queryStmt(self):
            return self.getTypedRuleContext(StatsParser.QueryStmtContext,0)


        def histogramStmt(self):
            return self.getTypedRuleContext(StatsParser.HistogramStmtContext,0)


        def getRuleIndex(self):
            return StatsParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = StatsParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.loadStmt()
                self.state = 33
                self.match(StatsParser.SEMI)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.queryStmt()
                self.state = 36
                self.match(StatsParser.SEMI)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.histogramStmt()
                self.state = 39
                self.match(StatsParser.SEMI)
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


    class LoadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(StatsParser.LOAD, 0)

        def STRING(self):
            return self.getToken(StatsParser.STRING, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_loadStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStmt" ):
                listener.enterLoadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStmt" ):
                listener.exitLoadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStmt" ):
                return visitor.visitLoadStmt(self)
            else:
                return visitor.visitChildren(self)




    def loadStmt(self):

        localctx = StatsParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(StatsParser.LOAD)
            self.state = 44
            self.match(StatsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(StatsParser.SELECT, 0)

        def aggList(self):
            return self.getTypedRuleContext(StatsParser.AggListContext,0)


        def WHERE(self):
            return self.getToken(StatsParser.WHERE, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(StatsParser.BoolExprContext,0)


        def getRuleIndex(self):
            return StatsParser.RULE_queryStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryStmt" ):
                listener.enterQueryStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryStmt" ):
                listener.exitQueryStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryStmt" ):
                return visitor.visitQueryStmt(self)
            else:
                return visitor.visitChildren(self)




    def queryStmt(self):

        localctx = StatsParser.QueryStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_queryStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(StatsParser.SELECT)
            self.state = 47
            self.aggList()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 48
                self.match(StatsParser.WHERE)
                self.state = 49
                self.boolExpr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatsParser.AggExprContext)
            else:
                return self.getTypedRuleContext(StatsParser.AggExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatsParser.COMMA)
            else:
                return self.getToken(StatsParser.COMMA, i)

        def getRuleIndex(self):
            return StatsParser.RULE_aggList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggList" ):
                listener.enterAggList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggList" ):
                listener.exitAggList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggList" ):
                return visitor.visitAggList(self)
            else:
                return visitor.visitChildren(self)




    def aggList(self):

        localctx = StatsParser.AggListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.aggExpr()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 53
                self.match(StatsParser.COMMA)
                self.state = 54
                self.aggExpr()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggFunc(self):
            return self.getTypedRuleContext(StatsParser.AggFuncContext,0)


        def LPAREN(self):
            return self.getToken(StatsParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(StatsParser.RPAREN, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(StatsParser.IDENT)
            else:
                return self.getToken(StatsParser.IDENT, i)

        def STAR(self):
            return self.getToken(StatsParser.STAR, 0)

        def AS(self):
            return self.getToken(StatsParser.AS, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_aggExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggExpr" ):
                listener.enterAggExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggExpr" ):
                listener.exitAggExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggExpr" ):
                return visitor.visitAggExpr(self)
            else:
                return visitor.visitChildren(self)




    def aggExpr(self):

        localctx = StatsParser.AggExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aggExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.aggFunc()
            self.state = 61
            self.match(StatsParser.LPAREN)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==24 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            self.match(StatsParser.RPAREN)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 64
                self.match(StatsParser.AS)
                self.state = 65
                self.match(StatsParser.IDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AVG(self):
            return self.getToken(StatsParser.AVG, 0)

        def SUM(self):
            return self.getToken(StatsParser.SUM, 0)

        def COUNT(self):
            return self.getToken(StatsParser.COUNT, 0)

        def MIN(self):
            return self.getToken(StatsParser.MIN, 0)

        def MAX(self):
            return self.getToken(StatsParser.MAX, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_aggFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggFunc" ):
                listener.enterAggFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggFunc" ):
                listener.exitAggFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggFunc" ):
                return visitor.visitAggFunc(self)
            else:
                return visitor.visitChildren(self)




    def aggFunc(self):

        localctx = StatsParser.AggFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HistogramStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HISTOGRAM(self):
            return self.getToken(StatsParser.HISTOGRAM, 0)

        def IDENT(self):
            return self.getToken(StatsParser.IDENT, 0)

        def BINS(self):
            return self.getToken(StatsParser.BINS, 0)

        def EQ(self):
            return self.getToken(StatsParser.EQ, 0)

        def NUMBER(self):
            return self.getToken(StatsParser.NUMBER, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_histogramStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHistogramStmt" ):
                listener.enterHistogramStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHistogramStmt" ):
                listener.exitHistogramStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHistogramStmt" ):
                return visitor.visitHistogramStmt(self)
            else:
                return visitor.visitChildren(self)




    def histogramStmt(self):

        localctx = StatsParser.HistogramStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_histogramStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(StatsParser.HISTOGRAM)
            self.state = 71
            self.match(StatsParser.IDENT)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 72
                self.match(StatsParser.BINS)
                self.state = 73
                self.match(StatsParser.EQ)
                self.state = 74
                self.match(StatsParser.NUMBER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(StatsParser.LPAREN, 0)

        def boolExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatsParser.BoolExprContext)
            else:
                return self.getTypedRuleContext(StatsParser.BoolExprContext,i)


        def RPAREN(self):
            return self.getToken(StatsParser.RPAREN, 0)

        def comparison(self):
            return self.getTypedRuleContext(StatsParser.ComparisonContext,0)


        def AND(self):
            return self.getToken(StatsParser.AND, 0)

        def OR(self):
            return self.getToken(StatsParser.OR, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)



    def boolExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = StatsParser.BoolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_boolExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 78
                self.match(StatsParser.LPAREN)
                self.state = 79
                self.boolExpr(0)
                self.state = 80
                self.match(StatsParser.RPAREN)
                pass
            elif token in [27]:
                self.state = 82
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = StatsParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        self.match(StatsParser.AND)
                        self.state = 87
                        self.boolExpr(5)
                        pass

                    elif la_ == 2:
                        localctx = StatsParser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 88
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 89
                        self.match(StatsParser.OR)
                        self.state = 90
                        self.boolExpr(4)
                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(StatsParser.IDENT, 0)

        def comparator(self):
            return self.getTypedRuleContext(StatsParser.ComparatorContext,0)


        def value(self):
            return self.getTypedRuleContext(StatsParser.ValueContext,0)


        def getRuleIndex(self):
            return StatsParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = StatsParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(StatsParser.IDENT)
            self.state = 97
            self.comparator()
            self.state = 98
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(StatsParser.EQ, 0)

        def NEQ(self):
            return self.getToken(StatsParser.NEQ, 0)

        def GT(self):
            return self.getToken(StatsParser.GT, 0)

        def LT(self):
            return self.getToken(StatsParser.LT, 0)

        def GTE(self):
            return self.getToken(StatsParser.GTE, 0)

        def LTE(self):
            return self.getToken(StatsParser.LTE, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = StatsParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(StatsParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(StatsParser.STRING, 0)

        def getRuleIndex(self):
            return StatsParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = StatsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.boolExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolExpr_sempred(self, localctx:BoolExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




