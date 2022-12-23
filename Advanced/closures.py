
# Nested Function basics  

    # enclosing function - contains another function inside of it
    # nested function - function defined inside another function 

def outer(x):
    def inner(y):
        print(x + y) # local to outter function scope (function defined inside function)
        
    return inner 

func = outer(5) # returns func (inner), w/ parameter plugged inside
func(6) # call func returned from enclosing function, passing second parameter to function

