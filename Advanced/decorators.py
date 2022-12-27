# decorators - functions that take in functions, check them for certain constraints, calls function if okay
# purpose - enforces a behavior or do something before/after a function is called



def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper function called func!")
        result = func(*args, **kwargs)
        return result
    
    return wrapper 

@decorator  
def foo(x, y, z = None):
    print(x, y, z)

foo(1, 7, z = 10)


# Decorator - Example for timing function execution 
import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        total_time = end_time - start_time
        print("Time to execute function", total_time)
        return result
    
    return wrapper


@timer
def loop():
    for _ in range(100000000):
        pass

loop()  

@timer
def get_max(x, y, z):
    loop()
    return max(x, y, z)

print(get_max(1, 2, 3))
      