class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("You must implement this method")
    
    def execute_code(self):
        raise NotImplementedError("You must implement this method") 
    
class GoCode(RunCodeInterface):
    def compile_code(self):
        print("compiling code")
        
    def execute_code(self):
        print("Execute GO code now")
    
class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("compiling code")
        
    def execute_code(self):
        print("Execute Java code now")
        

def run_code(code : RunCodeInterface):
    code.compile_code()
    code.execute_code()

go = GoCode()
java = JavaCode()
run_code(java)
run_code(go)
