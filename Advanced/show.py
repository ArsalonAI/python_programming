# Closure example - enclosing function "free variable" used w/in nested function cannot be directly mutated 
def counter(start):
    count = start # immutable free variable (enclosing function scope), accessible by nested functions
    
    def increment(value):
        nonlocal count # allows us to access enclosing function free variable w/o creating a locally defined variable within nested function scope
        count += value 
        return count 
    
    return increment


print(counter(2)(3)) # start at 2, increment by 3
