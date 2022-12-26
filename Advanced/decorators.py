# decorators - functions that take in functions, check them for certain constraints, calls function if okay


def decorator(func):
    def wrapper(x):
        print("Wrapper function called func!", x)
        result = func()
        return result
    
    return wrapper 

@decorator  
def foo():
    print("foo")

foo(1)