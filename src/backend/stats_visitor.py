from generated.StatsVisitor import StatsVisitor
from src.backend.codegen import CodeGen

class StatsVisitorImpl(StatsVisitor):
    def __init__(self):
        self.codegen = CodeGen()

    def visitProg(self, ctx):
        print("Recorriendo árbol de parseo")
        self.codegen.create_main_function()
        for stmt in ctx.stmt():
            self.visit(stmt)
        self.codegen.end_main_function()
        print(self.codegen.get_ir())

    def visitLoadStmt(self, ctx):
    	string_token = ctx.STRING()
    	if string_token is None:
        	print("Error semántico: falta el nombre del archivo entre comillas en 'load'.")
        	return None
    	filename = string_token.getText().strip('"')
    	print(f"LOAD → {filename}")
    	print(f"IR: print('Load dataset \"{filename}\"')")
    	return None

    def visitQueryStmt(self, ctx):
        print("SELECT →", ctx.getText())
        self.codegen.emit_print("SELECT query")

    def visitHistogramStmt(self, ctx):
        col = ctx.IDENT().getText()
        print(f"HISTOGRAM → {col}")
        self.codegen.emit_print(f"Histogram of {col}")
