
# Nested Function basics  

    # enclosing function - contains another function inside of it
    # nested function - function defined inside another function 

from re import X


def outer(x):
    def inner(y):
        print(x + y) # local to outter function scope (function defined inside function)
        
    return inner 

func = outer(5) # returns func (inner), w/ parameter plugged inside
func(6) # call func returned from enclosing function, passing second parameter to function

def outer_two(x):
    def inner(y):
        print(x + y)
        
    inner(5) # can call nested func w/in enclosing func
    
outer_two(5)

def outer_three(x):
    def inner(y):
        def inner2(z):
            print(x + y + z) 
        
        return inner2 # inner func (nested func #1) returns inner2 func (nested func w/ in inner func)
    
    return inner # outer_three (enclosing) func returns inner func (nested func)

outer_three(5)(4)(3) # outer_three(5) returns fn inner, then call fn inner(4) which returns inner2, call inner2(5) which prints x+y+z 

# closures 
def outer_four(x):
    def inner():
        print(x) # closure - accesses a "free variable" a variable from enclosing func scope (not it's local scope)
        
    return inner

outer_four(15)()

def collection():
    
    lst = [] # scoped to enclosing function, accessible within all nested function scopes
    
    def inner(value):
        lst.append(value)
        return lst
    return inner

add_value = collection()
print(add_value(1))
print(add_value(2))
print(add_value(3))

# Closure example - enclosing function "free variable" used w/in nested function cannot be directly mutated, use nonlocal keyword
def counter(start):
    count = start # immutable free variable (enclosing function scope), accessible by nested functions
    
    def increment(value):
        nonlocal count # allows us to access enclosing function free variable w/o creating a locally defined variable within nested function scope
        count += value 
        return count 
    
    return increment


print(counter(2)(3)) # start at 2, increment by 3


# Closure Example - nonlocal keyword references closest variable within nested structure (closest enclosing function)
def outer_example():
    def inner():
        def inner2():
            nonlocal x 
            x = 2
            print("Inner2 func x value:", x)
            
        x = 3
        inner2()
        print("Inner func x value:", x)
        
    x = 4
    inner()
    print("Outer func x value:", x)
    
outer_example()
