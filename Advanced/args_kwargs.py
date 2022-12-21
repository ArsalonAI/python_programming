
# *args - allows us to pass any number of arguments to a function
# stores all args in a tuple as they appear

def sum_items(*args):
    print(sum(args))
    
sum_items(1, 2, 3)
sum_items(2, 3, 4, 5, 6, 7)


# **kwargs allows us to pass keyword arguments - stores in a dictionary
def print_items(*args, **kwargs):
    print(args)
    print(kwargs)
    
print_items(1, 2, a = 3, b = "string", c = 9)

# pass elements in a datastructure to a function as parameters 
def take_items(a, b, c):
    return a + b + c 

items = [4, 5, 6]

# this becomes inefficient with many argument
x = take_items(items[0], items[1], items[2]) 
print(x)

# splat operator - one star '*' unpacks a list
y = take_items(*items) # separates the positional datastructure (collection), passing each element one at a time to the fn as parameters
print(y)

new_items = {"a" : 10, "b" : 15, "c" : 24}

z = take_items(**new_items) # double '**' unpacks a dictionary
print(z)