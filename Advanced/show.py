# Closure example 
def counter(start):
    count = start # immutable free variable (enclosing function scope), accessible by nested functions
    
    def increment(value):
        count += value # not same as free variable "count" this creates a new variable, locally accessible
        return count 
    
    return increment


print(counter(2)(3)) # start at 2, increment by 3
