from llvmlite import ir

class CodeGen:
    def __init__(self):
        self.module = ir.Module(name="StatsLangModule")
        self.builder = None
        self.main_func = None

    def create_main_function(self):
        func_type = ir.FunctionType(ir.VoidType(), [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def end_main_function(self):
        if self.builder:
            self.builder.ret_void()

    def emit_print(self, text: str):
        print(f"IR: print('{text}')")

    def get_ir(self):
        return str(self.module)
