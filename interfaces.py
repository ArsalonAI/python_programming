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


import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2
        
    def get_perimeter(self):
        return 4 * (self.side_length)

class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self,):
        return math.pi * (self.radius ** 2)
        
    def get_perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(3)
print(c.get_area())
print(c.get_perimeter())

s = Square(2)
print(s.get_area())
print(s.get_perimeter())
