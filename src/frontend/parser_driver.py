import os
from antlr4 import FileStream, CommonTokenStream
from generated.StatsLexer import StatsLexer
from generated.StatsParser import StatsParser
from src.frontend.error_listener import MyErrorListener
from src.backend.stats_visitor import StatsVisitorImpl

class ParserDriver:
    def __init__(self):
        pass

    def run(self, filename):
        print("══════════════════════════════════════════════════")
        print(f"Analizando archivo: {filename}")
        print("══════════════════════════════════════════════════")

        input_stream = FileStream(filename, encoding='utf-8')
        lexer = StatsLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = StatsParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.prog()
        print("\nÁrbol de parseo:")
        print(tree.toStringTree(recog=parser))

        # Backend
        visitor = StatsVisitorImpl()
        visitor.visit(tree)
