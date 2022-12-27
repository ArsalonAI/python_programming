import time 
# decorators - functions that take in functions, check them for certain constraints, calls function if okay
# purpose - enforces a behavior or do something before/after a function is called


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Top Bun!")
        result = func(*args, **kwargs)
        print("Bottom Bun!")
        return result
    
    return wrapper 

# Create a Decorator Func - will start timer before calling arg function, return total execution time of passed func
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)

        end_time = time.time()
        total_time = end_time - start_time
        print("Time to execute function", total_time)
        return result
    
    return wrapper

def pretty_printer(func):
    def wrapper(*args, **kwargs):
        
        print("This is a line executed before the function")
        result = func(*args, **kwargs)
        print("This is a line executed after the function")
        
        return result
    
    return wrapper

# Decorate the funcs w/ timer decorator 
@decorator  
def foo(x, y, z = None):
    print(x, y, z)
    
    
@timer 
def loop():
    for _ in range(100000):
        pass

@timer  
def get_max(x, y, z):
    loop()
    return max(x, y, z)


# Decorate a func w/ multiple decorators 
@timer
@pretty_printer
def print_numbers(num):
    for i in range(num):
        pass
    

# Call decorated functions
foo(1, 7, z = 10)
loop()  
print(get_max(1, 2, 3)) 
print_numbers(100)   
