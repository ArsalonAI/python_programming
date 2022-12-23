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