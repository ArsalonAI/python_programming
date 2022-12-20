
def foo():
    print("foo")
    
def bar():
    print("bar")

class MyClass: 
    @staticmethod
    def test():
        print("this is my class import test")
    
# run code only if this file is run directly (as main), if imported, doesn't run this code
if __name__ == "__main__":
    print("hello world")
    
